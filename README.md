amzfetch.py
===========

Tool to pull down Amazon MP3s via a .amz (XML) file.

amzfetch.py v0.20.00
------------------------------------

![alt tag](http://amzfetch.metacache.net/github/v0.20.00.png)

New GUI implemented via TkInter, certain information is outputted to console still, eventually I will add another window that will be used as an in-app console output.

User invokes the script as follows:
    python amzfetch.py pathto.amz
    
This version is very basic, but it DOES work, (it has been tested multiple times via actual .amz files from amazon digital store.

There are multiple improvements I can probably do even on this code alone (the download handling for instance, I already know of a more elegent way of doing that, these kind of changes will be integrated into v0.30.00 code base.

v0.20.00 KNOWN ISSUES
---------------------

* The URLs in the .amz file expire after a certain amount of time, if you try to use an expired .amz file the app will error.
* I need to impliment some form of file detection to make sure it only runs when fed the correct type of file (.amz)

Planned future improvements (versions rough guide)
--------------------------------------------------

* Building on v0.20.00, (most likely using lists in some manner) allow synchronous download of files.(v0.30.00)
* Allow the script to create the directory structure for your files (Artist/Album/mp3s). (v0.40.00)
* Integrate Keen.io API to track events through the work flow cycle (open the source file, Gather needed data on tracks & total % of tracks, completion of each of those mp3s). (v0.50.00)
* All above + complete bug fixes. (v1.00.00)

Thoughts on improving GUI
-----------------------

1. allow selection of .amz file from GUI, not command line
2. allow limited selection of specific files for download (selective downloads)
3. allow user to select location for downloaded files, toggle creation of folders or simple download location.

