#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import re
import glob
import collections

usage = """
main_parser.py - parse a directory of earthmine server log files 

Usage:

main_parser.py /path/to/logs/
    
""" 

logsList = []

class Parser:
  def __init__(self):
    """Parser initialization"""
    self.call_times = dict()
 
  def Parse(self, line):
   
    #----------------------------------------------------------
    # build map of api call counts and times
    #----------------------------------------------------------

    # start with substring of the call
    substr = ''
    pos = self.re_pos(line, 'get-')
    if pos != -1:
      substr = line[pos:]
    matches = self.get_res(substr,
        'get-[A-Za-z]+-*[A-Za-z]*-*[A-Za-z]*')

    # should only be one if any
    for call in matches:
      call = str(call)
      if call not in self.call_times:
        self.call_times[call] = []

      # build a list of call times for the api call
      times = self.get_res(substr, '[0-9]+')
      for time in times:
        self.call_times[call].append(time)

    # sanity
    #if 'get-panoramas' in self.call_times:
    #  print self.call_times['get-panoramas']
    
  # return the match itself
  def get_res(self, in_str, pat):
    return re.findall(pat, in_str)

  # return the position in the string of the match
  def re_pos(self, in_str, pat):
    p = re.compile(pat)
    pos = -1
    # should only be one, if any
    for m in p.finditer(in_str):
      pos = m.start()
        
    return pos

def listFiles():
  p = Parser() 
  file_list = glob.glob(os.path.join(sys.argv[1], '*access.log'))
 
  # split filename from path
  if len(sys.argv) == 2:
      for file in file_list:
        lines = [line.strip() for line in open(file)]
        for line in lines:
          p.Parse(line)

        #head = os.sep.join(file.split(os.sep)[:-1])
        #tail = file.split(os.sep)[-1]
        #logsList.append([head, tail])

def main(argv=None):
    
    """Main entry point"""
    if argv is None:
        argv = sys.argv

    # clip of 'python' from argv if its there
    if argv[0].find('ython') != -1:
        del argv[0]

    # make sure we have required arguments
    if len(argv) < 2:
        #print usage
        print foo_bar
        sys.exit(1)

    listFiles()

if __name__ == "__main__":
    sys.exit(main())
