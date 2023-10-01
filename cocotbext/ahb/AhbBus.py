#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : AhbBus.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson Ignacio da Silva (aignacio) <anderson@aignacio.com>
# Date              : 01.10.2023
# Last Modified Date: 01.10.2023
import logging
import cocotb
from cocotb_bus.bus import Bus

from .version import __version__
class AhbBus(Bus):
    def __init__(self):
        print("Hello World")
