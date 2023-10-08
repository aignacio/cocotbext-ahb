#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : __init__.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 08.10.2023
# Last Modified Date: 08.10.2023

# Imported all classes in the default constructor to avoid
# specific imports by knowing the folder/files
# ex. without this:
# from cocotbext.ahb.ahb_master import AHBLiteMaster
# from cocotbext.ahb.ahb_bus import AHBBus
# ex. with this:
# from cocotbext.ahb import AHBLiteMaster, AHBBus
from .ahb_master import AHBLiteMaster
from .ahb_bus import AHBBus
