#!/usr/bin/env python
# encoding: utf-8

import os
import re
import time
import sys
import urllib

from threading import Thread

class testit(Thread):
   def __init__ (self,ip):
      Thread.__init__(self)
      self.ip = ip
      self.status = -1
   def run(self):
       while 1:
           try:
                print 'Running thread: '+self.ip
                u = urllib.urlopen('http://berlin:8081/fileserver_example.c')
                u.close
                #u = urllib.urlopen('http://sparky')
           except:
               print 'cannot connect...'
               pass
"""
           if u:
               print 'Thread: '+self.ip+' headers: '+str(u.headers)
               #print u.headers
               #print u.read()+'\n'
               u.close
               """

threadlist = []

for threadnum in range(0,200):
   ip = str(threadnum)
   current = testit(ip)
   threadlist.append(current)
   current.start()

for thread in threadlist:
   thread.join()
   #print "Status from ",pingle.ip,"is",report[pingle.status]
   #print "Status from ",pingle.ip

#print time.ctime()
