Title: Sorting Directories On Size, Human Readable
Date: 2007-04-28
Category: Linux
Tags: linux, terminal, grep, directories, du, sort, human-readable
Summary: Linux madness


So far i have this:

`du -h --max-depth=1 | grep '[0-9]K' | sort -n ; du -h --max-depth=1 | grep '[0-9]M' | sort -n | du -h --max-depth=1 | grep '[0-9]G' | sort -n`

To include regular files in this sorting just use du -ah instead...

Edit: A far better version as pointed by <a href="http://deice.daug.net/" target="_blank">deice</a> is:
<pre>
<code>
du -s * | sort -n | cut -f 2- | while read a; do du -hs $a; done
</code></pre>

