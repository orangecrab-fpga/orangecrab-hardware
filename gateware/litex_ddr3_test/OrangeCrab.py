# This file is Copyright (c) 2017 Serge 'q3k' Bazanski <serge@bazanski.pl>
# License: BSD

from litex.build.generic_platform import *
from litex.build.lattice import LatticePlatform
from litex.build.lattice.programmer import LatticeProgrammer

# IOs ----------------------------------------------------------------------------------------------

_io = [
    ("clk100", 0, Pins("A9"), IOStandard("LVCMOS33")),
    ("rst_n", 0, Pins("R16"), IOStandard("LVCMOS25")),

    ("user_led", 0, Pins("V17"), IOStandard("LVCMOS25")),
    ("user_led", 1, Pins("T17"), IOStandard("LVCMOS25")),
    ("user_led", 2, Pins("R17"), IOStandard("LVCMOS25")),


    ("serial", 0,
        Subsignal("rx", Pins("L4"), IOStandard("LVCMOS33")),
        Subsignal("tx", Pins("K4"), IOStandard("LVCMOS33")),
    ),

    ("ddram", 0,
        Subsignal("a", Pins(
            "A4 D2 C3 C7 D3 D4 D1 B2",
            "C1 A2 A7 C2 C4"),
            IOStandard("SSTL135_I")),
        Subsignal("ba", Pins("B6 B7 A6"), IOStandard("SSTL135_I")),
        Subsignal("ras_n", Pins("C12"), IOStandard("SSTL135_I")),
        Subsignal("cas_n", Pins("D13"), IOStandard("SSTL135_I")),
        Subsignal("we_n", Pins("B12"), IOStandard("SSTL135_I")),
        Subsignal("cs_n", Pins("A12"), IOStandard("SSTL135_I")),
        Subsignal("dm", Pins("G16 D16"), IOStandard("SSTL135_I")),
        Subsignal("dq", Pins(
            "F17 F16 G15 F15 J16 C18 H16 F18",
            "C17 D15 B17 C16 A15 B13 A17 A13"),
            IOStandard("SSTL135_I"),
            Misc("TERMINATION=75")),
        Subsignal("dqs_p", Pins("G18 B15"), IOStandard("SSTL135D_I"), Misc("TERMINATION=OFF"), Misc("DIFFRESISTOR=100")),
        Subsignal("clk_p", Pins("J18"), IOStandard("SSTL135D_I")),
        Subsignal("cke", Pins("D6"), IOStandard("SSTL135_I")),
        Subsignal("odt", Pins("C13"), IOStandard("SSTL135_I")),
        Subsignal("reset_n", Pins("B1"), IOStandard("SSTL135_I")),
        Subsignal("vccio", Pins("D18 K16 B18"), IOStandard("SSTL135_II"), Misc("DRIVE=10")),
        Misc("SLEWRATE=FAST"),
    ),

]



# Connectors ---------------------------------------------------------------------------------------

_connectors = [
]

# Platform -----------------------------------------------------------------------------------------

class Platform(LatticePlatform):
    default_clk_name = "clk100"
    default_clk_period = 10

    def __init__(self, **kwargs):
        LatticePlatform.__init__(self, "LFE5U-25F-8MG285C", _io, _connectors, **kwargs)

    def do_finalize(self, fragment):
        try:
            self.add_period_constraint(self.lookup_request("eth_clocks", 0).rx, 1e9/125e6)
        except ConstraintError:
            pass
        try:
            self.add_period_constraint(self.lookup_request("eth_clocks", 1).rx, 1e9/125e6)
        except ConstraintError:
            pass

    def create_programmer(self, with_ispclock=True):
        _xcf_ispclock = """
        <Device>
            <SelectedProg value="FALSE"/>
            <Pos>2</Pos>
            <Vendor>Lattice</Vendor>
            <Family>ispCLOCK</Family>
            <Name>ispPAC-CLK5406D</Name>
            <IDCode>0x00191043</IDCode>
            <Operation>Erase,Program,Verify</Operation>
            <Bypass>
                <InstrLen>8</InstrLen>
                <InstrVal>11111111</InstrVal>
                <BScanLen>1</BScanLen>
                <BScanVal>0</BScanVal>
            </Bypass>
        </Device>
"""

        _xcf_template = """
<?xml version='1.0' encoding='utf-8' ?>
<!DOCTYPE        ispXCF    SYSTEM    "IspXCF.dtd" >
<ispXCF version="3.4.1">
    <Comment></Comment>
    <Chain>
        <Comm>JTAG</Comm>
        <Device>
            <SelectedProg value="TRUE"/>
            <Pos>1</Pos>
            <Vendor>Lattice</Vendor>
            <Family>ECP5UM5G</Family>
            <Name>LFE5UM5G-45F</Name>
            <IDCode>0x81112043</IDCode>
            <File>{{bitstream_file}}</File>
            <Operation>Fast Program</Operation>
        </Device>{ispclock}
    </Chain>
    <ProjectOptions>
        <Program>SEQUENTIAL</Program>
        <Process>ENTIRED CHAIN</Process>
        <OperationOverride>No Override</OperationOverride>
        <StartTAP>TLR</StartTAP>
        <EndTAP>TLR</EndTAP>
        <VerifyUsercode value="FALSE"/>
    </ProjectOptions>
    <CableOptions>
        <CableName>USB2</CableName>
        <PortAdd>FTUSB-0</PortAdd>
        <USBID>LATTICE ECP5_5G VERSA BOARD A Location 0000 Serial Lattice ECP5_5G VERSA Board A</USBID>
    </CableOptions>
</ispXCF>
""".format(ispclock=_xcf_ispclock if with_ispclock else "")

        return LatticeProgrammer(_xcf_template)
