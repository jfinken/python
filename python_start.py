#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Copyright (c) 2010 earthmine, inc. All rights reserved.
"""

usage = """
untitled.py - script will do some stuff 

Usage:

untitled.py [-flags_here] params here
    
"""

import sys

def main(argv=None):
    
    """Main entry point"""
    if argv is None:
        argv = sys.argv

    # clip of 'python' from argv if its there
    if argv[0].find('ython') != -1:
        del argv[0]

    # make sure we have required arguments
    if len(argv) < 3:
        print usage
        sys.exit(1)


if __name__ == "__main__":
    sys.exit(main())


