---
title: Introduction
type: docs
rev: r0.2
---

![OrangeCrab Photo](docs/r0.2/orangeCrab-6.jpg "OrangeCrab Photo")

# Introduction

The OrangeCrab is a small pocket sized development board in the Adafruit feather format. While small in size it packs a punch! The standard version is equiped with a Lattice ECP5 FPGA, and DDR3L memory. Paired with the FPGA is a FLASH chip, with enough memory to store multiple bitstreams.

## FPGA
The FPGA used on the OrangeCrab is an ECP5 from Lattice Semiconductor. The ECP5 series is a medium tier, low power, low cost FPGA product line. This device supports various DDR3 memory interfaces, because of this the board features DDR3L memory. The ECP5 is also one of the platforms that is fully supported by the Open Source Synthesis flow.

## DDR3
There is DDR3L memory attached to the FPGA. The hardware is configured by default for DDR3L (1.35V). There are enough address lines wired to the memory to support upto 8Gbit parts. (Twin-die is not supported) The standard OrangeCrab configulation makes use of 1Gbit. This is connected to the FPGA using a 16-bit data bus. 

## USB
The micro usb connector is wired directly into the FPGA. Just as a microprocessor can emulate UART or SPI using standard I/O pins the FPGA can do the same for USB. By using some of the FPGA logic to create a USB core, we can use the I/O pins on the FPGA to act as a USB device. This will operate at USB 2.0 full-speed rates (12Mbit/s). Operating at High Speed rates (480Mbit/s) is not possible with the OrangeCrab hardware.

## Hardware Versions

There are currently 3 released version of the board:

{{< hint warning >}}
### [Hardware r0.1]({{< relref "/docs/r0.1.md" >}})
Status: Prototype only

        Standout Features:
        - 2MByte FLASH 2x3mm USON part
        - ATSAMD10/11 Co-processor planned mainly for the ADC/DAC (fw never written)
        - Expansion port on the bottom of the feather breaking out extra I/O differential pairs.
{{< /hint >}}

{{< hint warning >}}
### [Hardware r0.2]({{< relref "/docs/r0.2.md" >}})
Status: Superseded

        Changes from r0.1:
        - Added FPGA I/O based ADC
        - Add User Button and self-reset
        - Larger FLASH 2MBytes -> 16MBytes
{{< /hint >}}

{{< hint info >}}
### [Hardware r0.2.1]({{< relref "/docs/r0.2.1.md" >}})
Status: Currently produced design
        
        Changes from r0.2:
        - Changed USB micro-b to USB-C
        - Swapped DCDC devices
        - Added support for ECP5 85F-5G
        - Added Castellated I/O pins 
{{< /hint >}}