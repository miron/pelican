Title: Some handy vim commands
Date: 2007-06-20
Category: Vim
Tags: vim, handy, reference
Summary: Years of practice, still no memorization





I want to have them in one place so i write them down here:

<span style="background-color:#ddffdd;color:#000000;font-weight:bold;"><tt>:g/^#/d</tt></span> Delete all lines that begins with #

<span style="background-color:#ddffdd;color:#000000;font-weight:bold;"><tt>:g/^$/d</tt></span> Delete all lines that are empty and contain no tabs

<span style="background-color:#ddffdd;color:#000000;font-weight:bold;"><tt>:g/^\s*$/d</tt></span> Delete all lines that are empty

<span style="background-color:#ddffdd;color:#000000;font-weight:bold;"><tt>:%s/$/{ctrl-V}{CR}/g</tt></span> Inserts blank line between lines <span style="background-color:#ddffdd;color:#000000;font-weight:bold;"></span>

<span style="background-color:#ddffdd;color:#000000;font-weight:bold;"><tt>:%s/{TAB}*$//</tt></span> Strip tabs at end of line

<span style="background-color:#ddffdd;color:#000000;font-weight:bold;"><tt>:g/&lt;pattern&gt;/t$</tt></span> Copy every line which matches pattern to the end of  the file

<span style="background-color:#ddffdd;color:#000000;font-weight:bold;"><tt>5&gt;&gt;</tt></span> indent 5 lines from line where cursor stands, handy because you dont need to enter visual mode

And yes, {ctrl-V},{CR} and {TAB} means you have to press it, not to type it.

Credits go to <a href="http://gentoo-wiki.com/HOWTO_VIM" title="vim howto" target="_blank">gentoo- wiki.com</a>, <a href="http://www.yolinux.com/TUTORIALS/LinuxTutorialAdvanced_vi.html" title="vim tips" target="_blank">yolinux.com</a> and <a href="http://www.int-x.org/doku.php?id=tipps:vimtipps" title="vim tips" target="_blank">www.int-x.org</a>