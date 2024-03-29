Title: Transparent Console-Programs For Linux I Use.
Date: 2006-10-18
Tags: irc, linux, myself, terminal, transparency, transparent, console, curses, 
Category: Linux
Summary: my lifes work is invisible

So far my favorite transparent consoleprograms are:

<a href="http://www.ibiblio.org/mc/" title="midnight commander" target="_blank"><b>midnight commander:</b></a>

Just start it like this in a transparent terminal:

mc -b

Full credit goes to the ingenious <a href="http://tamihania.wordpress.com/" title="tamihania" target="_blank">tami</a>, she was kind enough to share this fabulous hint. Have a look at her site, she has also some very beautiful screenshots and more useful tips here: <a href="http://tamilinux.wordpress.com/2007/02/16/fvwm-crystal-feat-patagonie/" title="tamihania" target="_blank">http://tamilinux.wordpress.com/2007/02/16/fvwm-crystal-feat-patagonie/</a>
<strike></strike>

<b><a href="http://www.ninjam.com/" title="Ninjam" target="_blank">ninjam:</a></b>

A realtime music collaboration software

edit cursesclient/cursesclient.cpp:

start_color();

use_default_colors();    &lt;-- add this line after the existing start_color();

init_pair(1, COLOR_WHITE, COLOR_BLUE); // normal status lines

<b><a href="http://www.jdkoftinoff.com/main/Free_Projects/Drum_Synth_For_Linux/" title="Drum Synth for the console" target="_blank">jdkdrum:</a> </b>

A command-line drummachine, reads simple ascii-patterns from stdin. you can also start it in interactive mode.

<a href="http://www.raggle.org/" title="Raggle " target="_blank"><b>raggle:</b></a>

A console RSS aggregator, written in <a href="http://www.ruby-lang.org/">Ruby </a>. Oh yes, did i mention the vi-like navigation ? Then i do it now :)

in your ~/.raggle/config.rb

do a %s/Ncurses::COLOR_BLACK/-1/g

well almost, i swapped one palettepair from the defaultconfig, and now its nearly perfect :)

I also set 'browser' to firefox (i know, elinks should be here :)) so change that to your liking in my <a href="http://princ3.files.wordpress.com/2007/03/config.txt" target="_blank" id="file-link-50" title="Transparent Raggle"> 			config.rb</a> (change *.txt to *.rb)

<b><a href="http://opensource.hld.ca/trac.cgi/wiki/CurseTheWeather" title="CurseTheWeather" target="_blank">CurseTheWeather:</a></b>

We all love weather, don't we :)

Edit CurseTheWeather-0.3/ctw:

curses.start_color()
curses.use_default_colors() &lt;-- Add this line, you almost know the trick :)
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)

<b><a href="http://thekonst.net/centericq/" title="Multiprotocolmessenger" target="_blank">centericq:</a> </b>

i prefer bitlbee in cooperation with weechat now

<a href="http://elinks.or.cz/" title="Terminal Browser" target="_blank"><b>elinks:</b></a>

console-based browser, you can compile it with spidermonkeysupport, a JavaScript C library,  so it is the only transparent textbrowser  i know which supports googlemail for example :)

You can assign  almost everything to any key. There is a special searchable keybinding manager to not get lost in  the sheer infinite capabilities in the art of keybinding. Of course i modeled mine after vim :) There is also an exmode available, you have to compile it with --enable-exmode as the gentoo-ebuild does not provide this  essential to survive feature, bugreport is underway :)

Some useful settings:

Document/Browsing/Forms/Confirm submission/0

Document/Browsing/Forms/Insert mode/0

Document/Browsing/Images/Display links to images w/o alt/0

<a href="http://software.schmorp.de/pkg/rxvt-unicode.html" title="Unicode Terminal" target="_blank"><b>rxvt-unicode: </b></a>

i start the daemon urxvtd and connect with the following command (i use wmii, transparency did not worked with the perl tabs to me and i dont really need tabs anymore thanks to the wounderful world of screen :)):

<i>urxvtc -tr</i>

