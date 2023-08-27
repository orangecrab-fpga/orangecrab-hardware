---
title: Getting Started
type: docs
rev: r0.2
---

# Getting Started

First time using an FPGA? This guide should cover everything you need to get the example verilog project built and loaded up on the OrangeCrab.

## Toolchain Setup
---

This guide will make use of the Open Source FPGA toolchain. It is possible to build and install these from scratch, but the whole process takes around 30 minutes, and can be a bit tricky if you're just getting started. 

It's advised to use an automated build from [YosysHQ/oss-cad-suite-build](https://github.com/YosysHQ/oss-cad-suite-build)

The guide will use Ubuntu Linux for a command reference.

---

Grab the [latest](https://github.com/YosysHQ/oss-cad-suite-build/releases/latest) build for your platform, extract them somewhere on your PC, and add the `oss-cad-suite/bin` folder to your path:

```
$ tar -xvf oss-cad-suite-linux-x64-[version].tgz
$ export PATH=$(pwd)/oss-cad-suite/bin:$PATH
```

```
 - MacOS:              export PATH=[path-to-bin]:$PATH
 - Linux:              export PATH=[path-to-bin]:$PATH
 - Windows Powershell: $ENV:PATH = "[path-to-bin];" + $ENV:PATH
 - Windows cmd.exe:    PATH=[path-to-bin];%PATH%
```

Check that they've been correctly installed by running:

```
$ yosys -V
Yosys 0.32+63 (git sha1 de54cf1a0, clang 10.0.0-4ubuntu1 -fPIC -Os)$ nextpnr-ecp5 -V
"nextpnr-ecp5" -- Next Generation Place and Route (Version nextpnr-0.6-46-ge08471df)
```

{{< hint warning >}}
The above steps only set the PATH variable for the current terminal session. Depending on your platform there are options to ensure the tools are kept in your path. 
{{< /hint >}}

---

On linux based systems you may also need to add a udev rule to enable user access to the usb device, once added you'll need to reload the rules or un-plug and reconnect the OrangeCrab for it to take effect
```
$ echo "ATTRS{idVendor}==\"1209\", ATTRS{idProduct}==\"5af0\", MODE=\"0666\", GROUP=\"plugdev\", TAG+=\"uaccess\"" | sudo tee /etc/udev/rules.d/99-orangecrab.rules
$ sudo udevadm trigger
```

You can check the connection and permissions using `dfu-util`

```
$ dfu-util --list
dfu-util 0.11-dev

Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
Copyright 2010-2021 Tormod Volden and Stefan Schmidt
This program is Free Software and has ABSOLUTELY NO WARRANTY
Please report bugs to http://sourceforge.net/p/dfu-util/tickets/

Found DFU: [1209:5af0] ver=0101, devnum=53, cfg=1, intf=0, path="1-1", alt=0, name="0x00080000 Bitstream", serial="UNKNOWN"
Found DFU: [1209:5af0] ver=0101, devnum=53, cfg=1, intf=0, path="1-1", alt=1, name="0x00100000 RISC-V Firmware", serial="UNKNOWN"
```

## Build Verilog Example
---
Download the [example](https://github.com/orangecrab-fpga/orangecrab-examples) repository. We'll build the verilog/blink example to test that everything is working.

```
$ git clone https://github.com/orangecrab-fpga/orangecrab-examples
$ cd OrangeCrab-examples/verilog/blink
$ make

    ... snip ...

Info: [ 81336,  81410) |* 
Info: [ 81410,  81484) | 
Info: [ 81484,  81558) | 
Info: [ 81558,  81632) |* 
ecppack --compress --freq 38.8 --input blink_out.config --bit blink.bit
cp blink.bit blink.dfu
dfu-suffix -v 1209 -p 5af0 -a blink.dfu
dfu-suffix (dfu-util) 0.11

Copyright 2011-2012 Stefan Schmidt, 2013-2014 Tormod Volden
This program is Free Software and has ABSOLUTELY NO WARRANTY
Please report bugs to http://sourceforge.net/p/dfu-util/tickets/

Suffix successfully added to file
```

{{< hint info >}}
If you have an OrangeCrab with a ECP5-85F installed then add the DENSITY flag when making

```bash
$ make DENSITY=85F
```
{{< /hint >}}

**🥳 Congratulations you've successfully compiled gateware for the ECP5 on the orangecrab!**


## Upload Verilog Example
---

Next, while holding the button on the OrangeCrab, plug it in. This enters the bootloader and enables you to upload new gateware. 
The LED should be smoothly fading through different colours.

```
$ make dfu
dfu-util -D blink.dfu
dfu-util 0.11

Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
Copyright 2010-2016 Tormod Volden and Stefan Schmidt
This program is Free Software and has ABSOLUTELY NO WARRANTY
Please report bugs to http://sourceforge.net/p/dfu-util/tickets/

Match vendor ID from file: 1209
Match product ID from file: 5af0
Opening DFU capable USB device...
ID 1209:5af0
Run-time device DFU version 0101
Claiming USB DFU Interface...
Setting Alternate Setting #0 ...
Determining device status: state = dfuIDLE, status = 0
dfuIDLE, continuing
DFU mode device DFU version 0101
Device returned transfer size 4096
Copying data from PC to DFU device
Download	[=========================] 100%        99314 bytes
Download done.
state(7) = dfuMANIFEST, status(0) = No error condition is present
state(8) = dfuMANIFEST-WAIT-RESET, status(0) = No error condition is present
Done!
```

You should now see the LED blinking through colours!

**🥳 Congratulations you've successfully loaded this gateware onto the ECP5 on the OrangeCrab!**
