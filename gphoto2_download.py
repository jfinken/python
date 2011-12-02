#!/usr/bin/env python
# encoding: utf-8
"""
format_capture_store.py

Created by josh on 08-18-2009
Copyright (c) 2009 earthmine, inc. All rights reserved.

1) run lsusb |grep Nikon to get the number of connected cameras and parse
out the bus and device number

2) make and cd to a destination dir (appears gphoto2 can only d/l to current dir)

3) for each port/device tuple in list, run 'gphoto2 --port usb:xxx,yyy --get-all-files'

"""
import os
import sys
import subprocess
import string
import re
import time

mediaRoot = "/media/captureStore0/gphoto2_test/"

def main():
    # first try, use bus and device passed in
    if len(sys.argv) > 2:
        port = str(sys.argv[1])
        bus = str(sys.argv[2])
        
    if os.path.exists(mediaRoot + port + "_" + bus) != True:
            os.mkdir(mediaRoot + port + "_" + bus)

    command = "cd "+mediaRoot + port + "_" + bus)
    retcode = subprocess.call(command, shell=True)
    if retcode != 0:
        print "Unable to cd to "+mediaRoot + port + "_" + bus + ".  Exiting..."
        return False

    # download files
    command = "gphoto2 --port usb:"+port+","+device+" --get-all-files"
    retcode = subprocess.call(command, shell=True)
    if retcode != 0:
        print "gphoto2 command: "+command+" failed.  Exiting..."
        return False



if __name__ == '__main__':
    main()