See my hints for <a href="http://princ3.wordpress.com/2006/10/01/unicode-terminal-with-tabs-support/" title="Tabs and clickable urls in rxvt-unicode" target="_blank">tabs and clickable links</a>, but be warned, the tabs dont support transparency (wmii/dwm)...

<a href="http://www.afterstep.org/aterm.php" title="Terminal capable of Transparency" target="_blank"><b>aterm:</b></a>

No Unicode, thats why i use rxvt-unicode, but this is for sure the the lightest terminal with transparency supported.

Just start like:

aterm -tr

Or you can add aterm*transparent:true to your ~/.Xdefaults

<a href="http://http://conky.sourceforge.net/" title="Systemmonitor" target="_blank"><b>conky:</b></a>

Systemmonitor, audacious and mpd support, hm maybe i switch to mpd then :)

<a href="http://htop.sourceforge.net/" title="Interactive Process Viewer" target="_blank"><b>htop:</b></a>

interactive process viewer:

kill, nice, incremental search, strace and view processes as tree, show kernelthreads... you can setup meters as bar, text, graph or led, very impressive.

<b><a href="http://gift.sourceforge.net/" title="p2p network" target="_blank">gift</a>/<a href="http://www.nongnu.org/giftcurs/" title="ncurses frontend to p2p" target="_blank">giFTcurs:</a></b>

A OpenFT, Ares, FastTrack, Gnutella, Gnutella2 daemon/client

<b><a href="http://mldonkey.sourceforge.net/Main_Page" title="p2p client" target="_blank">mldonkey</a>/<a href="http://nc110.sourceforge.net/" title="network swiss army knife" target="_blank">netcat:</a></b>

A eDonkey, BitTorrent, Gnutella, Gnutella2, FastTrack, OpenFT daemon. I use it with netcat (ok, mostly with the webinterface, but this is all about minimalistic transparency :)). Netcatlink to the original, of course you can also use telnet, netcat6, gnu-netcat, socat, cryptcat, nmap-ncat, sbd, pncat... go search for the client to your liking :)

<a href="http://www.museek-plus.org/" title="Soulseek Client" target="_blank"><b>museek+/mucous:</b></a>

Soulseekdaemon/client, just start in a transparent terminal. Mucous is ncurses-based and so far one of the most complex ncurses-programs i have seen. right-clickable context menues, chat-room-list, clickable tabs, but of course you can operate this fine peace of software only with your keyboard.

<a href="http://sourceforge.net/projects/nanodc" title="Ncurses-client for DC++" target="_blank"><span style="font-weight:bold;">nanodc:</span></a>

an ncurses-based client to the DC++ network, it uses the  DC++ client core and is therefore fully compatible.

For gentoo users, its in the sunrise overlay

<a href="http://libtorrent.rakshasa.no" title="BitTorrent Client " target="_blank"><b>rtorrent:</b></a>

Enter, tabcomplete to your torrentfile, cursor up to select the torrent, ^S to start downloading, thats it :)

Check this excellent <a href="http://kmandla.wordpress.com/2007/05/02/howto-use-rtorrent-like-a-pro/" title="rtorrent howto" target="_blank">tutorial</a>.

<a href="http://www.vim.org/" title="Console Text Editor " target="_blank"><b>vim:</b></a>

