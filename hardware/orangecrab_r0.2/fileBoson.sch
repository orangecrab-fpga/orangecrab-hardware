EESchema Schematic File Version 4
LIBS:bosonFrameGrabber-cache
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 4 6
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L bosonFrameGrabber:Boson U5
U 1 1 5ABA25B0
P 2100 3650
F 0 "U5" H 2204 5242 60  0000 C CNN
F 1 "Boson" H 2204 5136 60  0000 C CNN
F 2 "" H 2100 4900 60  0001 C CNN
F 3 "" H 2100 4900 60  0001 C CNN
F 4 "H11919CT-ND" H 0   0   50  0001 C CNN "SN-DK"
F 5 "DF40HC(4.0)-80DS-0.4V(51)" H 0   0   50  0001 C CNN "PN"
	1    2100 3650
	1    0    0    -1  
$EndComp
$Comp
L bosonFrameGrabber:Boson U5
U 2 1 5ABA25E7
P 5200 3250
F 0 "U5" H 5304 4842 60  0000 C CNN
F 1 "Boson" H 5304 4736 60  0000 C CNN
F 2 "" H 5200 4500 60  0001 C CNN
F 3 "" H 5200 4500 60  0001 C CNN
F 4 "H11919CT-ND" H 0   0   50  0001 C CNN "SN-DK"
F 5 "DF40HC(4.0)-80DS-0.4V(51)" H 0   0   50  0001 C CNN "PN"
	2    5200 3250
	1    0    0    -1  
$EndComp
$Comp
L bosonFrameGrabber:Boson U5
U 3 1 5ABA262D
P 5050 6050
F 0 "U5" H 5179 7642 60  0000 C CNN
F 1 "Boson" H 5179 7536 60  0000 C CNN
F 2 "" H 5050 7300 60  0001 C CNN
F 3 "" H 5050 7300 60  0001 C CNN
F 4 "H11919CT-ND" H 0   0   50  0001 C CNN "SN-DK"
F 5 "DF40HC(4.0)-80DS-0.4V(51)" H 0   0   50  0001 C CNN "PN"
	3    5050 6050
	1    0    0    -1  
$EndComp
$Comp
L bosonFrameGrabber:Boson U5
U 4 1 5ABA2670
P 8550 5750
F 0 "U5" H 8429 7342 60  0000 C CNN
F 1 "Boson" H 8429 7236 60  0000 C CNN
F 2 "" H 8550 7000 60  0001 C CNN
F 3 "" H 8550 7000 60  0001 C CNN
F 4 "H11919CT-ND" H 0   0   50  0001 C CNN "SN-DK"
F 5 "DF40HC(4.0)-80DS-0.4V(51)" H 0   0   50  0001 C CNN "PN"
	4    8550 5750
	1    0    0    -1  
$EndComp
$Comp
L bosonFrameGrabber:Boson U5
U 5 1 5ABA269F
P 8450 2700
F 0 "U5" H 8479 4292 60  0000 C CNN
F 1 "Boson" H 8479 4186 60  0000 C CNN
F 2 "" H 8450 3950 60  0001 C CNN
F 3 "" H 8450 3950 60  0001 C CNN
F 4 "H11919CT-ND" H 0   0   50  0001 C CNN "SN-DK"
F 5 "DF40HC(4.0)-80DS-0.4V(51)" H 0   0   50  0001 C CNN "PN"
	5    8450 2700
	1    0    0    -1  
