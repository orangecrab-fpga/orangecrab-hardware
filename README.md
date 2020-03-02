# OrangeCrab

![Front Photo](documentation/images/OrangeCrab_r0.2_front.jpeg "Front Photo")

## ECP5 DDR3 memory in a Feather form-factor.

	Hardware r0.2 is still in the testing stages.
    Hardware r0.1 is functional with some small errata

## What is it
Project goal: "Make a simple ECP5 breakout board with DDR3L memory". As that was the only design goal I also decide it might be nice to keep the overal size small and make it an adafruit feather compatible dev board.


## Hardware r0.2
* Lattice ECP5 25/45/85 variants (5G supported, but no SERDES routed)
* DDR3L Memory upto 8Gbit (512Mbit x16)
* Micro USB connection
* Full-speed (12Mbit) USB direct connection to FPGA
* Battery charger, with charge indicator LED
* User Button 
* 128Mbit QSPI FLASH Memory (Bitstream + User storage)
* 4bit MicroSD socket
* 48MHz Oscillator (Used by USB system)
* ADC/DAC pins use an analog Mux + SAR controlled by FPGA



![Back Photo](documentation/images/OrangeCrab_r0.2_back.jpeg "Back Photo")

## Licence

 * Hardware in this repository is licenced under CERN OHL v1.2
 * Gateware/Software/Firmware in this repository is licenced under MIT unless otherise indicated