EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 7
Title "Orange Crab"
Date "2020-11-01"
Rev "r0.2.1"
Comp "Good Stuff Department"
Comment1 ""
Comment2 ""
Comment3 "Licensed under CERN OHL v.1.2"
Comment4 "Designed by: Greg Davill"
$EndDescr
$Sheet
S 4050 2900 1800 900 
U 5AB8ACB7
F0 "FPGA" 60
F1 "FPGA.sch" 60
$EndSheet
$Sheet
S 4050 4200 1800 1000
U 5ABD38F2
F0 "DRAM" 60
F1 "DRAM.sch" 60
$EndSheet
$Sheet
S 1800 4200 1800 1000
U 5AC0A2A0
F0 "SDMMC" 60
F1 "SDMMC.sch" 60
$EndSheet
$Sheet
S 6300 2900 1900 900 
U 5ABC9A87
F0 "IO" 60
F1 "IO.sch" 60
$EndSheet
$Sheet
S 1800 2900 1900 900 
U 5D1738DB
F0 "POWER" 60
F1 "POWER.sch" 60
$EndSheet
$Comp
L Mechanical:MountingHole H4
U 1 1 5D2429C7
P 11050 6400
F 0 "H4" H 11150 6400 50  0001 L CNN
F 1 "MountingHole" H 11150 6355 50  0001 L CNN
F 2 "MountingHole:MountingHole_2.1mm" H 11050 6400 50  0001 C CNN
F 3 "~" H 11050 6400 50  0001 C CNN
F 4 "DNP" H 11050 6400 50  0001 C CNN "PN"
	1    11050 6400
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H3
U 1 1 5D24316A
P 10850 6400
F 0 "H3" H 10950 6400 50  0001 L CNN
F 1 "MountingHole" H 10950 6355 50  0001 L CNN
F 2 "MountingHole:MountingHole_2.1mm" H 10850 6400 50  0001 C CNN
F 3 "~" H 10850 6400 50  0001 C CNN
F 4 "DNP" H 10850 6400 50  0001 C CNN "PN"
	1    10850 6400
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H2
U 1 1 5D243527
P 10650 6400
F 0 "H2" H 10750 6400 50  0001 L CNN
F 1 "MountingHole" H 10750 6355 50  0001 L CNN
F 2 "MountingHole:MountingHole_2.2mm_M2_Pad" H 10650 6400 50  0001 C CNN
F 3 "~" H 10650 6400 50  0001 C CNN
F 4 "DNP" H 10650 6400 50  0001 C CNN "PN"
	1    10650 6400
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H1
U 1 1 5D243531
P 10450 6400
F 0 "H1" H 10550 6400 50  0001 L CNN
F 1 "MountingHole" H 10550 6355 50  0001 L CNN
F 2 "MountingHole:MountingHole_2.2mm_M2_Pad" H 10450 6400 50  0001 C CNN
F 3 "~" H 10450 6400 50  0001 C CNN
F 4 "DNP" H 10450 6400 50  0001 C CNN "PN"
	1    10450 6400
	1    0    0    -1  
$EndComp
$Sheet
S 6300 4200 1900 1000
U 5D35D1F5
F0 "DECOUPLING" 50
F1 "DECOUPLING.sch" 50
$EndSheet
$Comp
L Mechanical:Fiducial FID1
U 1 1 5EA1EE5B
P 10450 6650
F 0 "FID1" H 10535 6696 50  0001 L CNN
F 1 "Fiducial" H 10535 6605 50  0001 L CNN
F 2 "Fiducial:Fiducial_0.75mm_Mask1.5mm" H 10450 6650 50  0001 C CNN
F 3 "~" H 10450 6650 50  0001 C CNN
F 4 "DNP" H 10450 6650 50  0001 C CNN "PN"
	1    10450 6650
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:Fiducial FID2
U 1 1 5EA1F2D2
P 10600 6650
F 0 "FID2" H 10685 6696 50  0001 L CNN
F 1 "Fiducial" H 10685 6605 50  0001 L CNN
F 2 "Fiducial:Fiducial_0.75mm_Mask1.5mm" H 10600 6650 50  0001 C CNN
F 3 "~" H 10600 6650 50  0001 C CNN
F 4 "DNP" H 10600 6650 50  0001 C CNN "PN"
	1    10600 6650
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:Fiducial FID4
U 1 1 5EA1F5F9
P 10450 6800
F 0 "FID4" H 10535 6846 50  0001 L CNN
F 1 "Fiducial" H 10535 6755 50  0001 L CNN
F 2 "Fiducial:Fiducial_0.75mm_Mask1.5mm" H 10450 6800 50  0001 C CNN
F 3 "~" H 10450 6800 50  0001 C CNN
F 4 "DNP" H 10450 6800 50  0001 C CNN "PN"
	1    10450 6800
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:Fiducial FID5
U 1 1 5EA1F603
P 10600 6800
F 0 "FID5" H 10685 6846 50  0001 L CNN
F 1 "Fiducial" H 10685 6755 50  0001 L CNN
F 2 "Fiducial:Fiducial_0.75mm_Mask1.5mm" H 10600 6800 50  0001 C CNN
F 3 "~" H 10600 6800 50  0001 C CNN
F 4 "DNP" H 10600 6800 50  0001 C CNN "PN"
	1    10600 6800
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:Fiducial FID3
U 1 1 5EA1FF05
P 10750 6650
F 0 "FID3" H 10835 6696 50  0001 L CNN
F 1 "Fiducial" H 10835 6605 50  0001 L CNN
F 2 "Fiducial:Fiducial_0.75mm_Mask1.5mm" H 10750 6650 50  0001 C CNN
F 3 "~" H 10750 6650 50  0001 C CNN
F 4 "DNP" H 10750 6650 50  0001 C CNN "PN"
	1    10750 6650
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:Fiducial FID6
U 1 1 5EA1FF0F
P 10750 6800
F 0 "FID6" H 10835 6846 50  0001 L CNN
F 1 "Fiducial" H 10835 6755 50  0001 L CNN
F 2 "Fiducial:Fiducial_0.75mm_Mask1.5mm" H 10750 6800 50  0001 C CNN
F 3 "~" H 10750 6800 50  0001 C CNN
F 4 "DNP" H 10750 6800 50  0001 C CNN "PN"
	1    10750 6800
	1    0    0    -1  
$EndComp
$EndSCHEMATC
