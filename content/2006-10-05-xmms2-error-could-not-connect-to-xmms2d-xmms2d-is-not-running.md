Title: xmms2: Could not connect to xmms2d: xmms2d is not running.
Date: 2006-10-05
Tags: audio, linux, xmms2, error
Category: Linux
Summary: client running away from daemon

I came around this error, it means that the daemon and the client don't run in the same directory.

<font>xmms2d -i unix:///tmp/apantutarinte</font>
<font>export XMMS_PATH=unix:///tmp/apantutarinte xmms2 list</font>

helps alot.

Edit: this is no more necessary with DrGonzo release.
