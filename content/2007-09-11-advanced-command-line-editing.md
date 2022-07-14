Title: Advanced Command-Line Editing
Category: Linux
Date: 2007-09-11
Tags: terminal, vim
Summary: Lets celebrate my LPIC-2

Today I passed my 117-201 exam and now I play a little bit with the Vi key bindings on Zsh.  
In Bash you can set them with set -o vi, and in Zsh you can set them additionally with setopt vi.  

I want to get to the point of command line editing above the basic  
tab complete and history browsing, searching and minor corrections.  
So I start witch a little example: 

I want to rename a file with the following naming scheme:

`someID_filename.txt to filename.txt`

After my fulminant efficient Vim key combination for table editing, [Efficient table-editing]({filename}2007-06-13-vim-contest-who-finds-the-shortest-possible-solution-of-changing-an-postgre-tab-in-an-array.md/)   
I challenge everybody to find the shortest key combination to fulfill this task.

I start with an self-deprating solution:
First I type:
`mv someID_filname.txt`

Now the count begins:

`<Space><Esc>T_y$$p<Enter>`

This makes a total of 9 characters which i have to store in my brain. As I want
to have my head free for more complicated tasks, of course this has to
be optimized dramatically :)  

Have fun.  
