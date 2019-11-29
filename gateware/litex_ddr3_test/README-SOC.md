# OrangeCrab DDR3 SoC test code

``` Currently under-development ``` 

## Build Instructins
```console
$ python3 OrangeCrab-bitstream.py base
 ```

This will invoke Litex/Migen with Lattice Diamond to compile bios and generate bitstream for the ECP5.
When the synthesis is complete you will be left with "build/gateware/top.svf"

## Loading
Run this command to invoke openOCD and load the bitstream onto the FPGA via a JTAG adapter
 ```console
$ python3 load_fpga.py 
 ```


## Watch the BIOS run
Connect a serial link to the OrangeCrab on its external pins 0/1. 

In a new terminal run the litex_term (Or another Serial terminal such as screen), reload the bitstream to see this splash screen.
```console
$ litex_term --speed 115200 [port]
  [LXTERM] Starting....
  
          __   _ __      _  __
         / /  (_) /____ | |/_/
        / /__/ / __/ -_)>  <
       /____/_/\__/\__/_/|_|
  
   (c) Copyright 2012-2019 Enjoy-Digital
   (c) Copyright 2007-2015 M-Labs Ltd
  
   BIOS built on Nov 29 2019 14:50:06
   BIOS CRC passed (02af119d)
  
   Migen git sha1: 57a7311
   LiteX git sha1: 427d7af7
  
  --============ SoC info ================--
  CPU:       VexRiscv @ 48MHz
  ROM:       32KB
  SRAM:      4KB
  L2:        8KB
  MAIN-RAM:  131072KB
  
  --========= Peripherals init ===========--
  Initializing SDRAM...
  SDRAM now under software control
  Read leveling:
  m0, b0: |11100000| delays: 01+-01
  best: m0, b0 delays: 01+-01
  m1, b0: |11100000| delays: 01+-01
  best: m1, b0 delays: 01+-01
  SDRAM now under hardware control
  Memtest OK
  
  --========== Boot sequence =============--
  Booting from serial...
  Press Q or ESC to abort boot completely.
  sL5DdSMmkekro
  Timeout
  No boot medium found
  
  --============= Console ================--
  litex> ident
  Ident: OrangeCrab test SoC
  litex> 
```
