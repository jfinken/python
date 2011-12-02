#!/usr/bin/env python
# encoding: utf-8
"""
capture_store_umount.py

Created by josh on 07-21-2009
Copyright (c) 2009 earthmine, inc. All rights reserved.

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
    
    # now unmount first
    command = 'umount -t ext3 ' + dest % mountNum
    # do it
    output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).communicate()[0]

    # key component: remove the mount point directory
    umount = 'rmdir ' + dest % mountNum
    output = subprocess.Popen(umount, shell=True, stdout=subprocess.PIPE).communicate()[0]
else:
    # find the next (lowest) device number
    for i in range(MAX_DEVICE_STORES):
        srcfile = src % i
        destfile = dest % i
        # if the device node file does NOT exist, but the mount point does, that's our dog
        if (os.path.exists(srcfile) != True) and (os.path.exists(destfile) == True):
            print i
            break

