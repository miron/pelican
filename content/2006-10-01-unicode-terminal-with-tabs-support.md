Title: Unicode terminal with tabs support, clickable url's
Date: 2006-10-01
Category: Linux
Tags: linux, terminal, unicode, tabs, linux
Summary: how many terminals are there? many

After some time of search i found rxvt-unicode.
With compiled in perl support you can start it with:

<font>urxvt -pe tabbed</font>

or add:

<font>URxvt.perl-ext-common: default,tabbed </font>

to your ~/.Xdefaults

^shift cursor-left or cursor-right switches tabs,
^shift cursor-down creates new tab.

To leftclick an url in the terminal and open it for example in elinks, add:

URxvt.urlLauncher: elinks
URxvt.matcher.button: 1

Then start with urxvt -pe matcher

or simply add:

<font>URxvt.perl-ext-common: matcher</font>

to your ~/.Xdefaults (you can combine it with the tabs entry).

More useful hints:

man urxvtperl