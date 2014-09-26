amzfetch
========

Tool to pull down Amazon MP3s via a .amz file.

Initial thoughts on script workflow
===================================

1. User initiates the script
2. User selects input file (.amz)
3. Scripts takes .amz file and converts data to universal json format
4. Script now displays mp3s associated with the .amz file & their pertinents
5. User selects which mp3s they want to download, (all, specific mp3s) as well as number of concurrent downloads
6. User starts the script downloading the mp3s

Initial thoughts on improvement from original workflow
======================================================

1. Allow the script to create the directory structure for your files (Artist/Album/mp3s)

Initial thoughts on GUI
=======================

1. Command line
2. GUI framework (pyGTK, pyQT, Tkinter)
3. Web framework (Flask or Tornado)

Information required from data schema in .amz
=============================================

1. location
2. creator
3. album
4. title

