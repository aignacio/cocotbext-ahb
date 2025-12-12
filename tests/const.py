#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : const.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 08.10.2023
# Last Modified Date: 08.10.2023

import glob
import os


class cfg:
    RST_CYCLES = 3
    CLK_100MHz = (10, "ns")
    TIMEOUT_TEST = (CLK_100MHz[0] * 200, "ns")

    TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
    RTL_DIR = os.path.join(TESTS_DIR, "dut")
    TOPLEVEL = str(os.getenv("DUT"))
    SIMULATOR = str(os.getenv("SIM"))
    VERILOG_SOURCES = []  # The sequence below matters...
    VERILOG_SOURCES += glob.glob(f"{RTL_DIR}**/*.v", recursive=True)
    EXTRA_ENV = {}
    EXTRA_ENV["COCOTB_HDL_TIMEPRECISION"] = os.getenv("TIMEPREC")
    EXTRA_ENV["COCOTB_HDL_TIMEUNIT"] = os.getenv("TIMEUNIT")
    TIMESCALE = (os.getenv("TIMEUNIT"), os.getenv("TIMEPREC"))

    if SIMULATOR == "verilator":
        EXTRA_ARGS = [
            "--trace-fst",
            "--coverage",
            "--coverage-line",
            "--coverage-toggle",
            "--trace-structs",
            "--Wno-UNOPTFLAT",
            "--Wno-REDEFMACRO",
        ]
    elif SIMULATOR == "icarus":
        EXTRA_ARGS = ["WAVES=1"]

        EXTRA_ARGS = []
