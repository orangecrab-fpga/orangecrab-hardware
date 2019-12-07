#!/usr/bin/env python
import pcbnew
import re
import os.path
import sys
import time

def main(filename):
    pcb = pcbnew.LoadBoard(filename)
    pcb.BuildListOfNets() # required so 'pcb' contains valid netclass data
    from IPython import embed; embed()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: %s <boardname.kicad_pcb>" % sys.argv[0])
        sys.exit(1)
    main(sys.argv[1])