$EndComp
Text GLabel 9300 1400 2    60   Input ~ 0
BOSON_DATA0
Text GLabel 9300 1500 2    60   Input ~ 0
BOSON_DATA1
Text GLabel 9300 1600 2    60   Input ~ 0
BOSON_DATA2
Text GLabel 9300 1700 2    60   Input ~ 0
BOSON_DATA3
Text GLabel 9300 1800 2    60   Input ~ 0
BOSON_DATA4
Text GLabel 9300 1900 2    60   Input ~ 0
BOSON_DATA5
Text GLabel 9300 2000 2    60   Input ~ 0
BOSON_DATA6
Text GLabel 9300 2100 2    60   Input ~ 0
BOSON_DATA7
Text GLabel 9300 2200 2    60   Input ~ 0
BOSON_DATA8
Text GLabel 9300 2300 2    60   Input ~ 0
BOSON_DATA9
Text GLabel 9300 2400 2    60   Input ~ 0
BOSON_DATA10
Text GLabel 9300 2500 2    60   Input ~ 0
BOSON_DATA11
Text GLabel 9300 2600 2    60   Input ~ 0
BOSON_DATA12
Text GLabel 9300 2700 2    60   Input ~ 0
BOSON_DATA13
Text GLabel 9300 2800 2    60   Input ~ 0
BOSON_DATA14
Text GLabel 9300 2900 2    60   Input ~ 0
BOSON_DATA15
Text GLabel 9300 3100 2    60   Input ~ 0
BOSON_DATA_EN
Text GLabel 9300 3300 2    60   Input ~ 0
BOSON_CK
Text GLabel 9300 3400 2    60   Input ~ 0
BOSON_VSYNC
Text GLabel 9300 3500 2    60   Input ~ 0
BOSON_HSYNC
Text GLabel 9300 4450 2    60   Input ~ 0
BOSON_RXD
Text GLabel 9300 4550 2    60   Input ~ 0
BOSON_TXD
$Comp
L bosonFrameGrabber:GND #PWR042
U 1 1 5ABB36EF
P 2900 5350
F 0 "#PWR042" H 2900 5100 50  0001 C CNN
F 1 "GND" H 2903 5224 50  0000 C CNN
F 2 "" H 2800 5000 50  0001 C CNN
F 3 "" H 2900 5350 50  0001 C CNN
	1    2900 5350
	1    0    0    -1  
$EndComp
$Comp
L bosonFrameGrabber:+3V3 #PWR043
U 1 1 5ABB3714
P 2900 2250
F 0 "#PWR043" H 2900 2100 50  0001 C CNN
F 1 "+3V3" H 2903 2401 50  0000 C CNN
F 2 "" H 2900 2250 50  0001 C CNN
F 3 "" H 2900 2250 50  0001 C CNN
	1    2900 2250
	1    0    0    -1  
$EndComp
Wire Wire Line
	2750 3450 2900 3450
Wire Wire Line
	2900 3450 2900 5350
Wire Wire Line
	2750 5250 2900 5250
Connection ~ 2900 5250
Wire Wire Line
	2750 5150 2900 5150
Connection ~ 2900 5150
Wire Wire Line
	2750 5050 2900 5050
Connection ~ 2900 5050
Wire Wire Line
	2750 4950 2900 4950
Connection ~ 2900 4950
Wire Wire Line
	2750 4850 2900 4850
Connection ~ 2900 4850
Wire Wire Line
	2750 4750 2900 4750
Connection ~ 2900 4750
Wire Wire Line
	2750 4650 2900 4650
Connection ~ 2900 4650
Wire Wire Line
	2750 4550 2900 4550
Connection ~ 2900 4550
Wire Wire Line
	2750 4450 2900 4450
Connection ~ 2900 4450
Wire Wire Line
	2750 4350 2900 4350
Connection ~ 2900 4350
Wire Wire Line
	2750 4250 2900 4250
Connection ~ 2900 4250
Wire Wire Line
	2750 4150 2900 4150
Connection ~ 2900 4150
Wire Wire Line
	2750 4050 2900 4050
Connection ~ 2900 4050
Wire Wire Line
	2750 3950 2900 3950
Connection ~ 2900 3950
Wire Wire Line
	2750 3850 2900 3850
Connection ~ 2900 3850
Wire Wire Line
	2750 3750 2900 3750
Connection ~ 2900 3750
Wire Wire Line
	2750 3650 2900 3650
Connection ~ 2900 3650
Wire Wire Line
	2750 3550 2900 3550
Connection ~ 2900 3550
Wire Wire Line
	2750 2650 2900 2650
Wire Wire Line
	2900 2650 2900 2250
Wire Wire Line
	2750 2550 2900 2550
Connection ~ 2900 2550
Wire Wire Line
	2750 2450 2900 2450
Connection ~ 2900 2450
Wire Wire Line
	2750 2350 2900 2350
Connection ~ 2900 2350
Text GLabel 2750 2950 2    60   Input ~ 0
BOSON_RESET
Text GLabel 2750 3050 2    60   Input ~ 0
BOSON_EXTSYNC
$EndSCHEMATC
