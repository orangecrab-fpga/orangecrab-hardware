#!/usr/bin/env python3

import os
import sys

if len(sys.argv) < 2:
    print("usage: ./load_firmware.py /dev/ttyUSBX")
    exit(1)

os.system("cd firmware && make clean all")
os.system("litex_term --kernel=firmware/firmware.bin --kernel-adr=0x20000000 " + sys.argv[1])
