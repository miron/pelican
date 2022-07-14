Title: zsh and the stat command
Date: 2007-06-22
Tags: terminal, zsh, stat, time
Category: Linux

It works a litte bit different than in bash:

stat -g some_file

Shows the times in GMT

stat -s some_file

Shows the times in local time zone

More about zsh's stat you can find with man zshmodules under zsh/stat
