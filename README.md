amzfetch.py
===========

Tool to pull down Amazon MP3s via a .amz (XML) file.

Initial thoughts on script work flow for v0.10.00
------------------------------------

1. User initiates the script
2. User selects input file (.amz)
3. Scripts takes .amz file and strips out the unwanted data entries.
6. Scripts downloads mp3s sequentially

Planned future improvements
---------------------------

1. Improve error handling (currently gives the usual python errors if you don't specify a file when invoking the script, no actual checking to see if its actually a .amz file. (v0.20.00)
2. Get script to display all mp3 pertinents before download, once it has displayed each of the mp3's details allow the user to download mp3s. (v0.30.00)
3. Building on v0.30.00, (most likely using arrays) allow synchronous download of files.(v0.40.00)
4. Allow the script to create the directory structure for your files (Artist/Album/mp3s). (v0.50.00)
5. Integrate Keen.io API to track events through the work flow cycle (open the source file, strip un-needed data, data conversion, get number of mp3s to handle, completion of each of those mp3s). (v0.60.00)
6. All above + complete bug fixes. (v1.00.00)

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
