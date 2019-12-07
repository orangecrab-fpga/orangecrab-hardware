#!/usr/bin/env python
import pcbnew
from pcbnew import *
import re
import os.path
import sys
import time
"""
Very basic length making checker script for KiCad

This is not very fancy, but it can be used to create length matched traces.

HOW TO USE:

* Compile KiCad with Python scripting support (this isn't enabled by default
  and requires a rebuild, if you look in kicad-install.sh there's a line
  marked with "# Python scripting, uncomment to enable")

* Put each group of nets that should be length matched into their own
  netclass, named with the suffix _LMxxx, where xxx is the matching
  tolerance in millimetres.

  For example, the netclass name DATABUS_LM1.2 means all nets in that
  netclass should match within 1.2mm of each other.

* Run this script as "lengthmatch.py <nameofboardfile>", and it will print
  pass/fail length match data & lengths for each netclass that meets the _LM
  naming scheme.

* The script will keep running, and any time you save the board file
  it will re-examine any netclasses where at least one length has
  changed and print the new results. The idea is to keep this script
  open in a side window while you route your board.

* Once you think everything is correct, Ctrl-C to kill the script
  and then rerun it to double check all netclasses (in case you missed
  any netclasses that haven't changed in a while).

TIPS:

* You can't edit netclass names (to change tolerances, for example)
  inside the pcbnew editor, but you can edit the board file in a text
  editor and reload.

* The length matching just counts the total length of all traces in
  the net, so it doesn't know about geometry or overlapping traces or
  multi-ended traces or stubs. For this reason:

  * Use "magnetic pads" (under Preferences->General) so traces always
    begin & end in the middle of the pad.

  * Route in outline view mode (buttons at bottom left toolbar thingy)
    so you can easily see any accidental overlapping traces (including
    under pads) and delete them. One stray trace scrap under a pad can
    ruin your matching!

  * Use the Edit->Cleanup Tracks And Vias options to merge any
    overlapping traces (NB this can sometimes makes a mess of your
    board, so save first!)

* Length matching also doesn't account for vias, so try and match the
  numbers of these.

* Coloured text output should work on Linux and OS X but on Windows it
  requires "ansi.sys" loaded.


There is tons of room for improvement in this script, so if you add
any improvements please let me know so I can use them too. :)

(C)2014 Angus Gratton @projectgus, Licensed under New BSD License
(C)2019 Gregory Davill <greg.davill@gmail.com>

"""


# Very proof of concept code that creates a graph of the tracks branching out from one pad.

class Node():
    """A node class to create a graph"""

    def __init__(self, parent=None, length=None, position=None, track=None):
        self.parent = parent
        self.length = length
        self.position = position
        self.track = track
        self.children = []



def add_track(node, nt):
    # if equal don't add
    if node.track != None:
        if node.track == nt:
            return False

    # store our position as the other end of our track
    res = nt.IsPointOnEnds(node.position)
    if res == STARTPOINT:
        node.children += [Node(node, nt.GetLength(), nt.GetEnd(), nt)]
        return True
    elif res == ENDPOINT:
        node.children += [Node(node, nt.GetLength(), nt.GetStart(), nt)]
        return True
    else:
        for c in node.children:
            if add_track(c, nt):
                return True

    return False

def print_tree(n):
    print('%.1f,%.1f - (%.2f)mm' % (nm_to_mm(n.position.x),nm_to_mm(n.position.y), nm_to_mm(n.length)))
    print(' > ' + str(n.children))
    for c in n.children:
        print_tree(c)


def find_length(n, stop):
    if n.position == stop:
        #print("found!!")
        return n.length + 0.001 # small hack to ensure if we find the end a value propagates back.

    for c in n.children:
        length = find_length(c, stop)
        if length > 0.0001:
            return length + n.length

    return 0.0
            
    


BRIGHTGREEN = '\033[92;1m'
BRIGHTRED = '\033[91;1m'
ENDC = '\033[0m'

def print_color(color, s):
    print(color + s + ENDC)


def FindPadByNetName(mod, n):  
    for p in mod.Pads():
        if p.GetNetname() == n:
            return p
    return None

def findFirst(tracks, s):
    for t in tracks:
        if t.IsPointOnEnds(s):
            return t

