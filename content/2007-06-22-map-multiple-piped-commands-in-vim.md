Title: Map multiple piped commands in vim
Date: 2007-06-22
Category: Vim
Tags: ruby, vim, map, pipe, multiple
Summary: I seldom map, but I do map multiple commands in vim

If you want to map multiple commands in vim do it like this:

nmap <F1> :w\|!ruby %>;CR>

imap <F1> <Esc>:w\|!ruby %<CR>

This writes the actual file to disk and  evaluates it through the ruby interpreter when you hit the F1-key.

Alternatively you can do a:

:nmap &lt;F1&gt; :w\|rubyf %&lt;CR&gt;   (no space after the %)

:imap &lt;F1&gt; &lt;Esc&gt;:w\|rubyf %&lt;CR&gt;

which should be faster, condition is you have to build vim with ruby support,  but sometimes i get no results with this , vim gets crashed or does not respond anymore to me...

This mappings work both in insert- and command-mode