Well what can i write here, it's all about the keysteering, thats another goal of mine, to control my whole desktop vi-like. i already switch, move and resize windows like this (hail to <a href="http://www.suckless.org/wiki/dwm" title="Dynamic Window Manager" target="_blank">dwm</a>), scroll firefox hjkl-like <strike>with the <a href="http://mozilla.dorando.at/" title="Rebind your Keys" target="_blank">keyconfig-plugin</a> and this ingenious <a href="http://www.calmar.ws/firefox/" title="Vi-like keybindings for firefox" target="_blank">keybindings</a></strike> with <a href="http://vimperator.mozdev.org/" title="vim-like firefox extension" target="_blank">
</a>
<p style="font-size:15px;"><a href="http://vimperator.mozdev.org/" title="vim-like firefox extension" target="_blank">vimperator:</a> you like vim, you like firefox ? then this is a must have.</p>
I would wipe out midnight commander if the <a href="http://vim.sourceforge.net/scripts/script.php?script_id=808" title="Total Comander like file exploring in vim" target="_blank">vimcomanderscript</a> wouldn’t be so damn slow, and  <a href="http://vifm.sourceforge.net/" title="File Navigator, vi-keybindings !" target="_blank">vifm</a> does not have the comfort of mc and is also slower. I would almost die for vimlike keybindings in mc,  so when someone has an appropriate solution, please give it to me. I don't mind to press the functionkeys and controlkeys, but grapping to the cursorkeys is a very big workflowkiller as i have to move my hand from the standard-typing position. As i work almost on a laptop, even small error corrections with my thumb on my mousepad, like moving floating windows for example, are not as bad as reaching the f... cursorkeys because my elbows stay almost always at the same place, but only one grab to the cursors and i have to move my whole right shoulder, elbow, arm and also hold it in the air, so my right arm is blocked for this time and i cannot fluidly switch tasks. Another present from god would be a pdf-reader with vi-like keybindings... but hey, people can fly, so maybe one day this will be possible too :)

<b><a href="http://weechat.flashtux.org/" title="IRC-Client" target="_blank">weechat</a>/<a href="http://www.bitlbee.org/main.php/news.html" title="Multi-Protocol-Server/Client" target="_blank">bitlbee:</a></b>

i use now bitlbee in favor of centericq:
<pre>
/server bitlbee im.bitlbee.org 6667 -auto -nicks Nick1 Nick2 Nick3
register &lt;passwd&gt;
account add msn &lt;account&gt; &lt;passwd&gt;
account add oscar &lt;account&gt; &lt;passwd&gt; login.icq.com/login.oscar.aol.com
account add yahoo &lt;account&gt; &lt;passwd&gt;
account add jabber username@gmail.com &lt;passwd&gt; talk.google.com:5223:sslaccount on

identify &lt;passwd&gt;
set private false</pre>
Now the explanation:
First i tell weechat to autoconnect to bitlbee when starting weechat, you get redirected to your bitlbee channel.
In this channel you register the nick you joined the bitlbee network (either Nick1, Nick2, or Nick3).
Then you add your accounts, for icq/aol choose the appropriate server.
Then you connect all accounts to bitlbee, after that the only thing you have to do when you start weechat is to type identify &lt;passwd&gt;.

With set private false you get all messages in the mainwindow, there type nick: to talk to somebody in your list.

Works like charm, serverside buddylists for all networks, no need to rename ID's to nicknames.
For further information type help in your bitlbee channel,
to clear the window type /cl.
Have to find out howto connect  to the gadu gadu network, i guess i have to register to a jabber-server which has a gadu-gadu transport, but i don't know how for the moment.

some servers like testing.bitlbee.org have ssl-support through port 6668, just enter that port and type /set bitlbee.server_ssl = on

<a href="http://wiki.xmms2.xmms.se/index.php/Main_Page" title="Mp3 Player Daemon" target="_blank"><b>xmms2:</b></a>

Server/Client architecture, audioscrobbler/last.fm-plugin, written in ruby, is included.

millions of clients, but not one nice consoleclient :)

ok there is <a href="http://sirius.cine7.net/nyello/" title="pseudoshell frontend for xmms2" target="_blank">nyello</a>, as if i need another cli-client :) ok, have to be more tolerant here, lets see what the future shows.

So mpd and ncmpc move up closer and closer to me :) (If there would not be amarok, its grotoes slow but the comfort is capital and altough this is  chill, after a few hours of play it is not more.)

One big plus of xmms2: .cue cuesheet support which mpd does not have.

maybe some day i find out how to ged rid of the black background of x2cp

<b><a href="http://www.musicpd.org/" title="Music Player Daemon" target="_blank">mpd</a>/<a href="http://www.musicpd.org/ncmpc.shtml" title="ncurses client for mpd" target="_blank">ncmpc</a>/<a href="http://vidar.gimp.org/?page_id=50" title="Proxy for last.fm streams" target="_blank">lastfmproxy</a>/<a href="http://www.red-bean.com/~decklin/software/lastfmsubmitd/" title="scrobble with mpd" target="_blank">lastfmsubmitd</a>:</b>

