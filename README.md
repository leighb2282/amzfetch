amzfetch.py
===========

Tool to pull down Amazon MP3s via a .amz (XML) file.

Requires TkInter, can be installed via your Distro's package manager)

amzfetch.py v0.25.00
------------------------------------

![alt tag](http://leigh-burton.com/code/amzfetch/v0.25.00.png)

New GUI implemented via TkInter, with information pertaining to the download of mp3s now outputting to a console window.

User invokes the script as follows (no arguments required):
    python amzfetch.py
    
User can select an .amz for anywhere on the filesystem, once they have decided to download the MP3s from the .amz file they can choose a location to have the mp3s downloaded to.

There are multiple improvements I can probably do even on this code alone (the download handling for instance, I already know of a more elegent way of doing that, these kind of changes will be integrated into v0.30.00 code base.

v0.25.00 KNOWN ISSUES
---------------------

* If you close the console window before using the quit button on the main window it will error.
* The URLs in the .amz file expire after a certain amount of time, if you try to use an expired .amz file the app will error.
* I need to impliment some form of file detection to make sure it only runs when fed the correct type of file (.amz) as amzfetch will error if a non.amz file is selected.

Planned future improvements
---------------------------

* Allow limited selection of specific files for download (selective downloads)
* Add an additional download option which automatically downloads the mp3s to a downloads folder in the scripts location versus choosing a location.
* Improve file input handling (limit files in the file dialog to just .amz files, stop showing all files - including hiddne folders/files)
* Allow one instance of the tool to download multiple .amz files - currently to feed it another .amz file you will need to close and re-open the tool.
* fix the above error where if you close the console window before using the quit button on the main window it will error.
* Allow synchronous download of files.
* Integrate Keen.io API to track events through the work flow cycle (open the source file, Gather needed data on tracks & total % of tracks, completion of each of those mp3s).
* All above improvements + Known issues + complete bug fixes. (v1.00.00)

