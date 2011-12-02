#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by josh with great help from bryan on 2009-07-10.
Copyright (c) 2009 earthmine, inc. All rights reserved.
"""

import sys
import os
import subprocess

# grab the path from the command line, where the path is the last
# element in the command line list
dir = sys.argv[-1]
command = 'find ' + dir + ' -name "*.jpg"'
#print "About to call: %s" % (command)

# execute the find command
output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).communicate()[0]

# split the list by whitespace
files = output.split()
# files = files[:10] #only operate on 10 files

# call 'identify' for each jpg and grep for a corruption
status = []
files_examined = 0

for file in files:
    #identify = 'identify -regard-warnings ' + file
    #out = subprocess.Popen(identify, shell=True, stdout=subprocess.PIPE).communicate()[0]   
    
    # this guy gives me the return code... 0 is good, 1 is bad
    out = subprocess.call(["identify", "-regard-warnings", file])
    
    if out == 1:
        status.append(file)

    files_examined = files_examined + 1

# results
print ""
print "-----------------------------------------"
print "Files examined:\t",files_examined

if len(status) == 0:
    print "All jpegs are intact!"
else:
    print "Corrupt jpegs:\t",len(status),"\nThey are:"
    for jpg in status:
        print jpg 

print "-----------------------------------------"
