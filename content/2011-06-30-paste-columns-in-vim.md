Title: Paste columns in vim
Date: 2011-06-30
Category: Vim
Tags: linux, terminal, vim
Slug: Vim as Excel alternative
Summary: Multi columns in Vim

Finaly, after years of searching, i found an almost perfect solution.  

I sometimes like to write lists in vim which have 2 columns, or sometimes you copy something from the web and want to have it in two columns.  

First you have the text in one column, then you go to the first row you want to have in the second column.  
Then you enter visual blockmode with Ctrl-V, then you press $, as not all rows will be the same length.  
Then scroll down with j and select all items you want to have in the second column.  
Then yank with y, or delete with x, go to the first corner of the second row and paste with p.
