# Schematic review checklist

## General

- [ ] CAD ERC 100% clean. If some errors are invalid due to toolchain quirks, each exception must be inspected and signed off as invalid.
- [ ] Verify pin numbers of all schematic symbols against datasheet (if not yet board proven).
- [ ] Schematic symbol matches chosen component package
- [ ] Thermal pads are connected to correct power rail (may not always be ground)
- [x] Debug interfaces are not power gated in sleep mode

## Passive components
* [ ] Power/voltage/tolerance ratings specified as required
* [X] Ceramic capacitors appropriately de-rated for C/V curve
* [X] Polarized components specified in schematic if using electrolytic caps etc

## Power supply

### System power input

* [NA] Fusing and/or reverse voltage protection at system power inlet
* [x] Check total input capacitance and add inrush limiter if needed

### Regulators

* [NA] Under/overvoltage protection configured correctly if used
* [X] Verify estimated power usage per rail against regulator rating
* [NA] Current-sense resistors on power rails after regulator output caps, not in switching loop
 * To reduce BOM this have been omitted, will cut traces during board bringup to validate power supplies.
* [NA] Remote sense used on low voltage or high current rails
* [ ] Linear regulators are stable with selected output cap ESR
* [ ] Confirm power rail sequencing against device datasheets

### Decoupling
* [ ] Decoupling present for all ICs
* [ ] Decoupling meets/exceeds vendor recommendations if specified
* [ ] Bulk decoupling present at PSU

### General
* [ ] All power inputs fed by correct voltage
* [ ] Check high-power discrete semiconductors and passives to confirm they can handle expected load
* [ ] Analog rails filtered/isolated from digital circuitry as needed

## Signals

### Digital

* [ ] Signals are correct logic level for input pin
* [ ] Pullups on all open-drain outputs
* [ ] Pulldowns on all PECL outputs
* [ ] Termination on all high-speed signals
* [ ] AC coupling caps on gigabit transceivers
* [ ] TX/RX paired correctly for UART, SPI, MGT, etc
* [ ] Differential pair polarity / pairing correct
* [ ] Active high/low enable signal polarity correct
* [ ] I/O banking rules met on FPGAs etc

### Analog

* [NA] RC time constant for attenuators sane given ADC sampling frequency
* [NA] Verify frequency response of RF components across entire operating range. Don't assume a "1-100 MHz" amplifier has the same gain across the whole range.

### Clocks

* [X] All oscillators meet required jitter / frequency tolerance. Be extra cautious with MEMS oscillators as these tend to have higher jitter.
* [NA] Correct load caps provided for discrete crystals
* [X] Crystals only used if IC has an integrated crystal driver
* [X] Banking / clock capable input rules met for clocks going to FPGAs

### Strap/init pins
* [ ] Pullup/pulldowns on all signals that need defined state at boot
* [X] Strap pins connected to correct rail for desired state
* [x] JTAG/ICSP connector provided for all programmable devices
    * GsD: SAMD has test pads exposed via test-points
* [x] Config/boot flash provided for all FPGAs or MPUs without internal flash
* [NA] Reference resistors correct value and reference rail

### External interface protection

* [NA] Power outputs (USB etc) current limited
* [NA] ESD protection on data lines going off board

### Debugging / reworkability

* [NA] Use 0-ohm resistors vs direct hard-wiring for strap pins when possible
* [ ] Provide multiple ground clips/points for scope probes
* [x] Dedicated ground in close proximity to analog test points
* [ ] Test points on all power rails
* [ ] Test points on interesting signals which may need probing for bringup/debug
 * Added bottom test points to JTAG
 * DDR3 has termination on all Address lines, Upper byte traces are accesible on back layer.
 * Added USB Test pads

## Thermal

* [X] Power estimates for all large / high power ICs
    * ECP5 (@ 20% utilisation) 1/4W
* [NA] Thermal calculations for all large / high power ICs
* [NA] Specify heatsinks as needed

