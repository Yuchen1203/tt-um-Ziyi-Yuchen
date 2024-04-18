
# SPDX-FileCopyrightText: © 2023 Uri Shaked <uri@tinytapeout.com>
# SPDX-License-Identifier: MIT

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles
from cocotb.binary import BinaryValue

@cocotb.test()
async def test_pwm_with_reset_and_timing(dut):
    dut._log.info("Start")

    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1
    print(dut.clk)
    
    for i in range(100):
        await ClockCycles(dut.clk, 10)
        print(dut.uo_out[0].value)
