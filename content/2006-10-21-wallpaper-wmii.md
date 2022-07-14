Title: HowTo set the wallpaper in wmii
Date: 2006-10-21
Tags: linux, wmii, feh, background, image, wallpaper
Category: Linux
Summary: pretty

This took me a little bit, so i write it down.

In ~/.wmii-3.5/wmiirc, replace the following line:<em>			</em>

<em><code>xsetroot -solid '#0b1014'</code>
</em>with a command to set the background image, such as<em>			</em>

<em><code>eval `cat $HOME/.fehbg` &amp;</code>
</em>(requires <a href="http://linuxbrit.co.uk/feh/"> feh</a>)

Now i don't have to bother anymore with the configfile,

feh --bg-center ~/path/to/image sets the backgroundimage

and after a reboot the last shown picture is set.
