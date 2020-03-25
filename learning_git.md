# Summary of git commands

Git has a **staging area** in which it stores files with changes you want to save that haven't been saved yet, you can add more files to this area or take them out as often as you want, but once you commit them, you cannot make further changes

* git add filename(, filename, ...): put files in the staging area
* git commit: commit everything in the staging area as one unit: when you want to undo changes to a project, you undo all of a commit or none of it
    * arguments
    	* \-m "msg": leave log message
    	* \-\-amend -m "new msg": you want to change the msg you mistyped.
* git log: view the log of the history
	* contents (could also be added behind arguments)
		* file path:  shows changes made to that file
    	* directory path: when files were added or deleted in that directory, rather than when the contents of the directory's files were changed
    	* without any filenames will show you all the changes as example in your repository
	* examples:
		contents										           |		   Explanation
        -----------------------------------------------------------| ----------------------------------------------------------------------------------
        commit 0430705487381195993bac9c21512ccfb511056d		|		unique id: hash
		Author: Rep Loop <repl@datacamp.com>		|
		Date:   Wed Sep 20 13:42:26 2017 +0000		|

    		Added year to report title.		|

    	Press the space bar to go down a page or the 'q' key to quit.

* git status: shows you which files are in staging area, or which files have changes that haven't yet been put there
* git diff:
    * arguments
    	* \-r: \-r means comparing to a particular revision; HEAD is the shortcut for the most recent commit
	* contents (could also be added behind arguments)
		* file path: compare the file as it currently is to what you last saved
    	* directory path: show you the changes to the files in some directory.
    	* without any filenames will show you all the changes in your repository
    * examples:

        contents										           |		   Explanation
        -----------------------------------------------------------| ----------------------------------------------------------------------------------
		diff --git a/report.txt b/report.txt            |          diff --git: the command used to produce the output
		index e713b17..4c0742a 100644					|		   a and b are placeholders mearning "the first version" and "the second version"
		--- a/report.txt       							 |		   wherein lines being removed are prefixed with - and lines being added are prefixed with +
		+++ b/report.txt                  				|		   A line starting with @@ that tells where the changes are being made
		@@ -22,3 +22,4 @@ Date,Tooth					|		   The pairs of numbers are start line and number of lines. This diff output indicates changes starting at line 1, with 5 lines where there were once 4
		2017-08-13,incisor								|		   Lines that haven't changed are sometimes shown before
		2017-08-13,wisdom								|		   and after the ones that have in order to give context, 	
		2017-09-07,molar								|		   but no +/- in front of them			 	   
		+2017-11-01,bicuspid	           				|		   A line-by-line listing of the changes with - showing deletions and + showing additions

# How git store information 
![store information: copyright of datacamp](images/store.png)
