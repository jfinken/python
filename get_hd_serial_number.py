#!/usr/bin/env python
# encoding: utf-8
"""
requires smartmontools

Created by josh on 08-18-2009
Copyright (c) 2009 earthmine, inc. All rights reserved.
"""

import os
import sys
import subprocess
import re

node = "/dev/sda1"

command = "smartctl -a " + node + " |grep -i 'serial number'"
output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).communicate()[0]
# grep output
serial = re.split("(\n)", output)[0]
serial = re.split("(\s+)", serial)[-1]
print serial

