# OrangeCrab DDR3 test code

``` Currently under-development ``` 

## Build Instructins
```console
$ python3 OrangeCrab-bitstream.py ddr3_test
 ```

This will invoke Litex/Migen to compile bios and generate bitstream for the ECP5.
When the synthesis is complet you will be left with "build/gateware/top.svf"

## Loading
Run this command to invoke openOCD and load the bitstream onto the FPGA via a JTAG adapter
 ```console
$ python3 load_fpga.py 
 ```




## Running DDR3 Tests

The Litex DDR3 test code is run by connecting a serial link to the OrangeCrab on External Pins 0/1


In a new terminal run the litex_server
```console
$ litex_server --uart --uart-port [PORT] --uart-baudrate 115200
```

Then back in your original terminal you can run the python files that interact with the hardware via the litex_server

This will connect to the board and return the Bitstream ID String
```console
$ python3 test_identifier.py
  fpga_id: Versa ECP5 test SoC 2019-11-29 11:45:32
```

If you do not see a valid 'fpga_id' here then likely your serial setup is incorrect.



Connects to the wishbone bus in the FPGA and performs memory operations in the address space mapped to the DDR3 memory.
```console
$ python3 test_sdram.py
```

On my setup this returns the following:
```console
Release reset
Bring CKE high
Load Mode Register 2, CWL=5
Load Mode Register 3
Load Mode Register 1
Load Mode Register 0, CL=6, BL=8
ZQ Calibration
Read leveling...
delay: 0 |dq0: 0b00001010, 
dq1: 0b00001010, 
dq2: 0b00001010, 
dq3: 0b00001010, 
dq4: 0b00001010, 
dq5: 0b00001010, 
dq6: 0b00001010, 
dq7: 0b00001010, 
dq8: 0b00000000, 
dq9: 0b00000000, 
dq10: 0b00000000, 
dq11: 0b00000000, 
dq12: 0b00000000, 
dq13: 0b00000000, 
dq14: 0b00000000, 
dq15: 0b00000000, 
delay: 1 |dq0: 0b00001010, 
dq1: 0b00001010, 
dq2: 0b00001010, 
dq3: 0b00001010, 
dq4: 0b00001010, 
dq5: 0b00001010, 
dq6: 0b00001010, 
dq7: 0b00001010, 
dq8: 0b00000010, 
dq9: 0b00000010, 
dq10: 0b00000010, 
dq11: 0b00000010, 
dq12: 0b00000010, 
dq13: 0b00000010, 
dq14: 0b00000010, 
dq15: 0b00000010, 
delay: 2 |dq0: 0b00001010, 
dq1: 0b00001010, 
dq2: 0b00001010, 
dq3: 0b00001010, 
dq4: 0b00001010, 
dq5: 0b00001010, 
dq6: 0b00001010, 
dq7: 0b00001010, 
dq8: 0b00001010, 
dq9: 0b00001010, 
dq10: 0b00001010, 
dq11: 0b00001010, 
dq12: 0b00001010, 
dq13: 0b00001010, 
dq14: 0b00001010, 
dq15: 0b00001010, 
delay: 3 |dq0: 0b00000010, 
dq1: 0b00000010, 
dq2: 0b00000010, 
dq3: 0b00000010, 
dq4: 0b00000010, 
dq5: 0b00000010, 
dq6: 0b00000010, 
dq7: 0b00000010, 
dq8: 0b00000010, 
dq9: 0b00000010, 
dq10: 0b00000010, 
dq11: 0b00000010, 
dq12: 0b00000010, 
dq13: 0b00000010, 
dq14: 0b00000010, 
dq15: 0b00000010, 
delay: 4 |dq0: 0b00000010, 
dq1: 0b00000010, 
dq2: 0b00000010, 
dq3: 0b00000010, 
dq4: 0b00000010, 
dq5: 0b00000010, 
dq6: 0b00000010, 
dq7: 0b00000010, 
dq8: 0b00000010, 
dq9: 0b00000010, 
dq10: 0b00000010, 
dq11: 0b00000010, 
dq12: 0b00000010, 
dq13: 0b00000010, 
dq14: 0b00000010, 
dq15: 0b00000010, 
delay: 5 |dq0: 0b00000010, 
dq1: 0b00000010, 
dq2: 0b00000010, 
dq3: 0b00000010, 
dq4: 0b00000010, 
dq5: 0b00000010, 
dq6: 0b00000010, 
dq7: 0b00000010, 
dq8: 0b00000010, 
dq9: 0b00000010, 
dq10: 0b00000010, 
dq11: 0b00000010, 
dq12: 0b00000010, 
dq13: 0b00000010, 
dq14: 0b00000010, 
dq15: 0b00000010, 
delay: 6 |dq0: 0b00001010, 
dq1: 0b00001010, 
dq2: 0b00001010, 
dq3: 0b00001010, 
dq4: 0b00001010, 
dq5: 0b00001010, 
dq6: 0b00001010, 
dq7: 0b00001010, 
dq8: 0b00001010, 
dq9: 0b00001010, 
dq10: 0b00001010, 
dq11: 0b00001010, 
dq12: 0b00001010, 
dq13: 0b00001010, 
dq14: 0b00001010, 
dq15: 0b00001010, 
delay: 7 |dq0: 0b00001010, 
dq1: 0b00001010, 
dq2: 0b00001010, 
dq3: 0b00001010, 
dq4: 0b00001010, 
dq5: 0b00001010, 
dq6: 0b00001010, 
dq7: 0b00001010, 
dq8: 0b00001010, 
dq9: 0b00001010, 
dq10: 0b00001010, 
dq11: 0b00001010, 
dq12: 0b00001010, 
dq13: 0b00001010, 
dq14: 0b00001010, 
dq15: 0b00001010, 
0: 0x3c6ef35f, 0x3c6ef35f OK
1: 0x3c88596c, 0x3c88596c OK
2: 0x3ca1bf79, 0x3ca1bf79 OK
3: 0x3cbb2586, 0x3cbb2586 OK
4: 0x3cd48b93, 0x3cd48b93 OK
5: 0x3cedf1a0, 0x3cedf1a0 OK
6: 0x3d0757ad, 0x3d0757ad OK
7: 0x3d20bdba, 0x3d20bdba OK
8: 0x3d3a23c7, 0x3d3a23c7 OK
9: 0x3d5389d4, 0x3d5389d4 OK
10: 0x3d6cefe1, 0x3d6cefe1 OK
11: 0x3d8655ee, 0x3d8655ee OK
12: 0x3d9fbbfb, 0x3d9fbbfb OK
13: 0x3db92208, 0x3db92208 OK
14: 0x3dd28815, 0x3dd28815 OK
15: 0x3debee22, 0x3debee22 OK
16: 0x3e05542f, 0x3e05542f OK
17: 0x3e1eba3c, 0x3e1eba3c OK
18: 0x3e382049, 0x3e382049 OK
19: 0x3e518656, 0x3e518656 OK
20: 0x3e6aec63, 0x3e6aec63 OK
21: 0x3e845270, 0x3e845270 OK
22: 0x3e9db87d, 0x3e9db87d OK
23: 0x3eb71e8a, 0x3eb71e8a OK
24: 0x3ed08497, 0x3ed08497 OK
25: 0x3ee9eaa4, 0x3ee9eaa4 OK
26: 0x3f0350b1, 0x3f0350b1 OK
27: 0x3f1cb6be, 0x3f1cb6be OK
28: 0x3f361ccb, 0x3f361ccb OK
29: 0x3f4f82d8, 0x3f4f82d8 OK
30: 0x3f68e8e5, 0x3f68e8e5 OK
31: 0x3f824ef2, 0x3f824ef2 OK
32: 0x3f9bb4ff, 0x3f9bb4ff OK
33: 0x3fb51b0c, 0x3fb51b0c OK
34: 0x3fce8119, 0x3fce8119 OK
35: 0x3fe7e726, 0x3fe7e726 OK
36: 0x40014d33, 0x40014d33 OK
37: 0x401ab340, 0x401ab340 OK
38: 0x4034194d, 0x4034194d OK
39: 0x404d7f5a, 0x404d7f5a OK
40: 0x4066e567, 0x4066e567 OK
41: 0x40804b74, 0x40804b74 OK
42: 0x4099b181, 0x4099b181 OK
43: 0x40b3178e, 0x40b3178e OK
44: 0x40cc7d9b, 0x40cc7d9b OK
45: 0x40e5e3a8, 0x40e5e3a8 OK
46: 0x40ff49b5, 0x40ff49b5 OK
47: 0x4118afc2, 0x4118afc2 OK
48: 0x413215cf, 0x413215cf OK
49: 0x414b7bdc, 0x414b7bdc OK
50: 0x4164e1e9, 0x4164e1e9 OK
51: 0x417e47f6, 0x417e47f6 OK
52: 0x4197ae03, 0x4197ae03 OK
53: 0x41b11410, 0x41b11410 OK
54: 0x41ca7a1d, 0x41ca7a1d OK
55: 0x41e3e02a, 0x41e3e02a OK
56: 0x41fd4637, 0x41fd4637 OK
57: 0x4216ac44, 0x4216ac44 OK
58: 0x42301251, 0x42301251 OK
59: 0x4249785e, 0x4249785e OK
60: 0x4262de6b, 0x4262de6b OK
61: 0x427c4478, 0x427c4478 OK
62: 0x4295aa85, 0x4295aa85 OK
63: 0x42af1092, 0x42af1092 OK
0 errors
```