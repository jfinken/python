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
import threadpool
#import thread

corrupt_jpegs = []
files_examined = 0

# callable for each worker
def do_identify(file):
    out = subprocess.call(["identify", "-regard-warnings", file])
    return (out, file)

# callback when worker returns
def onIndentifyComplete(request, (out, file)):
    global corrupt_jpegs
    if out == 1:
        corrupt_jpegs.append(file)

    """
    global files_examined
    lock.acquire()
    try:
        files_examined += 1
    finally:
        lock.release()
    """
    
# assemble a list of files by grabbing the path from the command line, where the path is the last
# element in the command line list
dir = sys.argv[-1]
command = 'find ' + dir + ' -name "*.jpg"'
#print "About to call: %s" % (command)

# execute the find command
output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).communicate()[0]

# split the list by whitespace
files = output.split()
print len(files), " files to process...";
requests = threadpool.makeRequests(do_identify, files, onIndentifyComplete)

# create worker pool
poolSize = 32    
print "Creating thread pool of %d worker threads..." % poolSize
pool = threadpool.ThreadPool(poolSize)

# put requests in queue..
for req in requests:
    pool.putRequest(req)

# wait for all to finish    
try:
    pool.wait()
except AttributeError:
    pass

# results
print ""
print "-----------------------------------------"
print "Files examined:\t",len(files)

if len(corrupt_jpegs) == 0:
    print "All jpegs are intact!"
else:
    print "Corrupt jpegs:\t",len(corrupt_jpegs),"\nThey are:"
    for jpg in corrupt_jpegs:
      	print jpg 

print "-----------------------------------------"
print ""
