#!/usr/bin/env python
# amzfetch.py
# Description: Tool for downloading Amazon MP3s using a .amz file.
# Version: 0.00.00
# Last Updated: Fri 26 Sep 2014 11:35:13 PM PDT  
# Leigh Burton, lburton@metacache.net
# Status: it just dumps the input file to console.
 
import os
import sys
import argparse


def main(arguments):

    script, input_file = sys.argv
    in_file = open(input_file)
    prop = in_file.read()

    #This doesn't seem to strip the whitespace, even though it should.    
    striped = prop.strip()
    
    #print striped

    #This doesn't error, it just doesn't work :(
    with open('newfile.amz', 'w') as newfile:
        for line in striped:
            if 'meta' in line:
                pass
            else:
                newfile.write(line)
    newin = open('newfile.amz', 'r')
    print newin.read()

#for line in prop:
#    line2 = line.strip( )
#    print line2
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
