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
from threading import Thread

# grab the path from the command line, where the path is the last
# element in the command line list
dir = sys.argv[-1]
# command = 'find ' + dir + ' -name "*.jpg"'
#print "About to call: %s" % (command)

# define thread
class Worker(Thread):
    def __init__(self, dir):
        Thread.__init__(self)
        self.dir = dir
        self.corrupt_list = []
        self.files_examined = 0;

    def run(self):
        #get the work list
        command = 'find ' + dir + ' -name "*.jpg"'
            
        # execute the find command
        output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).communicate()[0]

        # split the list by whitespace
        files = output.split()
        # files = files[:10] #only operate on 10 files

        # call 'identify' for each jpg and grep for a corruption
        for file in files:
            #identify = 'identify -regard-warnings ' + file
            #out = subprocess.Popen(identify, shell=True, stdout=subprocess.PIPE).communicate()[0]   
    
            # this guy gives me the return code... 0 is good, 1 is bad
            out = subprocess.call(["identify", "-regard-warnings", file])
    
            if out == 1:
                self.corrupt_list.append(file)

            self.files_examined = self.files_examined + 1

# worker list
workers = []            
# send each dir to a worker and start

current = Worker(dir)
workers.append(current)
current.start()

# compile results
files_examined = 0
all_corrupt_list = []
for worker in workers
    worker.join()
    files_examined += worker.files_examined
    all_corrupt_list.append(worker.corrupt_list)

print ""
print "-----------------------------------------"
print "Files examined:\t",files_examined

if len(all_corrupt_list) == 0:
    print "All jpegs are intact!"
else:
    print "Corrupt jpegs:\t",len(all_corrupt_list),"\nThey are:"
    for jpg in all_corrupt_list:
        print jpg 

print "-----------------------------------------"
