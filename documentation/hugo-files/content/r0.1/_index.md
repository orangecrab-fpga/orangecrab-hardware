---
title: Introduction
type: docs
rev: r0.1
---

# Introduction

The OrangeCrab is an FPGA development board based around the Lattice ECP5 FPGA. The OrangeCrab features a direct USB connection to the FPGA and comes loaded with a DFU bootloader so you can get started without the need of an external programmer.

The OrangeCrab makes use of the logic inside the ECP5 to support DDR3L memory. In it's minimal configuration this adds 128Mbytes of memory to the FPGA. Example gateware is provided that creates a System-On-Chip inside the FPGA with this RAM memory mapped.

## Technical details

Here are the main details for the OrangeCrab

* Lattice ECP5 25 (With limited support for 45/85 variants)
* DDR3L Memory upto 1Gbit (64Mbit x16)
* Micro USB connection
* Full-speed (12Mbit) USB direct connection to FPGA
* Battery charger, with charge indicator LED
* Reset Button 
* 16Mbit QSPI FLASH Memory (Bitstream + User storage)
* 4bit MicroSD socket
* 48MHz Oscillator (Used by USB system)
* ATSAMD10/11 Co-processor planned mainly for the ADC/DAC
* Spare 3.3V I/O's broken out onto a 30pin low profile connector
  * 7 diff pairs
  * 1 single ended only

## Photos
![Front Photo](OrangeCrab_r0.1_front.jpeg "Front Photo")
![Back Photo](OrangeCrab_r0.1_back.jpeg "Back Photo")
