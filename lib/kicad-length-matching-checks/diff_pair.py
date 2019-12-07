#!/usr/bin/env python
import pcbnew
import re
import os.path
import sys
import time
"""
Very basic differential pair length making checker script for KiCad

This is not very fancy, but it can be used to create length matched
differential pairs. You can set an intra-pair matching tolerance (ie
each pair of traces must match to this tolerance), and an inter-pair
matching tolerance (ie no pair in a group of pairs can exceed that
difference between the pairs).

For an example of a board that uses this, look at:
http://github.com/projectgus/novepad

HOW TO USE:

* Compile KiCad with Python scripting support (this isn't enabled by default
  and requires a rebuild, if you look in kicad-install.sh there's a line
  marked with "# Python scripting, uncomment to enable")

* Put each group of nets that should be length matched into their own
  netclass, named with the suffix _DPxxx/yyy, where xxx is the
  intra-pair matching tolerance in millimetres, and yyy is the
  inter-pair matching tolerance in millimetres.

  For example, the netclass name LVDS_DP1.2/5 means that all the
  individual pairs in that netclass need to match within 1.2mm, and
  also all traces in that netclass should be matched within 5mm
  overall.

  If you don't care about inter-pair length matching (for instance,
  your pairs are totally unrelated or are self-clocking) then just put
  a large value like 1000mm for the inter-pair part of the match - ie
  LVDS_DP1.2/1000.

* Name each net using the naming scheme <pairname>_<pairsubpart> using
  an underscore, for instance the net names LVDS_CLK_N and LVDS_CLK_P
  will belong to the same "LVDS_CLK" pair. Add these nets to the length
  matching netclass.

  Actually, "pairs" can have more than 2 nets in them so you could
  also have net names like DATA_1, DATA_2, DATA_3 that will all belong
  to the same "pair". The <pairsubpart> doesn't matter, what matters
  is that the part before the final underscore is the same.

* Run this script as "diff_pairs.py <nameofboardfile>", and it will
  print pass/fail length match data & lengths for each netclass that
  meets the _DP naming scheme. Intra-pair pass/fail for a netclass is
  printed first, then inter-pair. Individual trace lengths are only
  printed if the matching fails (as the output gets kind of long
  otherwise).

* The script will keep running, and any time you save the board file
  it will re-examine any netclasses where at least one length has
  changed and print the new results. The idea is to keep this script
  running in a side window while you route your board.

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
  requires "ansi.sys" loaded. If you're red/green colourblind then you
  might want to edit the script, sorry!


There is tons of room for improvement in this script, so if you add
any improvements please let me know so I can use them too. :)

(C)2014 Angus Gratton @projectgus, Licensed under New BSD License

"""

BRIGHTGREEN = '\033[92;1m'
GREEN = '\033[92m'
BRIGHTRED = '\033[91;1m'
RED = '\033[91m'
ENDC = '\033[0m'

def print_color(color, s):
    print(color + s + ENDC)

def get_board_pairs(filename):
    """
    Returns a dict from pair netclass name -> (intrapair tolerance, interpair tolerance, list of pairs)
    Where 'pairs' are a list of lists of tuples of netnames and their lengths.

    Only netclasses with differential matching tolerances are returned
    """
    pcb = pcbnew.LoadBoard(filename)
    pcb.BuildListOfNets() # required so 'pcb' contains valid netclass data

    tolerances = {}
    nets = {}

    tracks = pcb.GetTracks() # tuples of (netname, classname)
    netclasses = list(set(t.GetNet().GetClassName()  for t in tracks)) # unique netclass names

    result = {}
    for netclass in netclasses:
        tolerance = get_tolerance(netclass)
        if tolerance is None:
            continue
        intra,inter = tolerance
        tracks_netclass = [t for t in tracks if t.GetNet().GetClassName() == netclass] # tracks in this netclass
        netnames = list(set([t.GetNet().GetNetname() for t in tracks_netclass])) # unique netnames in this netclass
        netnames.sort()

        pairnames = list(set([get_pairname(netname) for netname in netnames]))

        def get_netlength(netname):
            return int(sum(t.GetLength() for t in tracks_netclass if t.GetNet().GetNetname() == netname))

        pairs = [ [(n,get_netlength(n)) for n in netnames if get_pairname(n)==p] for p in pairnames ]
        result[netclass] = (intra, inter, pairs)
    return result

