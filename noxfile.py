#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : noxfile.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson Ignacio da Silva (aignacio) <anderson@aignacio.com>
# Date              : 30.09.2023
# Last Modified Date: 02.10.2023
import nox

@nox.session(python=["3.6", "3.7", "3.8", "3.9", "3.10"])
def run(session):
    session.env['DUT'] = 'ahb_template'
    session.env['SIM'] = 'verilator'
    session.env['TIMEPREC'] = '"100ps"'
    session.env['TIMEUNIT'] = '"1ns"'
    session.install('pytest',
                    'pytest-xdist',
                    'pytest-split',
                    'cocotb-bus == 0.2.1',
                    'cocotb-test == 0.2.4',
                    'cocotb >= 1.8.0')
    session.install("-e", ".")
    session.run('pytest', '-rP', '-n', 'auto')
