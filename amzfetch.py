#!/usr/bin/env python
# amzfetch.py
# Description: Tool for downloading Amazon MP3s using a .amz file.
# Version: 0.00.00
# Last Updated: Sat 27 Sep 2014 01:40:22 PM PDT    
# Leigh Burton, lburton@metacache.net
# Status: Parsing URL, song name, artist & album to screen working. 
 
import os
import sys
import argparse
from xml.dom import minidom


def main(arguments):

    script, input_file = sys.argv
    
    xmldoc = minidom.parse(input_file)
    itemloc = xmldoc.getElementsByTagName('location')
    itemtitle = xmldoc.getElementsByTagName('title')
    itemcreator = xmldoc.getElementsByTagName('creator')
    itemalbum = xmldoc.getElementsByTagName('album')
     
    print "%s Songs \n" % len(itemloc)
    itemtotal = len(itemloc)
    itemtotal = itemtotal - 1
    itemfoo = 0
    while itemfoo != itemtotal:
        print "URL: %s" % itemloc[itemfoo].childNodes[0].nodeValue
        print "Song: %s" % itemtitle[itemfoo + 1].childNodes[0].nodeValue
        print "Artist: %s" % itemcreator[itemfoo].childNodes[0].nodeValue
        print "Album: %s \n" % itemalbum[itemfoo].childNodes[0].nodeValue
        itemfoo = itemfoo + 1

#for line in prop:
#    line2 = line.strip( )
#    print line2
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
