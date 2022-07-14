Title: Disable shift-backspace logout in XGL and enable AltGr
Date: 2006-10-04
Tags: linux, XGL, altgr, logout
Category: Linux
Summary: so many fingers, so many keys

It drove me mad that i logged <font>always</font> out from <font>XGL</font> after pressing <font>accidentally</font> shift-backspace.

You have to type:

<code>xmodmap -e "keycode 22 = BackSpace BackSpace" </code>

after your Window Manager started (that would be beryl  in my case).

And because my <font>AltGr</font> key <font>didn't</font> worked too i first looked at the <font>keycode</font> with <font>xev</font> which was 113.

Then a little <font>lookup</font> how the key is occupied:

<code>xmodmap -pk</code>

And <font>finally</font> to make the key work again:
<font>
<code>xmodmap -e 'keycode 113 = Mode_switch'</code></font>

And because i am a lazy person and dont want to type that over and over again to load it on startup i put both in my ~/.Xmodmap file:

<code>echo 'keycode 22 = BackSpace BackSpace' &gt;&gt; ~/.Xmodmap</code>
<code>echo 'keycode 113 = Mode_switch' &gt;&gt; ~/.Xmodmap</code>
