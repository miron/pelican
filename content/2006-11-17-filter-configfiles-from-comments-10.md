Title: Filter configfiles from comments
Date: 2006-11-17
Tags: linux, egrep, filter, comments
Category: Linux
Summary: no code, just comments

Somtimes you only want to see configuration in a config-file, to filter out every blank line and every comment line a simple:
<pre>

egrep -v '^$|^#' something.conf
  |    |  | | '-&gt; a  mesh at the beginning of line
  |    |  | '-&gt; or
  |    |  '-&gt; from start to end ... nothing -&gt; blank line
  |    '-&gt; do not show ... containing
  '-&gt; to match against regular expressions</pre>
will do the work.

Edit:

Found another way:

grep ^[^#]

Also filters comments and blank lines (but no spaces and tabs).

