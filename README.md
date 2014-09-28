amzfetch.py
===========

Tool to pull down Amazon MP3s via a .amz (XML) file.

amzfetch.py v0.10.00
------------------------------------

User invokes the script as follows:
    python amzfetch.py pathto.amz
    
This version is very basic, but it DOES work, (it has been tested multiple times via actual .amz files from amazon digital store.
There are multiple improvements I can probably do even on this code alone (the download handling for instance, I already know of a more elegent way of doing that, these kind of changes will be integrated into v0.30.00 code base, I want to get error handling throughout the code working correctly before I make large changes to the functionality code.

Planned future improvements
---------------------------

* Improve error handling (currently gives the usual python errors if you don't specify a file when invoking the script, no actual checking to see if its actually a .amz file. (v0.20.00)
* Get script to display all mp3 pertinents before download, once it has displayed each of the mp3's details allow the user to download mp3s. (v0.30.00)
* Building on v0.30.00, (most likely using arrays) allow synchronous download of files.(v0.40.00)
* Allow the script to create the directory structure for your files (Artist/Album/mp3s). (v0.50.00)
* Integrate Keen.io API to track events through the work flow cycle (open the source file, strip unneeded data, data conversion, get number of mp3s to handle, completion of each of those mp3s). (v0.60.00)
* All above + complete bug fixes. (v1.00.00)

Initial thoughts on GUI
-----------------------

1. Command line
2. GUI framework (pyGTK, pyQT, Tkinter)
3. Web framework (Flask or Tornado)

Information required from data schema in .amz
---------------------------------------------

```
<track>
	<location>
	<creator>
	<album>
	<title>
</track>
```
Each mp3 is included in its own unique track 'bucket'

other data items currently extraneous

Recommended JSON format (Potentially Defunct)
---------------------------------------------

```
{"tracks":[
    {"location":"###", "creator":"###", "album":"###", "title":"###"},
	{"location":"###", "creator":"###", "album":"###", "title":"###"}
]}
```