def get_board_properties(filename):
    """
    Returns a dict from netclass name -> (tolerance, nets)
    Where tolerance is maximum difference in matched track lengths.
    And nets is a list of (netname, length) for each net in the netclass.

    Only netclasses with length matching tolerances are returned
    """
    pcb = pcbnew.LoadBoard(filename)
    pcb.BuildListOfNets() # required so 'pcb' contains valid netclass data

    tolerances = {}

    tracks = pcb.GetTracks() # tuples of (netname, classname)
    netclasses = list(set(t.GetNet().GetClassName()  for t in tracks)) # unique netclass names

    result = {}

    # Device A
    deviceA = pcb.FindModuleByReference("U3")
    deviceB = pcb.FindModuleByReference("U4")
    
    for netclass in netclasses:
        tolerance = get_tolerance(netclass)
        if tolerance is None:
            continue
        tracks_netclass = [t for t in tracks if t.GetNet().GetClassName() == netclass] # tracks in this netclass
        netnames = list(set([t.GetNet().GetNetname() for t in tracks_netclass])) # unique netnames in this netclass
        netnames.sort()

        nets = []
        for n in netnames:
            length = 0
            tracks_filtered = [t for t in tracks_netclass if (t.GetNet().GetNetname() == n ) & (t.IsTrack() == True)]

            pad_a = FindPadByNetName(deviceA, n)
            pad_b = FindPadByNetName(deviceB, n)

            t = None#,start = findFirst(tracks_filtered, pad_a.GetPosition())
            
            for f in tracks_filtered: 
                if f.IsPointOnEnds(pad_a.GetPosition(),mm_to_nm(0.001)):
                    start = f.IsPointOnEnds(pad_a.GetPosition(),mm_to_nm(0.001)) == STARTPOINT
                    t = f
                    break
            if start == None:
                continue

            tracks_filtered = [tr for tr in tracks_filtered if tr != t]

            #print('%s %d'% (n, len(tracks_filtered)))

            # got starting point
            root = Node(position=pad_a.GetPosition(), length=0.0)
            add_track(root,t)

            done = [t]
            for _ in range(len(tracks_filtered)):
                for t in (set(tracks_filtered) - set(done)):
                    if add_track(root,t):
                        done += [t]
                
            #print_tree(root)
            length = find_length(root, pad_b.GetPosition())
        
            nets += [(n,length)]


        result[netclass] = (tolerance, nets)
    return result

def nm_to_mm(nm):
    return float(nm) / 1e6

def mm_to_nm(mm):
    return int(mm * 1e6)

def get_tolerance(classname):
    "Returns the length match tolerance encoded in a netclass match, or None if not a matched length"
    name = re.search(r"(^|_)LM([0-9\.]+)($|_)", classname)
    if name is None:
        return None
    return mm_to_nm(float(name.group(2)))

def median(x):
    "Return median from a list of values. Thanks to http://stackoverflow.com/a/25791644"
    if len(x)%2 != 0:
        return sorted(x)[int(len(x)/2)]
    else:
        midavg = (sorted(x)[int(len(x)/2)] + sorted(x)[int(len(x)/2-1)])/2.0
        return midavg

def test_netclass(netclass, tolerance, nets):
    """
    Test the given netclass name for the given length matching tolerances.
    nets is a list of (netname, length) for all nets in the netclass.
    """
    nets.sort()

    minlen = min(net[1] for net in nets)
    maxlen = max(net[1] for net in nets)
    delta = maxlen - minlen
    meets = delta < tolerance

    print_color(BRIGHTGREEN if meets else BRIGHTRED,
                "%s -> %s TOLERANCE %.2f (max variance %.2f)" % (netclass, "MEETS" if meets else "FAILS", nm_to_mm(tolerance), nm_to_mm(delta)))
    # print individual net lengths, relative to the median length
    medlen = median([net[1] for net in nets])
    for (net,netlen) in nets:
        if (netlen == minlen) & (~meets):
            print_color(BRIGHTRED,
            "   %s %.2fmm (%s%.2fmm)" % (net,nm_to_mm(netlen),"+" if netlen > medlen else "",  nm_to_mm(netlen-medlen)))
        elif (maxlen - netlen) < tolerance:
            print_color(BRIGHTGREEN,
            "   %s %.2fmm (%s%.2fmm)" % (net,nm_to_mm(netlen),"+" if netlen > medlen else "",  nm_to_mm(netlen-medlen)))
        else:
            print("   %s %.2fmm (%s%.2fmm)" % (net,nm_to_mm(netlen),"+" if netlen > medlen else "",  nm_to_mm(netlen-medlen)))

    return meets


if __name__ == "__main__":
    try:
        filepath = sys.argv[1]
    except IndexError:
        print("Usage: %s <boardname.kicad_pcb> [--once]" % sys.argv[0])
        sys.exit(1)
    oldprops = {}
    first = True

    while True:
        # wait for the file contents to change
        lastmtime = os.path.getmtime(filepath)
        mtime = lastmtime
        while mtime == lastmtime and not first:
            try:
                mtime = os.path.getmtime(filepath)
            except OSError:
                pass # kicad save process seems to momentarily delete file, so there's a race here with "No such file.."
            time.sleep(0.05)

        first = False
        allmatches = True
        props = get_board_properties(filepath)
        for (netclass, (tolerance, nets)) in sorted(props.items()):
            # only re-test any netclasses whose contents have changed
            try:
                if oldprops[netclass] == (tolerance, nets):
                    continue
            except KeyError:
                pass
            allmatches = test_netclass(netclass, tolerance, nets) and allmatches
        if "--once" in sys.argv:
            sys.exit(not allmatches)
        oldprops = props
