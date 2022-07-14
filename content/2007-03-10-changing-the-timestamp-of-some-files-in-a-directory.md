Title: Changing the timestamp of some files in a directory
Date: 2007-03-10
Category: Linux
Tags: linux, terminal, shell, zsh, touch
Summary: do you remember the touch command?

Lets assume i want to change the timestamp of all pdf-files in a directory to now, this is the way to go (zsh):<br /><br />for file in *.pdf; touch ${file}<br /><br />
