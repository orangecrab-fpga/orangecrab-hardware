---
title: Overview
type: docs
rev: r0.2
---

# Overview

The OrangeCrab is a small pocket sized development board in the Adafruit feather format. While small in size it packs a punch! The standard version is equiped with a Lattice ECP5 FPGA, and DDR3L memory. Paired with the FPGA is a FLASH chip, with enough memory to store multiple bitstreams.

## FPGA
The FPGA used on the OrangeCrab is an ECP5 from Lattice Semiconductor. The ECP5 series is a medium tier, low power, low cost FPGA product line. This device supports various DDR3 memory interfaces, because of this the board features DDR3L memory. The ECP5 is also one of the platforms that is fully supported by the Open Source Synthesis flow.

## DDR3
There is DDR3L memory attached to the FPGA. The hardware is configured by default for DDR3L (1.35V). There are enough address lines wired to the memory to support upto 8Gbit parts. (Twin-die is not supported) The standard OrangeCrab configulation makes use of 1Gbit. This is connected to the FPGA using a 16-bit data bus. 

## USB
The micro usb connector is wired directly into the FPGA. Just as a microprocessor can emulate UART or SPI using standard I/O pins the FPGA can do the same for USB. By using some of the FPGA logic to create a USB core, we can use the I/O pins on the FPGA to act as a USB device. This will operate at USB 2.0 full-speed rates (12Mbit/s). Operating at High Speed rates (480Mbit/s) is not possible with the OrangeCrab hardware.
