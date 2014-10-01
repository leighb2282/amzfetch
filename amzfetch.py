#!/usr/bin/env python
# amzfetch.py
# Description: Tool for downloading Amazon MP3s using a .amz file.
# Version: 0.10.20
# Last Updated: Wed 01 Oct 2014 10:00:42 AM PDT      
# Leigh Burton, lburton@metacache.net
# Status: IT WORKS!!!!! Sequential download of MP3s! 
 
import os
import sys
import argparse
import urllib2
from xml.dom import minidom

def main(arguments):

    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help = "Input file (.amz)")
    args = parser.parse_args(arguments)

    #_, input_file = sys.argv
    with open(args.infile, 'r') as input_file:
        xmldoc = minidom.parse(input_file)
        itemloc = xmldoc.getElementsByTagName('location')
        itemtitle = xmldoc.getElementsByTagName('title')
        itemtnum = xmldoc.getElementsByTagName('trackNum')
        itemcreator = xmldoc.getElementsByTagName('creator')
        itemalbum = xmldoc.getElementsByTagName('album')
     
    print "%s Songs \n" % len(itemloc)
    itemtotal = len(itemloc)
    itemfoo = 0
    while itemfoo != itemtotal:
        mp3url = itemloc[itemfoo].childNodes[0].nodeValue
        mp3title = itemtitle[itemfoo + 1].childNodes[0].nodeValue
        mp3tnum = itemtnum[itemfoo].childNodes[0].nodeValue
        mp3creator = itemcreator[itemfoo].childNodes[0].nodeValue
        mp3album = itemalbum[itemfoo].childNodes[0].nodeValue
        
        print "\033[94mArtist: \033[92m%s \033[94mSong: \033[92m%s \033[94mAlbum: \033[92m%s" % (mp3creator, mp3title, mp3album)
        print "\033[94mURL: \033[92m%s\n" % mp3url
        response = urllib2.urlopen(mp3url)
        mp3out = response.read()
        with open(mp3tnum + ' ' + mp3title + '.mp3', 'wb') as newfile:
                newfile.write(mp3out)
        itemfoo = itemfoo + 1
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
