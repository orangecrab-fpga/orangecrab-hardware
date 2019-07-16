# Layout review checklist

## General

* [X] [Schematic review](schematic-checklist.md) complete and signed off, including pin swaps done during layout
* [X] Layout DRC 100% clean

## Decoupling

* [X] Decoupling caps as close to power pins as possible
* [X] Low inductance mounting used for decoupling (prefer ViP if available, otherwise "[]8" shaped side vias
   * No ViP available. Larger tracks used to help reduce inductance.

## DFM / yield enhancement

* [X] All design rules within manufacturer's capability
* [X] Minimize use of vias/traces that push fab limits
    * 0.15mm vias are un-avoidable. Design has been Checked by manufacturer
* [X] Controlled impedance specified in fab notes if applicable
    * Using values based on my suggested stackup and from ciPCB
* [-] Stackup verified with manufacturer and specified in fab notes
    * Still to be validated by Fab engineers.
* [X] Board finish specified in fab notes
* [X] If panelizing, add panel location indicators for identifying location-specific reflow issues
* [NA] (recommended) Layer number markers specified to ensure correct assembly
    * Lack of physical space :(
* [X] Fiducials present (on both sides of board) if targeting automated assembly
* [X] Fiducial pattern asymmetric to detect rotated or flipped boards
* [X] Soldermask/copper clearance on fiducials respected
* [X] Panelization specified if required
    * Fab has created panelisation

## Footprints

* [X] Confirm components are available in the selected package
* [X] Verify schematic symbol matches the selected package
* [X] Confirm pinout diagram is from top vs bottom of package
* [-] (recommended) PCB printed 1:1 on paper and checked against physical parts
    * TODO
* [X] 3D models obtained (if available) and checked against footprints
    * And rendered!
* [X] Soldermask apertures on all SMT lands and PTH pads

## Differential pairs
* [X] Routed differentially
* [X] Skew matched
* [-] Correct clearance to non-coupled nets
    * Tricky to do with space contraints. 

## High-speed signals

* [X] Sufficient clearance to potential aggressors
* [X] Length matched if required
* [X] Minimize crossing reference plane splits/slots or changing layers, use caps/stitching vias if unavoidable
* [NA] Confirm fab can do copper to edge of PCB for edge launch connectors
* [NA] Double-check pad width on connectors and add plane cutouts if needed to minimize impedance discontinuities

## Power
* [X] Minimal slots in planes from via antipads
* [X] Sufficient width for planes/traces for required current

## Sensitive analog
* [NA] Guard ring / EMI cages provided if needed
* [NA] Physically separated from high current SMPS or other noise sources
* [NA] Consider microphone effect on MLCCs if near strong sound sources

## Mechanical
* [X] LEDs, buttons, and other UI elements on outward-facing side of board
* [X] Keep-outs around PCB perimeter, card guides, panelization mouse-bites, etc respected
* [X] Stress-sensitive components (MLCC) sufficiently clear from V-score or mouse bite locations, and oriented to reduce bending stress
* [NA] Clearance around large ICs for heatsinks/fans if required
* [X] Clearance around pluggable connectors for mating cable/connector
* [X] Clearance around mounting holes for screws
* [NA] Plane keepouts and clearance provided for shielded connectors, magnetics, etc
* [X] Confirm PCB dimensions and mounting hole size/placement against enclosure or card rack design
* [X] Verify mounting hole connection/isolation
* [X] Components not physically overlapping/colliding
* [NA] Clearance provided around solder-in test points for probe tips

## Thermal

* [X] Thermal reliefs used for plane connections (unless via is used for heatsinking)
* [X] Solid connections used to planes if heatsinking
* [X] Ensure thermal balance on SMT chip components to minimize risk of tombstoning

## Solder paste

* [X] No uncapped vias in pads (except low-power QFNs where some voiding is acceptable)
* [ ] QFN paste prints segmented
* [ ] Small pads 100% size, larger pads reduced to avoid excessive solder volume

## Solder mask

* [X] Confirm SMD vs NSMD pad geometry
* [X] Adequate clearance around pads (typ. 50 um)

## Silkscreen

* [X] Text size within fab limits
* [X] Text not overlapping drills or component pads
* [X] Text removed entirely in, or moved outside of, high component/via density areas
* [X] Traceability markings (rev, date, name, etc) provided
* [NA] Silkscreen box provided for writing/sticking serial number
* [X] Text mirrored properly on bottom layer

## Flex specific
* [NA] Components oriented to reduce bending forces
* [ ] Teardrops on all wire-to-pad connections

## CAM production
* [ ] KiCAD specific: rerun DRC and zone fills before exporting CAM files to ensure proper results
* [ ] Export gerber/drill files at the same time to ensure consistency
* [ ] Visually verify final CAM files to ensure no obvious misalignments
