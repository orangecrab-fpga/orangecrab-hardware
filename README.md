# OrangeCrab

## ECP5 FPGA Feather development board.
![Front Photo](documentation/images/OrangeCrab_r0.2_front.jpeg "Front Photo")

## Latest Revision: 
* [OrangeCrab r0.2](hardware/orangecrab_r0.2/)

Previous Revisions:
* [OrangeCrab r0.1](hardware/orangecrab_r0.1/)

---

## What is it?
There aren't many OSHW ECP5 boards available. Given that this FPGA is fully supported by an open source toolchain I decided to create one. In order to make use of the DDR3L support the ECP5 has, I've added some DDR3L memory. The board matches the feather format

## Hardware Overview
* Lattice ECP5-25F FPGA in csfBGA285 package
    * 24 K - Look Up Tables
    * 1008 Kb - Embedded Block RAM
    * 194 Kb - Distributed RAM
    * 28 - 18x18 Multipliers
    * PLLs: 2
    * Internal oscillator
    * Flexible I/O for DDR3 Memory Support
* DDR3L Memory
    * 128 Mbytes (1Gbit)
    * 64M x16
    * 1.35V low voltage operation
* Micro USB connection
    * Full-speed (12Mbit) USB with direct connection to FPGA
* Non-volatile Storage
    * 128Mbit QSPI FLASH Memory 
        * Bootloader (First 4Mbits)
        * User Bitstream
        * User storage (Firmware/MSC backend/etc)
        * QSPI compatible
    * MicroSD socket
        * 4bit SD interface (CK, CMD, DAT0-3)
* Power supply
    * High effeciency DCDC for main supplies
    * Battery charger (100mA), with charge indicator LED
    * LiPo battery connector (PH type)
* 48MHz onboard oscillator
* Standard 0.05" JTAG connector
* User I/O
    * 1x Button 
    * 1x RGB LED
    * 20x I/O on 0.1" headers
* Analog System
    * Analog Mux
    * SAR ADC, external RC / input comparator of FPGA
    * Digital bypass
    * Internal channels for supply monitor
    * Battery voltage sensing
* Feather Format Board
    * Dimensions: 22.86mm x 50.8mm (0.9" x 2.0")

---

![Back Photo](documentation/images/OrangeCrab_r0.2_back.jpeg "Back Photo")

## Licence

 * Hardware in this repository is licenced under CERN OHL v1.2
 * Gateware/Software/Firmware in this repository is licenced under MIT unless otherise indicated

 ## OSHW
This board is an OSHWA approved design: [AU000006](https://certification.oshwa.org/au000006.html)