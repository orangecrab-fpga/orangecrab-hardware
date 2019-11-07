#!/usr/bin/env python3
import sys

from litex import RemoteClient

from sdram_init import *

wb = RemoteClient(debug=False)
wb.open()

# # #

# Tests---------------------------------------------------------------------------------------------
sdram_initialization  = True
sdram_write_training  = False
sdram_read_training   = True
sdram_test            = True

# Parameters----------------------------------------------------------------------------------------

N_BYTE_GROUPS = 2
NDELAYS       = 8

# MPR
MPR_PATTERN = 0b01010101

# MR3
MPR_SEL   = (0b00<<0)
MPR_ENABLE = (1<<2)

# Software helpers/models---------------------------------------------------------------------------

def ddram_software_control():
    wb.regs.sdram_dfii_control.write(0)

def ddram_hardware_control():
    wb.regs.sdram_dfii_control.write(dfii_control_sel)

def ddram_mr_write(reg, value):
    wb.regs.sdram_dfii_pi0_baddress.write(reg)
    wb.regs.sdram_dfii_pi0_address.write(value)
    wb.regs.sdram_dfii_pi0_command.write(dfii_command_ras | dfii_command_cas | dfii_command_we | dfii_command_cs)
    wb.regs.sdram_dfii_pi0_command_issue.write(1)

def ddram_reset_wdelays():
    for i in range(N_BYTE_GROUPS):
        wb.regs.ddrphy_dly_sel.write(1<<i)
        wb.regs.ddrphy_wdly_dqs_rst.write(1)
        wb.regs.ddrphy_dly_sel.write(0)

def ddram_reset_rdelays():
    for i in range(N_BYTE_GROUPS):
        wb.regs.ddrphy_dly_sel.write(1<<i)
        wb.regs.ddrphy_rdly_dq_rst.write(1)
        wb.regs.ddrphy_dly_sel.write(0)

def ddram_set_bitslip(bitslip):
    for i in range(N_BYTE_GROUPS):
        wb.regs.ddrphy_dly_sel.write(1<<i)
        wb.regs.ddrphy_rdly_dq_bitslip_rst.write(1)
        for i in range(bitslip):
            wb.regs.ddrphy_rdly_dq_bitslip.write(1)
        wb.regs.ddrphy_dly_sel.write(0)


def ddram_set_rdelay(rdelay):
    for i in range(N_BYTE_GROUPS):
        wb.regs.ddrphy_dly_sel.write(1<<i)
        wb.regs.ddrphy_rdly_dq_rst.write(1)
        for i in range(rdelay):
            wb.regs.ddrphy_rdly_dq_inc.write(1)
        wb.regs.ddrphy_dly_sel.write(0)

# software control
ddram_software_control()

# DDRAM Initialization------------------------------------------------------------------------------

if sdram_initialization:
    for i, (comment, a, ba, cmd, delay) in enumerate(init_sequence):
        print(comment)
        wb.regs.sdram_dfii_pi0_address.write(a)
        wb.regs.sdram_dfii_pi0_baddress.write(ba)
        if i < 2:
            wb.regs.sdram_dfii_control.write(cmd)
        else:
            wb.regs.sdram_dfii_pi0_command.write(cmd)
            wb.regs.sdram_dfii_pi0_command_issue.write(1)

# DDRAM Write Training------------------------------------------------------------------------------

if sdram_write_training:

    class DDRAMWriteLeveling:
        def enable(self):
            ddram_mr_write(1, ddrx_mr1 | (1 << 7))
            wb.regs.ddrphy_wlevel_en.write(1)

        def disable(self):
            ddram_mr_write(1, ddrx_mr1)
            wb.regs.ddrphy_wlevel_en.write(0)

        def run(self):
            print("Write leveling...")
            ddram_reset_wdelays()
            self.enable()
            delays = [-1]*N_BYTE_GROUPS
            for i in range(N_BYTE_GROUPS):
                print("m{}:".format(i), end="")
                # scan taps
                taps_scan = [0]*NDELAYS
                for j in range(NDELAYS):
                    zero_count = 0
                    one_count = 0
                    for k in range(2):
                        wb.regs.ddrphy_wlevel_strobe.write(1)
                        dq = wb.regs.sdram_dfii_pi0_rddata.read()
                        if dq & 0b1:
                            one_count += 1
                        else:
                            zero_count += 1
                    if (one_count > zero_count):
                        taps_scan[j] = 1
                    else:
                        taps_scan[j] = 0
                    print("{}".format(taps_scan[j]), end="")
                    sys.stdout.flush()
                    wb.regs.ddrphy_wdly_dq_inc.write(1);
                    wb.regs.ddrphy_wdly_dqs_inc.write(1);
                print("|", end="");

                # select last 0/1 transition
                one_window_active = 0
                one_window_start = 0
                for j in range(NDELAYS):
                    if one_window_active:
                        if taps_scan[j] == 0:
                            one_window_active = 0
                    else:
                        if taps_scan[j]:
                            one_window_active = 1
                            one_window_start = j
                delays[i] = one_window_start
                print(delays[i])

            # configure delays
            wb.regs.ddrphy_wdly_dq_rst.write(1)
            wb.regs.ddrphy_wdly_dqs_rst.write(1)
            # need to init manually on Ultrascale
            for j in range(wb.regs.ddrphy_wdly_dqs_taps.read()):
                wb.regs.ddrphy_wdly_dqs_inc.write(1)
            for j in range(delays[i]):
                wb.regs.ddrphy_wdly_dq_inc.write(1)
                wb.regs.ddrphy_wdly_dqs_inc.write(1)

            print(" delay: {:02d}".format(delays[i]))
            self.disable()

    ddram_leveling = DDRAMWriteLeveling()
    ddram_leveling.run()

