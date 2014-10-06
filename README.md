amzfetch.py
===========

Tool to pull down Amazon MP3s via a .amz (XML) file.

Requires TkInter, can be installed via your Distro's package manager)

amzfetch.py v0.24.00
------------------------------------

![alt tag](http://amzfetch.metacache.net/github/v0.23.00.png)

New GUI implemented via TkInter, with information pertaining to the download of mp3s now outputting to a console window alongside logging to a log file (which you can set in the logloc variable at the top of the source.

User invokes the script as follows:
    python amzfetch.py pathto.amz
    
This version is very basic, but it DOES work, (it has been tested multiple times via actual .amz files from amazon digital store.

There are multiple improvements I can probably do even on this code alone (the download handling for instance, I already know of a more elegent way of doing that, these kind of changes will be integrated into v0.30.00 code base.

v0.24.00 KNOWN ISSUES
---------------------

* The URLs in the .amz file expire after a certain amount of time, if you try to use an expired .amz file the app will error.
* I need to impliment some form of file detection to make sure it only runs when fed the correct type of file (.amz)

Planned future improvements
---------------------------

* Allow selection of .amz file from GUI, not command line
* Allow limited selection of specific files for download (selective downloads)
* Allow user to select location for downloaded files, toggle creation of folders or simple download location.
* Allow synchronous download of files.
* Allow the script to create the directory structure for your files (Artist/Album/mp3s).
* Integrate Keen.io API to track events through the work flow cycle (open the source file, Gather needed data on tracks & total % of tracks, completion of each of those mp3s).
* All above + complete bug fixes. (v1.00.00)

Thoughts on improving GUI
-----------------------

1. allow selection of .amz file from GUI, not command line
2. allow limited selection of specific files for download (selective downloads)
3. allow user to select location for downloaded files, toggle creation of folders or simple download location.

