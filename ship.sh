#!/bin/bash
docker run -it --rm -v $(pwd):/cocotbext-ahb/ -w /cocotbext-ahb/ aignacio/rtldev bash
