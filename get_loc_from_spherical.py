#!/usr/bin/env python
"""
example.py

earthmine API example python script
Tom Slankard <tom@earthmine.com>
Copyright 2009 earthmine inc.

This example is for illustrative purposes only, and is provided AS IS.
Use at your own risk.

This example does three things: 
1. Fetches views of a latitude and longitude with a "get-views" request.
2. Retrieves the image associated with a view returned and displays it.
3. Fetches 3D locations and quality for pixels in the image using a
   "get-locations-from-view" request.
"""

import httplib
import hashlib
import time
import sys
import json
import urllib

#  set API key and shared secret
key = "v2p44ypo8on5ne62f961qp1k"
secret = "iVKJLlJm99"

if key == "" or secret == "":
    print "Don't forget to set your API key and shared secret!"
    sys.exit()

def make_api_request(body):
    """Submit a JSON-encoded request to the earthmine API cloud service"""
    
    #  create a connection to the service endpoint
    conn = httplib.HTTPConnection("cloud.earthmine.com", timeout=100)
    
    #  add the API key to HTTP headers
    headers = {"x-earthmine-auth-id" : key}
    
    #  sign the request
    timestamp = str(int(time.time()))
    stringtosign = key + secret + timestamp
    sig = hashlib.md5(stringtosign).hexdigest()
    
    #  make the request
    conn.request("POST", "/service?sig=" + sig + "&timestamp=" + timestamp, body, headers)
    response = conn.getresponse()
    
    #  check for error
    if response.status != 200:
        print "An error occurred! HTTP status:", r1.status
        sys.exit()
    
    return response

#  create get-views API request in JSON format
body2="""
{
    "operation": "get-locations-from-spherical",
    "parameters" : {
        "request" : { "pano-id": "1000003067065",
        "relative-locations" : [{"yaw":140.8887,"pitch":-8.771}]
        } 
    }
}
"""
# submit the request to the server
print "Fetching views of specified latitude and longitude..."
r1 = make_api_request(body2)

#  parse JSON into a python dictionary
parsed_response = json.loads( r1.read() )
#print "    Found %d views." % (len(parsed_response['result']['views']))
print parsed_response


