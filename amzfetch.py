#!/usr/bin/env python
# amzfetch.py
# Description: Tool for downloading Amazon MP3s using a .amz file.
# Version: 0.00.00
# Last Updated: Fri 26 Sep 2014 10:40:34 PM PDT  
# Leigh Burton, lburton@metacache.net
# Status: it just dumps the input file to console.

"""amzfetch.py - A tool for downloading Amazon MP3s as detailed in a .amz file. 
   
"""
 
import os
import sys
import argparse
 
def main(arguments):

    script, input_file = sys.argv
    in_file = open(input_file)
    prop = in_file.read()

    striped = prop.strip( )
    print striped

#for line in prop:
#    line2 = line.strip( )
#    print line2

    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
