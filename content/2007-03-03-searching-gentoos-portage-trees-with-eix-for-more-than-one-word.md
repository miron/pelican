Title: Search gentoo portage-trees with eix for multiple words
Date: 2007-03-03
Category: Linux
Tags: linux, terminal, word, description, regex, regexp, gentoo, eix
Summary: regex are words is a language 


Edit:

You can, now ?, use multiple arguments of -S to achieve the same result so:

<code> eix -S 'cd' -S 'writ' </code>

works the same.
Thanks goes to Emil Beinroth for this hint.

All i wanted to do, was to search gentoo's package descriptions for two words, quite after or nearby. How could i know that this proved to be so hard :)

After long research i found on a site a regexp doing  more or less that what i wanted:

<a href="http://www.regular-expressions.info/near.html" title="Regular Expressions" target="_blank">http://www.regular-expressions.info/near.html</a>

Of course it malfunctioned, so i tried to adapt it to eix.

Here my results so far, help and improvement suggestions appreciated :):

So when i try for example to search for the words 'cd' and 'writing' i type:

<code>eix -S 'cd(\W*\w*){9}writing|writing(\W*\w*){9}cd'</code>

Spoken:

find the word 'cd', followed by some non-alphanumerics (or not), followed by some alphanumerics (or not) and repeat this alphanumerics - non-aphanumerics thingie for my sake 9 times before you search for the word 'writing' (so this match finds only to a maximum of 8 words between 'cd' and 'writing'). Then reverse the two words and do the same sh...

Then try this same with 'write' or 'writ', there are at least 6 applications which don't have the word 'burn' in their descriptions, it could be that easy :)

at least i have united k3b and xcdroast in one search result, so that all was not for nothing :)
