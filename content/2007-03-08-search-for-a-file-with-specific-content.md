Title: Search for a file with specific content
Date: 2007-03-08
Tags: linux, terminal, find, grep, content, file
Category: Linux
Summary: the search never ends

Found a site which describes this quite good (german):

<a href="http://www.linuxfocus.org/Deutsch/September1998/article64.html">http://www.linuxfocus.org/Deutsch/September1998/article64.html</a>

Lets do some comparison and search the whole root directory for the string "PAGER":

Lazy as i am i first started with the shortest possibility:

<em>grep "PAGER" `find / -type f -print`</em>

Does not find anything for me, zsh gives me an error "argument list too long"

Here some explanation why this is so:

<a href="http://michael-prokop.at/blog/2007/02/26/argument-list-too-long/">http://michael-prokop.at/blog/2007/02/26/argument-list-too-long/</a>

getconf ARG_MAX shows us the limit of 131072 characters allowed passing the command-line at once.,

So lets try something else, this time using xargs, which breaks the command down below 131072 characters:

<em>find / -type f -print | xargs grep "PAGER"</em>

Little bit better now, but, when i come across files with spaces in the filename i get problems, so lets try it again:

<em>find / -type f -print0 | xargs -0 grep "PAGER"</em>

ok, this finally works. Somewhere someone shouted out that the parameters -print0 and -0 are not posix compliant, so for you purists out there another working solution:

<em>find / -type f -exec grep "PAGER" /dev/null {} \;</em>
