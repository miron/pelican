Title: zsh and the stat command
Date: 2007-06-22
Tags: terminal, zsh, stat, time
Category: Linux
Summary: there was a time when people knew their file systems

It works a litte bit different than in bash:

`stat -g some_file`

Shows the times in GMT

`stat -s some_file`

Shows the times in local time zone

You can find more about zsh's stat with `man zshmodules` under zsh/stat
