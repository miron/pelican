Title: Hints to start Processes in Background (zsh) and logging out
Date: 2007-04-30
Tags: linux, terminal, zsh, jobs, background, logout
Category: Linux
Summary: nohupidihup

Start the process with nohup:

`nohup someprocess`

When it is allready started, type disown. (alias disown="kill -CONT %1; disown" or alias disown="bg; disown" to not to have to kill or bg manualy)

Start the process with &amp;! which automatically disowns the process.

Start the program in the background, either with

program &amp;  or ^Z bg, then type kill -9 $$ (this one closes also the actual shell).

