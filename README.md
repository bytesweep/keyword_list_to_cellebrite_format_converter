# Keyword List to Cellebrite Format Converter
This simple tool is designed as a drag and drop converter. If you are working a digital forensic investigation and you are working with a keyword list many tools can accept a keyword list with one word per line. 
This tool can accept that keyword list and quickly convert that list into a format that can be easily used in the global search bar found in the Cellebrite UFDR / Physical Analyzer family of tools.

INSTRUCTIONS FOR USE:

To use this tool simply drag and drop the keyword list you wish to convert on to the script. 

The script will convert the list and save a new file using the same filename of your keyword list and adding "-CELLEBRITE" to the end of it. 

Your original keyword list will not be modified. The contents of the new list will be the same in quality. 

Your new list will show one keyword per line with a ", " after each word. 

If your keywords in your original list have a space this script will interpret them as individual keywords and it will separate them out. 

<i> To Do: Adjust script to handle keywords that contain more than one word per line so "ICE CREAM" is "ICE CREAM" and not "ICE, CREAM"</i>

<b>EXAMPLE:</b>

Original List:

Steak
Chicken
Fish
Bread

Converted List:

Steak, Chicken, Fish, Breah
