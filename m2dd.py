#!/usr/bin/env python
# encoding: utf-8
"""
m2dd.py

Copyright (c) 2010 earthmine, inc. All rights reserved.
"""
import sys
import math

usage = """
m2dd.py - script to convert meters to decimal degrees, at the given latitude

Usage:

m2dd.py latitude meters 
"""

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

    # convert
    circumference = 2.0 * math.pi * calculateEarthRadius( float(argv[1]) )
    decimal_degrees = 360 * float(argv[2]) / circumference

    print '%.10f'%decimal_degrees

def calculateEarthRadius(lat):
    a = 6378137.0
    b = 6356752.3
    latRadians = math.radians(lat)
    cosLat = math.cos(latRadians)
    sinLat = math.sin(latRadians)
    
    numer = math.pow(a*a*cosLat, 2) + math.pow(b*b*sinLat, 2)
    denom = math.pow(a*cosLat, 2) + math.pow(b*sinLat, 2)

    return math.sqrt(numer/denom)


if __name__ == "__main__":
    sys.exit(main())


