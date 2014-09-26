#!/usr/bin/env python
# amzfetch.py
# Description: Tool for downloading Amazon MP3s using a .amz file.
# Version: 0.00.00
# Last Updated: Fri 26 Sep 2014 11:02:38 AM PDT 

"""amzfetch.py - A tool for downloading Amazon MP3s as detailed in a .amz file. 
   
"""
 
import os
import sys
import argparse
 
def main(arguments):
 
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help = "Input file",
                        type = argparse.FileType('r'))
 
    args = parser.parse_args(arguments)
    
    print args
script, input_file = sys.argv
in_file = open(input_file)
print in_file.read()
	
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
