Title: Fast search and replace in vim
Date: 2007-06-11
Category: Vim
Tags: vim, search, replace
Summary: The fastest editor in the world

Today a fast search and replace technique in vim,  I copy an example direct from the vimhelp:

	
	/foo<CR>        find "foo"
	c//e            change until end of match
	bar<Esc>        type replacement
	//<CR>          go to start of next match
	c//e            change until end of match
	beep<Esc>       type another replacement
	etc.
