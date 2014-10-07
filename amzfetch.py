#!/usr/bin/env python
# amzfetch.py
# Description: Tool for downloading Amazon MP3s using a .amz file.
# Version: 0.25.00
# Last Updated: Mon 06 Oct 2014 10:43:07 PM PDT 
# Leigh Burton, lburton@metacache.net
# Status: Full Re-write in process, to allow in-app loading of files.
 
import os
import sys
import urllib2
from xml.dom import minidom
from Tkinter import *
from tkFileDialog import askopenfilename
from tkFileDialog import askdirectory


toolv = 'v0.25.00'

def main(arguments):
    
    filename = ''
    itemtotal = ''
    
    # function to kill the open windows.
    def allquit():
        console.destroy()
        root.destroy()
    
    # Function that downloads files.
    def urldl():
        with open(main.filename, 'r') as input_file:
            xmldoc = minidom.parse(input_file)
            itemloc = xmldoc.getElementsByTagName('location')
            itemtitle = xmldoc.getElementsByTagName('title')
            itemtnum = xmldoc.getElementsByTagName('trackNum')
            itemcreator = xmldoc.getElementsByTagName('creator')
            itemalbum = xmldoc.getElementsByTagName('album')
        itemtotal = len(itemloc)
        
        console.update()
        itemfoo = 0
        downloc = askdirectory()
        if downloc == '':
            print ''
        else:
            label = Label(console, text='Starting Download of ' + str(itemtotal) + ' songs', fg="red").grid(sticky=W)
            label = Label(console, text='Files will be in ' + downloc, fg="red").grid(sticky=W)
            console.update()
            while itemfoo != itemtotal:
                mp3url = itemloc[itemfoo].childNodes[0].nodeValue
                mp3title = itemtitle[itemfoo + 1].childNodes[0].nodeValue
                mp3tnum = itemtnum[itemfoo].childNodes[0].nodeValue
                mp3creator = itemcreator[itemfoo].childNodes[0].nodeValue
                mp3album = itemalbum[itemfoo].childNodes[0].nodeValue
                response = urllib2.urlopen(mp3url)
                mp3out = response.read()
                with open(downloc + '/' + mp3tnum + ' ' + mp3title + '.mp3', 'wb') as newfile:
                    newfile.write(mp3out)
                    newfile.close()
                itemfoo = itemfoo + 1
                label = Label(console, text=unicode(mp3title).encode("utf-8") + ' by ' + unicode(mp3creator).encode("utf-8") + ' Downloaded').grid(sticky=W)
                console.update()
            label = Label(console, text='All Items Downloaded', fg="red").grid(sticky=W)
            console.update()
    
    # function to select the amzfile.
    def openamz():
        main.filename = askopenfilename()
        if main.filename == '':
            print ''
        else:
            with open(main.filename, 'r') as input_file:
                xmldoc = minidom.parse(input_file)
                itemloc = xmldoc.getElementsByTagName('location')
                itemtitle = xmldoc.getElementsByTagName('title')
                itemtnum = xmldoc.getElementsByTagName('trackNum')
                itemcreator = xmldoc.getElementsByTagName('creator')
                itemalbum = xmldoc.getElementsByTagName('album')
     
            itemtotal = len(itemloc)
            itemfoo = 0
            while itemfoo != itemtotal:
                mp3url = itemloc[itemfoo].childNodes[0].nodeValue
                mp3title = itemtitle[itemfoo + 1].childNodes[0].nodeValue
                mp3tnum = itemtnum[itemfoo].childNodes[0].nodeValue
                mp3creator = itemcreator[itemfoo].childNodes[0].nodeValue
                mp3album = itemalbum[itemfoo].childNodes[0].nodeValue
                itemfoo = itemfoo + 1
                lartist = Label(root, text='Artist: ', fg="#357EC7").grid(row=itemfoo, column=0, sticky=E)
                dartist = Label(root, text=unicode(mp3creator).encode("utf-8")).grid(row=itemfoo, column=1, sticky=W)
                ltitle = Label(root, text='Song: ', fg="#357EC7").grid(row=itemfoo, column=2, sticky=E)
                dtitle = Label(root, text='(' + str(mp3tnum) + ') ' + unicode(mp3title).encode("utf-8")).grid(row=itemfoo, column=3, sticky=W)
                lalbum = Label(root, text='Album: ', fg="#357EC7").grid(row=itemfoo, column=4, sticky=E)
                dalbum = Label(root, text=str(mp3album)).grid(row=itemfoo, column=5, sticky=W)
            itemfoo = itemfoo + 1
            dlurl = Button(root, text='Download Songs', command=urldl).grid(row=0, column=1, sticky=W)
            label = Label(console, text=main.filename + ' Opened', fg="#357EC7").grid(sticky=W)
        
            root.update()

    #test function.    
    def test():
        label = Label(console, text=str(main.filename), fg="#357EC7").grid(sticky=W)
        console.update()
    


    
    ##########################
    # Initial App stuff here #
    ##########################
    
    # Set up windows.
    console = Tk()
    root = Tk()
    root.geometry('+100+100')
    console.minsize(300,200)
    console.geometry('+100+300')
    # Set the window titles.
    console.title('amzfetch.py :: Console Output')
    root.title('amzfetch.py ' + toolv + ' :: ')
    
    # Create the initial widgets (Quit, Open).
    dlquit = Button(root, text='Quit', command=allquit).grid(row=0, column=0, sticky=E)
    dlopen = Button(root, text='Open', command=openamz).grid(row=0, column=1, sticky=W)
    # Create initial windows.
    root.mainloop()
    console.mainloop()
    
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
