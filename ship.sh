#!/bin/bash
docker run -it --rm --name rtldev -v $(pwd):/cocotbext-ahb/ -w /cocotbext-ahb/ aignacio/rtldev bash
