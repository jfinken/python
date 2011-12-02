#!/usr/bin/env python
# encoding: utf-8
"""
jp2_full_tileset_test.py

Copyright (c) 2010 earthmine, inc. All rights reserved.
"""

usage = """
jp2_full_tileset_test.py 

Loop over the entire tileset downloading subsets of jp2 files.  Used to replicate the 
equivalent of an earthmine client tile download.

Usage:

jp2_full_tileset_test.py 
    
"""
import sys
import os
import urllib2

# note the S3 bucket is in here
BASE_SERVICE = 'http://ec2-67-202-8-249.compute-1.amazonaws.com:9001/adore-djatoka/resolver?url_ver=Z39.88-2004&rft_id=http://s3.amazonaws.com/tiles.earthmine.com/'

REGION_SERVICE = '&svc_id=info:lanl-repo/svc/getRegion&svc_val_fmt=info:ofi/fmt:kev:mtx:jpeg2000&svc.format=image/jpeg&svc.rotate=0'

#PANO_IDS = ['269', '66']
PANO_IDS = ['269']

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

    #levels = [0, 1, 2, 3]
    #levels = [0]
    #levels = [1]
    #levels = [2]
    levels = [3]

    faces = ['f.jp2', 'r.jp2', 'l.jp2', 'b.jp2', 'u.jp2', 'd.jp2']
    # how many iterations
    for iter in range(20):
        for p in PANO_IDS:
            for f in faces:
                for lev in levels:
                    tps = get_tiles_per_side(lev)
                    width = get_tile_width(lev)
                    for y in range(tps):
                        for x in range(tps):
                            offset = str(y*width)+','+str(x*width)+','+str(width)+','+str(width)
                            print '[iter '+str(iter)+'] Fetching '+f+' for pano '+p+' level '+str(lev)+' offset '+offset
                            url = BASE_SERVICE + p +'/'+ f + REGION_SERVICE + '&svc.level='+str(lev)+'&svc.region='+offset
                            #print url
                            response = urllib2.urlopen(url)
                            html = response.read()

if __name__ == "__main__":
    sys.exit(main())
