Title: Browsing the Rails API with elinks using rails.vim
Date: 2007-06-29
Category: Vim
Tags: rubyOnRails, vim, rails, elinks
Summary: I'm using elinks to browse the Rails API

Add this line to your .vimrc

`command -bar -nargs=1 OpenURL :!elinks <args>


