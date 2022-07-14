Title: Moving Files containing a specific string
Date: 2006-12-25
Tags: linux, terminal, find, mv, move
CAtegory: Linux
Summary: sometimes commands are longer than the content itself

So far i found this solution to move files from current directory to a given one:  
`find . -type f -iname '*string*' -exec mv {} /dir \;`  	
If someone knows something shorter, please let me know.  
