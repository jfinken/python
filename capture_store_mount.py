#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by josh on 07-21-2009
Copyright (c) 2009 earthmine, inc. All rights reserved.

1) when 'captureStore' is detected, begin looping, incrementing a counter.  Create
    a device node for the smaller counter number available at /dev/captureStore
    
2) Given the incremented device node, mount that device node as /media/captureStoreN where N is the next.

"""
import os
import sys
import fnmatch
import subprocess

src = "/dev/captureStore%d"
dest = "/media/captureStore%d"
MAX_DEVICE_STORES = 36

if len(sys.argv) > 1:
    mountNum = int(sys.argv[-1])
    
    #first make the path if necessary
    if os.path.exists(dest % mountNum) != True:
        os.mkdir(dest % mountNum)

    # now mount
    command = 'mount -t ext3 ' + src % mountNum + ' ' + dest % mountNum
    # do it
    output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).communicate()[0]
else:
    # find the next (lowest) device number
    for i in range(MAX_DEVICE_STORES):
        file = src % i
        if os.path.exists(file) != True:
            print i
            break

