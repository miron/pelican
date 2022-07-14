Title: Insert Current Date In Vim
Date: 2007-08-27
Category: Vim
Tags: linux, vim, insert, date
Summary: I don't know how to do that in vscode


If you write a ToDo list or a schedule in vim, you probably want to insert the current date or the date after one week from now. 
Here is how to do it:  

`:r !date`

or to add one week to the current Date:  

`:r !date -d "today 1 week"`

enjoy :)


