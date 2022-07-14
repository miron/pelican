Title: Howto rebind keys in weechat
Date: 2007-05-05
Tags: irc, terminal, weechat, irc, rebind, keys
Category: Linux
Summary: weechat r00l3z


I found it difficult to grab allways to the F6 and F7 keys to switch buffers, so i remaped them to ctrl-P and ctrl-N. Here is how:

/key ctrl-N /buffer +1

/key ctrl-P /buffer -1

Because my Alt-K key is mapped in dwm to switch windows, i get keycodes in weechat witch /key call grab_key, and press then the key i need the code for.

dont forget to /save.
