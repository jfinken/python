#!/usr/bin/env python
# encoding: utf-8
"""
gps_time_to_date.py

Created by josh on 08-18-2009
Copyright (c) 2009 earthmine, inc. All rights reserved.

given gps week to gps milliseconds

"""
import os
import sys
import string
import time
import math

if len(sys.argv) < 3:
    print "\nUsage: gps_time_to_date gpsWeek gpsMs\n"
    exit() 

gpsWeek = int(sys.argv[1])
gpsMilliSeconds = int(sys.argv[2])
year = 1980 
month = 1 
day = 6
mjd = 367 * year - 7 * (year + (month + 9) / 12) / 4 - 3 * ((year + (month - 9) / 7) / 100 + 1) / 4 + 275 * month / 9 + day + 1721028 - 2400000 + gpsWeek*7 + (gpsMilliSeconds/86400000)

J = mjd + 2400001 + 68569
C = 4 * J / 146097
J = J - (146097 * C + 3) / 4
Y = 4000 * (J + 1) / 1461001
J = J - 1461 * Y / 4 + 31
M = 80 * J / 2447


#Get Hrs / Mins/ Seconds

hour = math.floor((gpsMilliSeconds-(math.floor(gpsMilliSeconds/86400000)*86400000))/3600000)
minute =  math.floor((gpsMilliSeconds -hour*3600000 - math.floor(gpsMilliSeconds/86400000)*86400000)/60000)
second = (gpsMilliSeconds -hour*3600000 -minute*60000-math.floor(gpsMilliSeconds/86400000)*86400000)/1000

day = (int) (J - 2447 * M / 80)
J = M / 11;
month = (int) (M + 2 - (12 * J))
year = (int) (100 * (C - 49) + Y + J)

print "Date: "+str(month) + "/" + str(day) + "/" + str(year) +"\tTime: " + str(hour) + ":" + str(minute) + ":" + str(second) + "+00"
