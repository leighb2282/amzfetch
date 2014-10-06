#!/usr/bin/env python
# amzfetch.py
# Description: Tool for downloading Amazon MP3s using a .amz file.
# Version: 0.24.00
# Last Updated: Sun 05 Oct 2014 07:40:44 PM PDT    
# Leigh Burton, lburton@metacache.net
# Status: GUI via TkInter, Displays list of MP3s in the .amz file, user can then download them. 
 
import os
import sys
import argparse
import urllib2
from xml.dom import minidom
from Tkinter import *
from time import strftime


toolv = 'v0.24.00'
logloc = 'amzfetch.log'


def main(arguments):
    console = Tk()
    console.title('Console Output')
    
    def allquit():
        conlog = open(logloc, 'a+')
        conlog.write(strftime("%Y-%m-%d %H:%M:%S") + ' ' + args.infile + ' Closed.\n')
        conlog.close()
        console.destroy()
        root.destroy()
        
    root = Tk()
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help = "Input file (.amz)")
    args = parser.parse_args(arguments)

    with open(args.infile, 'r') as input_file:
        xmldoc = minidom.parse(input_file)
        itemloc = xmldoc.getElementsByTagName('location')
        itemtitle = xmldoc.getElementsByTagName('title')
        itemtnum = xmldoc.getElementsByTagName('trackNum')
        itemcreator = xmldoc.getElementsByTagName('creator')
        itemalbum = xmldoc.getElementsByTagName('album')
     
    itemtotal = len(itemloc)
    itemfoo = 0
    label = Label(console, text=str(itemtotal) + ' songs in ' + args.infile, fg="#357EC7").grid(sticky=W)
    
    conlog = open(logloc, 'a+')
    conlog.write(strftime("%Y-%m-%d %H:%M:%S") + ' ' + args.infile + ' Opened. ' + str(itemtotal) + ' songs in ' + args.infile + '\n')
    conlog.close()
        
    def urldl():
        itemfoo = 0
        label = Label(console, text='Starting Download of ' + str(itemtotal) + ' songs', fg="red").grid(sticky=W)
        
        conlog = open(logloc, 'a+')
        conlog.write(strftime("%Y-%m-%d %H:%M:%S") + ' ' + args.infile + ' Starting Download of ' + str(itemtotal) + ' songs\n')
        conlog.close()
        
        console.update()
        while itemfoo != itemtotal:
            
            mp3url = itemloc[itemfoo].childNodes[0].nodeValue
            mp3title = itemtitle[itemfoo + 1].childNodes[0].nodeValue
            mp3tnum = itemtnum[itemfoo].childNodes[0].nodeValue
            mp3creator = itemcreator[itemfoo].childNodes[0].nodeValue
            mp3album = itemalbum[itemfoo].childNodes[0].nodeValue
            response = urllib2.urlopen(mp3url)
            mp3out = response.read()
            with open(mp3tnum + ' ' + mp3title + '.mp3', 'wb') as newfile:
                newfile.write(mp3out)
                newfile.close()
            label = Label(console, text=str(mp3title) + ' by ' + str(mp3creator) + ' Downloaded').grid(sticky=W)
            console.update()
            
            conlog = open(logloc, 'a+')
            conlog.write(strftime("%Y-%m-%d %H:%M:%S") + ' ' + args.infile + ' ' + str(mp3title) + ' by ' + str(mp3creator) + ' Downloaded\n')
            conlog.close()
            
            itemfoo = itemfoo + 1
        label = Label(console, text='All Items Downloaded', fg="red").grid(sticky=W)
        
        conlog = open(logloc, 'a+')
        conlog.write(strftime("%Y-%m-%d %H:%M:%S") + ' ' + args.infile + ' All Items Downloaded\n')
        conlog.close()
        
        console.update()
        
    while itemfoo != itemtotal:
        mp3url = itemloc[itemfoo].childNodes[0].nodeValue
        mp3title = itemtitle[itemfoo + 1].childNodes[0].nodeValue
        mp3tnum = itemtnum[itemfoo].childNodes[0].nodeValue
        mp3creator = itemcreator[itemfoo].childNodes[0].nodeValue
        mp3album = itemalbum[itemfoo].childNodes[0].nodeValue
        
        lartist = Label(root, text='Artist: ', fg="#357EC7").grid(row=itemfoo, column=0, sticky=E)
        ltitle = Label(root, text='Song: ', fg="#357EC7").grid(row=itemfoo, column=2, sticky=E)
        lalbum = Label(root, text='Album: ', fg="#357EC7").grid(row=itemfoo, column=4, sticky=E)
        dartist = Label(root, text=str(mp3creator)).grid(row=itemfoo, column=1, sticky=W)
        dtitle = Label(root, text='(' + str(mp3tnum) + ') ' + str(mp3title)).grid(row=itemfoo, column=3, sticky=W)
        dalbum = Label(root, text=str(mp3album)).grid(row=itemfoo, column=5, sticky=W)
        itemfoo = itemfoo + 1
    
    dlquit = Button(root, text='Quit', command=allquit).grid(row=itemfoo, column=0, sticky=E)
    dlurl = Button(root, text='Download Songs', command=urldl).grid(row=itemfoo, column=1, sticky=E)
    root.title('amzfetch.py ' + toolv + ' :: ' + args.infile)
    root.mainloop()
    
    console.mainloop()
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
