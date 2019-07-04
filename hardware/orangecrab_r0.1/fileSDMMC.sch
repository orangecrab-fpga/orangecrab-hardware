EESchema Schematic File Version 4
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 4 6
Title "Orange Crab"
Date "2019-06-28"
Rev "r0.1"
Comp "GsD"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text GLabel 5450 3950 0    60   Input ~ 0
SD_DAT0
Text GLabel 5450 4050 0    60   Input ~ 0
SD_DAT1
Text GLabel 5450 3350 0    60   Input ~ 0
SD_DAT2
Text GLabel 5450 3450 0    60   Input ~ 0
SD_DAT3
Text GLabel 5450 3550 0    60   Input ~ 0
SD_CMD
Text GLabel 5450 3750 0    60   Input ~ 0
SD_CK
Text GLabel 5450 4350 0    60   Input ~ 0
SD_CD
$Comp
L gkl_power:+3V3 #PWR049
U 1 1 5AC0A2E2
P 4900 3150
F 0 "#PWR049" H 4900 3000 50  0001 C CNN
F 1 "+3V3" H 4903 3301 50  0000 C CNN
F 2 "" H 4900 3150 50  0001 C CNN
F 3 "" H 4900 3150 50  0001 C CNN
	1    4900 3150
	1    0    0    -1  
$EndComp
$Comp
L gkl_power:GND #PWR050
U 1 1 5AC0A2FD
P 4900 4550
F 0 "#PWR050" H 4900 4300 50  0001 C CNN
F 1 "GND" H 4903 4424 50  0000 C CNN
F 2 "" H 4800 4200 50  0001 C CNN
F 3 "" H 4900 4550 50  0001 C CNN
	1    4900 4550
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x11_Male J4
U 1 1 5AC0A68B
P 5650 3850
F 0 "J4" H 5450 4600 50  0000 C CNN
F 1 "MicroSD" H 5400 4500 50  0000 C CNN
F 2 "bosonFrameGrabber:1040310811" H 5650 3850 50  0001 C CNN
F 3 "~" H 5650 3850 50  0001 C CNN
F 4 " WM6357CT-ND" H 5650 3850 60  0001 C CNN "SN-DK"
F 5 "1040310811" H 0   0   50  0001 C CNN "PN"
	1    5650 3850
	-1   0    0    -1  
$EndComp
Wire Wire Line
	4900 3850 4900 4150
Wire Wire Line
	4900 4150 5450 4150
Text Notes 5700 4400 0    63   ~ 0
DAT2\nDAT3/CD\nCMD\nVDD\nCLK\nVSS\nDAT0\nDAT1\nGND\nCD_0\nCD_1\n
Wire Notes Line
	5600 3250 5600 4450
Wire Notes Line
	5600 4450 6400 4450
Wire Notes Line
	6400 4450 6400 4350
Wire Notes Line
	6400 4350 6200 4350
Wire Notes Line
	6200 4350 6200 3350
Wire Notes Line
	6200 3350 6400 3350
Wire Notes Line
	6400 3350 6400 3250
Wire Notes Line
	6400 3250 5600 3250
Wire Wire Line
	5450 3650 4900 3650
Wire Wire Line
	4900 3650 4900 3150
Wire Wire Line
	5450 3850 4900 3850
Connection ~ 4900 4150
Wire Wire Line
	4900 4150 4900 4250
Wire Wire Line
	5450 4250 4900 4250
Connection ~ 4900 4250
Wire Wire Line
	4900 4250 4900 4550
$EndSCHEMATC
