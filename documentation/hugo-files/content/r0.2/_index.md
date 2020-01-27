---
title: Introduction
type: docs
rev: r0.2
---

# Introduction

The OrangeCrab is an FPGA development board based around the Lattice ECP5 FPGA. The OrangeCrab features a direct USB connection to the FPGA and comes loaded with a DFU bootloader so you can get started without the need of an external programmer.

The OrangeCrab makes use of the logic inside the ECP5 to support DDR3L memory. In it's minimal configuration this adds 128Mbytes of memory to the FPGA. Example gateware is provided that creates a System-On-Chip inside the FPGA with this RAM memory mapped.

## Technical details

Here are the main details for the OrangeCrab

* Lattice ECP5 25/45/85 variants (5G supported, but no SERDES routed)
* DDR3L Memory upto 8Gbit (512Mbit x16)
* Micro USB connection
* Full-speed (12Mbit) USB direct connection to FPGA
* 20 I/O pins (6 analog capable)
* Battery charger, with charge indicator LED
* User Button 
* 128Mbit QSPI FLASH Memory (Bitstream + User storage)
* 4bit MicroSD socket
* 48MHz Oscillator (Used by USB system)
* ADC/DAC pins use an analog Mux + SAR controlled by FPGA

## Photos
![Front Photo](OrangeCrab_r0.2_front.jpeg "Front Photo")
![Back Photo](OrangeCrab_r0.2_back.jpeg "Back Photo")
