EESchema Schematic File Version 4
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 6 6
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text Notes 1800 1700 0    50   ~ 0
Battery Input
Text Notes 4650 1700 0    50   ~ 0
Battery Charger
Text Notes 1850 2900 0    50   ~ 0
USB input
$Comp
L Connector:USB_B_Micro J?
U 1 1 5D173F1E
P 1750 3500
F 0 "J?" H 1807 3967 50  0000 C CNN
F 1 "USB_B_Micro" H 1807 3876 50  0000 C CNN
F 2 "" H 1900 3450 50  0001 C CNN
F 3 "~" H 1900 3450 50  0001 C CNN
	1    1750 3500
	1    0    0    -1  
$EndComp
$Comp
L gkl_pmic:BQ24230 U?
U 1 1 5D174B89
P 5000 2650
F 0 "U?" H 4975 3469 50  0000 C CNN
F 1 "BQ24230" H 4975 3378 50  0000 C CNN
F 2 "" H 5050 3400 50  0001 C CNN
F 3 "" H 5050 3400 50  0001 C CNN
F 4 "BQ24232RGTR" H 5000 2650 50  0001 C CNN "PN"
F 5 "Texas Instruments" H 5000 2650 50  0001 C CNN "Mfg"
	1    5000 2650
	1    0    0    -1  
$EndComp
$Comp
L gkl_pmic:FAN53601 U?
U 1 1 5D17570A
P 7650 2050
F 0 "U?" H 7650 2419 50  0000 C CNN
F 1 "FAN53601" H 7650 2328 50  0000 C CNN
F 2 "" H 7650 2350 50  0001 C CNN
F 3 "" H 7650 2350 50  0001 C CNN
	1    7650 2050
	1    0    0    -1  
$EndComp
Text Notes 8000 1800 0    50   ~ 0
1.1V @ 1A
$Comp
L gkl_pmic:FAN53601 U?
U 1 1 5D178438
P 7650 2950
F 0 "U?" H 7650 3319 50  0000 C CNN
F 1 "FAN53601" H 7650 3228 50  0000 C CNN
F 2 "" H 7650 3250 50  0001 C CNN
F 3 "" H 7650 3250 50  0001 C CNN
	1    7650 2950
	1    0    0    -1  
$EndComp
Text Notes 8000 2700 0    50   ~ 0
1.35V @ 1A
$Comp
L Connector:Conn_01x02_Male J?
U 1 1 5D179AC3
P 2000 2100
F 0 "J?" H 2108 2281 50  0000 C CNN
F 1 "Conn_01x02_Male" H 2108 2190 50  0000 C CNN
F 2 "" H 2000 2100 50  0001 C CNN
F 3 "~" H 2000 2100 50  0001 C CNN
	1    2000 2100
	1    0    0    -1  
$EndComp
$EndSCHEMATC