I think my search for an consolebased solution whith most of last.fm features is over:

layman -a mpd   &lt;-- for lastfmsubmitd/lastmp (tried mpdscribble, but it doesn't scrobbled last.fm-streams for me complaining that the song is too short)

layman -a zugaina    &lt;-- for lastfmproxy

So to have everything working you have to start all of this :

/etc/init.d/mpd start

/etc/init.d/lastfmproxy start

/etc/init.d/lastfmsubmitd start (in gentoo you have to do a chown lastfm /etc/lastfmsubmitd.conf)

/etc/init.d/lastmp

mpd --update-db updates your database

For playing streams in the m3u-format directly from the net i have this solution:

First create this script and make it executable (you need to emerge mpc for this to work):
<blockquote> #!/bin/bash
mpc clear
cat $1 | mpc add
mpc play</blockquote>
Then associate your browser to open all .m3u endings with this script.

More useful hints about mpd you can find <a href="http://pp.laemmy.net/MPD#titelanker10" title="mpd tips" target="_blank">here</a> (German only). Btw: i tend to use the mpc-client bundled with mpd

<b><a href="http://rus.members.beeb.net/rexima.html" title="console mixer" target="_blank">rexima:</a></b>

A simple Mixer for the console, cursesbased, most important: you can select channels with j+k and adjust volume with h+l :)

<b><a href="http://triq.net/obex" title="bluetooth transfer" target="_blank">obexftp:</a></b>

Transfer files from and to your cellphone via bluetooth

To receive files from your mobile simply start the server with:

obexftpd -c /tmp -b

Then add the OPUSH handler:

<code>sdptool add --channel=10 OPUSH</code>

If for some reason you can't connect with your mobile, delete this directory:

rm -r /var/lib/bluetooth

Now send your files from the menu of your mobile and you receive them in your tmp-directory

<b><a href="http://www.roaringpenguin.com/penguin/open_source_remind.php" title="calendar for console" target="_blank">remind:</a></b>

consolebased calendar, see  <a href="http://princ3.wordpress.com/2006/10/22/gtd/" title="My GTD article" target="_blank">here</a>.

<b><a href="http://www.arrakis.es/~rggi3/youtube-dl/" title="youtube commandline download" target="_blank">youtube-dl:</a></b>

Well, not much to say here, download youtube videos from the command-line

emerge youtube-dl

<b><a href="http://archmage.sourceforge.net" title="view chm files" target="_blank">archmage:</a></b>

with this little handy program you can view *.chm files, it replaced completely xchm for me.

archmage -p 1234 some/interestingtext.chm

now connect with a textbrowser to port 1234, for example:

elinks http://localhost:1234

and voila, you can read *.chm files at the console.

For you gentooers out there, there is an ebuild at <a href="http://bugs.gentoo.org/show_bug.cgi?id=55892" title="archmage ebuild">bugs.gentoo.org</a>

<b><a href="http://alioth.debian.org/projects/surfraw/" title="commandline  interface to WWW " target="_blank">surfraw:</a></b>

search the web from the commandline, currently supports 72 searchengines, some examples:

sr leodict some_english_word_i_dont_understand

This opens  leo.org in elinks (you can of course specify your favourite browser) and translates the word for me into the german language. Of course you can  set your own language:

sr leodict -help

shows you all options for this! searchengine.

This is the best commandline-translating-solution i have, i made an alias leo="sr leodict" and mapped quiting elinks without confirmation to a lowercase q instead of the default uppercase one.

You can also search wikipedia, ebay, google, imdb, /. ...:

sr -elvi

shows you all available searchengines and webservices.

<b><a href="http://www.linuxpowertop.org/" title="tool helping reduce powerconsuming software/settings" target="_blank">powertop:</a></b>

reduce the consumption of power by following the suggestions for your computer
