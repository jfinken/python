#!/usr/bin/env python
# encoding: utf-8
"""
jp2_full_tileset_test.py

Copyright (c) 2010 earthmine, inc. All rights reserved.
"""

usage = """
s3_tileset_test.py 

Loop over the entire tileset downloading tiles from s3.  

Usage:

s3_tileset_test.py 
    
"""
import sys
import os
import urllib2

BASE_SERVICE = 'http://s3.earthmine.com/tile/'
PANO_IDS = ['1000006664842']

def get_tile_width(tile_level):
    if tile_level == 0:
        return(256)
    else:
        return(512)

def get_tiles_per_side(tile_level):
    lev = tile_level - 1
    if lev < 0:
        lev = 0

    return(pow(2, lev))

def main(argv=None):

    global BASE_SERVICE
    global REGION_SERVICE
    global PANO_IDS

    #tile_levels = ['z_p']
    #tile_levels = ['z_0']
    #tile_levels = ['z_1']
    tile_levels = ['z_2']
    #tile_levels = ['z_p', 'z_0', 'z_1', 'z_2']

    faces = ['f', 'r', 'l', 'b', 'u', 'd']
    stuff = ['00', '01', '10', '11']
    stuff2 = ['00', '01', '02', '03',
              '10', '11', '12', '13',
              '20', '21', '22', '33',
              '30', '31', '32', '33']

    for iter in range(20):
        for p in PANO_IDS:
            for f in faces:
                for l in range(len(tile_levels)):
                    lev = tile_levels[l]
                    tps = get_tiles_per_side(l)
                    for thing in stuff2:
                    #for y in range(tps):
                    #    for x in range(tps):
                        file = thing+'.jpg'
                        #file = str(x) + str(y)+'.jpg'
                        url = BASE_SERVICE + p[0:3]+'/'+p[3:6] +'/'+p[6:9]+'/'+p+'/'+f+'/'+lev+'/'+file
                            #print 'Fetching '+url
                        print url
                        response = urllib2.urlopen(url)
                        html = response.read()

if __name__ == "__main__":
    sys.exit(main())