# DDRAM Read Training-------------------------------------------------------------------------------

if sdram_read_training:

    # PHY DATA mapping:
    # 8 bit module:
    # DQ0:
    # p0 [-------1-------0]
    # p1 [-------3-------2]

    def command_prd(address, baddress, cmd):
        wb.regs.sdram_dfii_pi0_address.write(address)
        wb.regs.sdram_dfii_pi0_baddress.write(baddress)
        wb.regs.sdram_dfii_pi0_command.write(cmd)
        wb.regs.sdram_dfii_pi0_command_issue.write(1)

    def command_pwr(address, baddress, cmd):
        wb.regs.sdram_dfii_pi1_address.write(address)
        wb.regs.sdram_dfii_pi1_baddress.write(baddress)
        wb.regs.sdram_dfii_pi1_command.write(cmd)
        wb.regs.sdram_dfii_pi1_command_issue.write(1)

    class DDRAMReadLeveling:
        def enable_mpr(self):
            ddram_mr_write(3, MPR_SEL | MPR_ENABLE)

        def disable_mpr(self):
            ddram_mr_write(3, 0)

        def run(self):
            print("Read leveling...")
            ddram_reset_rdelays()
            ddram_set_bitslip(0)
            self.enable_mpr()
            for i in range(NDELAYS):
                ddram_set_rdelay(i)
                print("delay: {} |".format(i), end="")
                command_prd(0, 0, dfii_command_cas|dfii_command_cs|dfii_command_rddata)
                p0 = wb.regs.sdram_dfii_pi0_rddata.read()
                p1 = wb.regs.sdram_dfii_pi1_rddata.read()
                for j in range(16):
                    dq = 0
                    dq |= (p1 >> (16 + j)) & 0b1
                    dq <<= 1
                    dq |= (p1 >> (0 + j)) & 0b1
                    dq <<= 1
                    dq |= (p0 >> (16 + j)) & 0b1
                    dq <<= 1
                    dq |= (p0 >> (0 + j)) & 0b1
                    print("dq{:d}: 0b{:08b}, ".format(j, dq))

            for j in range(N_BYTE_GROUPS):
                wb.regs.ddrphy_dly_sel.write(1 << j)
                wb.regs.ddrphy_rdly_dq_inc.write(1)
                wb.regs.ddrphy_dly_sel.write(0)
            self.disable_mpr()

    ddram_leveling = DDRAMReadLeveling()
    ddram_leveling.run()

# DDRAM Test----------------------------------------------------------------------------------------

if sdram_test:
    ddram_set_rdelay(7)
    ddram_set_bitslip(0)

    # hardware control
    ddram_hardware_control()

    def seed_to_data(seed, random=True):
        if random:
            return (1664525*seed + 1013904223) & 0xffffffff
        else:
            return seed

    def write_pattern(length):
        for i in range(length):
            wb.write(wb.mems.main_ram.base + 4*i, seed_to_data(i))

    def check_pattern(length, debug=False):
        errors = 0
        for i in range(length):
            error = 0
            if wb.read(wb.mems.main_ram.base + 4*i) != seed_to_data(i):
                error = 1
                if debug:
                    print("{}: 0x{:08x}, 0x{:08x} KO".format(i, wb.read(wb.mems.main_ram.base + 4*i), seed_to_data(i)))
            else:
                if debug:
                    print("{}: 0x{:08x}, 0x{:08x} OK".format(i, wb.read(wb.mems.main_ram.base + 4*i), seed_to_data(i)))
            errors += error
        return errors

    write_pattern(64)
    errors = check_pattern(64, debug=True)
    print("{} errors".format(errors))

# # #

wb.close()
