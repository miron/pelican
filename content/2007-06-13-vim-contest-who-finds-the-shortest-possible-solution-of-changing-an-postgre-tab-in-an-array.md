Title: Vim contest: shortest solution postgreSQL tab to array
Category: Vim
Date: 2007-06-13
Tags: vim, pragmatic, efficient, editing, benchmark, fast, contest
Summary: To all the Vim wizards out there

Maybe some of you have realised that i became a little obsessed  in the last days  using vim.

Inspired by this Blog <a href="http://helmi-blebe.blogspot.com/2007/04/vim-tips-blockwise-selection-mode-and.html" title="fast table editing in vim" target="_blank">entry</a> I want to start a contest.

Who finds the fastest solution of editing a given postgre table and changing it into an given array ?

What you can win ? Well, the satisfaction of being the only true vim-master of the world :)

That said, here the general framework.

First the table we use in our contest:
<pre>col1 | integer                     | not null
col2 | timestamp without time zone | not null
col3 | character varying(100)      |
col4 | numeric                     |
col5 | numeric                     |
col6 | integer                     |
col7 | integer                     |
col8 | numeric                     |
col9 | numeric                     |
col10 | character varying(100)     |
col11 | character varying          |
col12 | character varying(100)     | not null
col13 | character varying          |
col14 | character varying          |
col15 | numeric                    |
col16 | numeric                    |
col17 | numeric                    |
col18 | character varying          |
col19 | numeric                    |</pre>
There are no lines before or after this table, and no spaces before or after this table

This table we want to alter into this:
<pre>$ary = array('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7','col8',
'col9','col10', 'col11', 'col12', 'col13', 'col14', 'col15', 'col16', 'col17',
'col18', 'col19');</pre>
The array has to begin at the left topmost corner too

We start at the top left corner in normal mode

textwidth is set to 78

tabstop is set to 8

shiftwidth is also set to 8

all relevant settings i did not mention here shall not be altered from the default configuration

only standard keymappings of vim 7.1 are allowed, no abbreviations

So the best would be to start it like this: vim -u NONE

The ending position of the cursor does not matter, as well as the mode in which you  are when you  finished

Every keystroke will be counted, so when a shift- or ctrl-key has to be pressed, this counts as an extra keystroke

I use a German keyboard so my keystrokes will differ from the English ones, of course, for those people with different keyboards, when someone with an English keyboard finds the fastest solution, the keystrokes of the other keyboards will be translated to the English one and vice versa :)

As i am pretty sure there will be some  obscurities because of the endless possibilities of vim, they will be discussed and added to the framework.

So let me begin with my first solution:

&lt;CTRL-V&gt;GI'&lt;Esc&gt;qqelC',&lt;Esc&gt;+q18@qs);&lt;Esc&gt;ggi$ary = array(&lt;Esc&gt;VGq

This makes a total of :
<blockquote> 57 keystrokes</blockquote>
on a German keyboard, this will be converted to the amount of keystrokes on an English keyboard, if needed. I'm very sure it takes less strokes on an English one.

Lets see this test also as an benchmark for other editors, but if you use the mouse, every move of the arm counts as 1 keystroke, so when you grab for the mouse and click something, this counts as 2 keystrokes, not counting the clicks of course, if you move your arm after the click back to your keyboard again, this counts as another keystroke, if you click something else this move counts as another keystroke, if the icons are side by side then only the click is counted.

We have our first winner, this is Matt's solution:

i$ary = array(&lt;Esc&gt;lqqi'&lt;Esc&gt;f C',&lt;Esc&gt;+q99@qs);&lt;Esc&gt;vggJX

Makes a total of:
<blockquote>53 keystrokes (converted to a German keyboard)</blockquote>
Actually the last X is from me, but i'm cocksure he would find that out for himself :)

And the master is on the road again, here my improved version of Matts version:

i$ary = array(&lt;CTRL-O&gt;qq'&lt;Esc&gt;f C',&lt;Esc&gt;+q99@qs);&lt;Esc&gt;vggJX

Makes a total of:
<blockquote> 52 keystrokes</blockquote>

