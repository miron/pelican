Title: Copy and Paste from Web to Vim
Date: 2007-01-12
Tags: linux, terminal, vim, copy, paste, web
Category: Vim
Summary: vim meets the web

Normaly autoindent is enabled, so it looks horrible when you paste something from an webpage into vim.
So before you do this, type:

<em>:set paste</em>

Then in insert mode you can paste as usual with Shift+Ins.

Edit: Caution! This disables mapping in insert mode and in command-line mode and abbreviations !!

So to disable it again type :set paste! or :set nopaste.

Another method and much faster is to type:

:a

paste the code and hit CTRL-C.

Hint: Hit enter before CTRL-C if you did not cut the last \n to not to miss the last line.

What annoys me too sometimes is the auto-commenting of vim, you can disable it with:

:set com=f://

But this only works when you type it in command mode. To set it permanently, you have to write this in your ~/.vimrc :

set fo-=r