def nm_to_mm(nm):
    return float(nm) / 1e6

def mm_to_nm(mm):
    return int(mm * 1e6)

def get_tolerance(classname):
    "Returns a tuple of the differential pair tolerances (intrapair, interpair) encoded in a netclass match, or None if not a matched length"
    name = re.search(r"(^|_)DP([0-9\.]+)/([0-9\.]+)$", classname)
    if name is None:
        return None
    return ( mm_to_nm(float(name.group(2))), mm_to_nm(float(name.group(3))) )

def get_pairname(netname):
    "Return a 'pair' name for a netname like SIGNAL for SIGNAL_P or SIGNAL_N."
    if netname.endswith('_N') or netname.endswith("_P"):
        return netname[:-2]
    if netname.endswith('+') or netname.endswith("-"):
        return netname[:-1]
    return netname

def median(x):
    "Return median from a list of values. Thanks to http://stackoverflow.com/a/25791644"
    if len(x)%2 != 0:
        return sorted(x)[len(x)/2]
    else:
        midavg = (sorted(x)[len(x)/2] + sorted(x)[len(x)/2-1])/2.0
        return midavg

def mean(x):
    return sum(x)/len(x) if len(x) > 0 else None

def test_pairs(netclass, intra_tolerance, inter_tolerance, pairs):
    """
    Test the given netclass name for the given differential pair tolerances
    nets is a list of (netname, length) for all nets in the netclass.
    """
    pairs.sort()

    all_lengths = [[p[1] for p in pair] for pair in pairs]
    minlen = min([min(p[1] for p in pair) for pair in pairs])
    maxlen = max([max(p[1] for p in pair) for pair in pairs])
    delta = maxlen - minlen
    meets = delta < inter_tolerance

    matches = True

    print_color(BRIGHTGREEN if meets else BRIGHTRED, "%s -> %s INTER-PAIR TOLERANCE %.4f mm (current delta %.4f)" % (netclass, "MEETS" if meets else "FAILS", nm_to_mm(inter_tolerance), nm_to_mm(delta)))
    if not meets:
        matches = False
        # print mean length of each pair
        for pair in pairs:
            print("  %s mean length %.4f mm" % (get_pairname(pair[0][0]), nm_to_mm(mean([p[1] for p in pair]))))

    for pair in pairs:
        mintrace = min(p[1] for p in pair)
        maxtrace = max(p[1] for p in pair)
        tracedelta = maxtrace - mintrace
        meantrace = mean([p[1] for p in pair])
        meets = tracedelta < intra_tolerance
        print_color(ENDC if meets else RED, "    %s %s intra-pair tolerance %.4f mm (current delta %.4f)" % (get_pairname(pair[0][0]), "meets" if meets else "fails",
                                                                           nm_to_mm(intra_tolerance), nm_to_mm(tracedelta)))
        # print comparison of each net length to the mean length in this pair
        if not meets:
            matches = False
            for p in pair:
                print_color(RED, "        %s length %.4f (%.4f)" % (p[0], nm_to_mm(p[1]), nm_to_mm(p[1]-meantrace)))

    return matches


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
        while (mtime == lastmtime) and not first:
            try:
                mtime = os.path.getmtime(filepath)
            except OSError:
                pass # kicad save process seems to momentarily delete file, so there's a race here with "No such file.."
            time.sleep(0.05)

        first = False
        allmatches = True
        props = get_board_pairs(filepath)
        for (netclass, (intra, inter, pairs)) in sorted(props.items()):
            # only re-test any netclasses whose contents have changed
            try:
                if str(oldprops[netclass]) == str(props[netclass]):
                    continue
            except KeyError:
                pass
            allmatches = test_pairs(netclass, intra, inter, pairs) and allmatches
        if "--once" in sys.argv:
            sys.exit(not allmatches)
        oldprops = props
