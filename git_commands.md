# Summary of git commands

Git has a **staging area** in which it stores files with changes you want to save that haven't been saved yet, you can add more files to this area or take them out as often as you want, but once you commit them, you cannot make further changes

* git add filename(, filename, ...): put files in the staging area
* git commit( -m "msg"): commit everything in the staging area
* git status: shows you which files are in staging area, or which files have changes that haven't yet been put there.
* git diff:
    * arguments
    -r 
	* contents (could also be added behind arguments)
	+ filename:
   	  compare the file as it currently is to what you last saved
    + directory:
   	  show you the changes to the files in some directory.
    + without any filenames will show you all the changes in your repository


    * examples:

		diff --git a/report.txt b/report.txt                       diff --git: the command used to produce the output
		index e713b17..4c0742a 100644							   a and b are placeholders mearning "the first version" and "the second version"
		--- a/report.txt       									   wherein lines being removed are prefixed with - and lines being added are prefixed with +
		+++ b/report.txt                  						   A line starting with @@ that tells where the changes are being made
		@@ -22,3 +22,4 @@ Date,Tooth							   The pairs of numbers are start line and number of lines. This diff output indicates changes starting at line 1, with 5 lines where there were once 4.
		2017-08-13,incisor										   Lines that haven't changed are sometimes shown before
		2017-08-13,wisdom										   and after the ones that have in order to give context, 	
		2017-09-07,molar										   but no +/- in front of them			 	   
		+2017-11-01,bicuspid	           						   A line-by-line listing of the changes with - showing deletions and + showing additions


* 