# This file is Copyright (c) 2017 Serge 'q3k' Bazanski <serge@bazanski.pl>
# License: BSD

from litex.build.generic_platform import *
from litex.build.lattice import LatticePlatform

# IOs ----------------------------------------------------------------------------------------------

_io = [
    ("clk100", 0, Pins("A9"), IOStandard("LVCMOS33")),
    ("rst_n", 0, Pins("V17"), IOStandard("LVCMOS33")),

    ("usr_btn", 0, Pins("J17"),IOStandard("SSTL135_I")),
    ("user_led", 0, Pins("K4"),IOStandard("LVCMOS33")),

    ("rgb_led", 0,
        Subsignal("r", Pins("K4"), IOStandard("LVCMOS33")),
        Subsignal("g", Pins("M3"), IOStandard("LVCMOS33")),
        Subsignal("b", Pins("J3"), IOStandard("LVCMOS33")),    
    ),

    ("serial", 0,
        Subsignal("tx", Pins("N17"), IOStandard("LVCMOS33")),
        Subsignal("rx", Pins("M18"), IOStandard("LVCMOS33")),
    ),

    ("ddram", 0,
        Subsignal("a", Pins(
            "C4 D2 D3 A3 A4 D4 C3 B2",
            "B1 D1 A7 C2 B6"), #C1 A2 C7"),
            IOStandard("SSTL135_I"),Misc("SLEWRATE=SLOW")),
        Subsignal("ba", Pins("D6 B7 A6"), IOStandard("SSTL135_I"),Misc("SLEWRATE=SLOW")),
        Subsignal("ras_n", Pins("C12"), IOStandard("SSTL135_I"),Misc("SLEWRATE=SLOW")),
        Subsignal("cas_n", Pins("D13"), IOStandard("SSTL135_I"),Misc("SLEWRATE=SLOW")),
        Subsignal("we_n", Pins("B12"), IOStandard("SSTL135_I"),Misc("SLEWRATE=SLOW")),
        Subsignal("cs_n", Pins("A12"), IOStandard("SSTL135_I"),Misc("SLEWRATE=SLOW")),
        Subsignal("dm", Pins("D16 G16"), IOStandard("SSTL135_I"),Misc("SLEWRATE=SLOW")),
        Subsignal("dq", Pins(
            "C17 D15 B17 C16 A15 B13 A17 A13",
            "F17 F16 G15 F15 J16 C18 H16 F18"),
            IOStandard("SSTL135_I"),
            Misc("TERMINATION=OFF SLEWRATE=SLOW")),
        Subsignal("dqs_p", Pins("B15 G18"), IOStandard("SSTL135D_I"), Misc("TERMINATION=OFF DIFFRESISTOR=100 SLEWRATE=FAST")),
        Subsignal("clk_p", Pins("J18"), IOStandard("SSTL135D_I"),Misc("SLEWRATE=SLOW")),
        Subsignal("cke", Pins("D18"), IOStandard("SSTL135_I"),Misc("SLEWRATE=SLOW")),
        Subsignal("odt", Pins("C13"), IOStandard("SSTL135_I"),Misc("SLEWRATE=SLOW")),
        Subsignal("reset_n", Pins("L18"), IOStandard("SSTL135_I"),Misc("SLEWRATE=SLOW")),
        Subsignal("vccio", Pins("K16 D17 K15 K17 B18 C6"), IOStandard("SSTL135_II")),
        Subsignal("gnd", Pins("L15 L16"), IOStandard("SSTL135_II")),
    ),



    ("usb", 0,
        Subsignal("d_p", Pins("N1")),
        Subsignal("d_n", Pins("M2")),
        Subsignal("pullup", Pins("N2")),
        IOStandard("LVCMOS33")
    ),

    ("spiflash4x", 0,
        Subsignal("cs_n", Pins("U17"), IOStandard("LVCMOS33")),
        #Subsignal("clk",  Pins("R17"), IOStandard("LVCMOS33")),
        Subsignal("dq",   Pins("U18 T18 R18 N18"), IOStandard("LVCMOS33")),
    ),

]



# Connectors ---------------------------------------------------------------------------------------

_connectors = [
]

# Platform -----------------------------------------------------------------------------------------

class Platform(LatticePlatform):
    default_clk_name = "clk48"
    default_clk_period = int(1e9/48e6)

    def __init__(self, **kwargs):
        LatticePlatform.__init__(self, "LFE5U-25F-8MG285C", _io, _connectors, **kwargs)

