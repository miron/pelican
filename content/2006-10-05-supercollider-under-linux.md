Title: supercollider under linux
Date: 2006-10-05
Tags: audio, linux, supercollider, error
Category: Vim 
Summary: there is a vimscript for that


Just compiled supercollider and get the error:
<pre><em>sclang: error while loading shared libraries: libscsynth.so: cannot
</em><em> open shared object file: No such file or directory
</em></pre>
my break from linux was too long, so i forgot to add /usr/local/lib to /etc/ld.so.conf and run ldconfig as root.

Found this supercollider interaction script for vim:

<a href="http://www.neisis.net/~alex/scvim/" title="supercollider interaction for vim" target="_blank"> http://www.neisis.net/~alex/scvim/</a>
