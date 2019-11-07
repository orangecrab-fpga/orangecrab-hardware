#!/usr/bin/env python3

import os

os.system("openocd -f openocd/ecp5-versa5g.cfg -c \"transport select jtag; init; svf build/gateware/top.svf; exit\"")
