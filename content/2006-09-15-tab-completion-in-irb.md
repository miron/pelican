Title: Tab completion in irb
Date: 2006-09-15
Tags: ruby, completion, irb
Category: Ruby
Summary: i don't want to type if i don't need to

Just want to memorize.
irb --readline -r irb/completion
Now i can tabcomplete methods. (But this disables Filecompletion)

To make it permanent add this to your .irbrc:

require 'irb/completion'