Title: The Object ARGF and his methods
Date: 2006-09-18
Category: Ruby
Tags: code, ruby, syntax, object, coding
Summary: ruby, ruby, ruby, ah-ah-ah-ah-ah-ah

Today i worked my way through the pickaxe book and triped over this fine example:

There is mentioned that you can abbreviate

ARGF.each {|line| print line if line =~ /Ruby/ }

to something like:

print ARGF.grep(/Ruby/)

So i tried that out in irb and to my surprise the behavior was not the same, ARGF.grep did not print anything. Fortunately a nice guy on #ruby-lang gave me a nice explanation, which goes far beyond my expectations.
1.) Irb has stdin and therefore has weird behavior.
2.) grep collects all its results into an array so it won't return until the file    (stdin) is closed.
3.) After hitting Ctr-D a possibly match gets printed.
4.) each prints immediately the result
5.) To have the same behavior from grep use:

ARGF.grep(/Ruby/) { |s| print s }

no intermediate array is then created, resp. it does create an array but with the results of the block rather than the strings.

Thanks goes to LoganCapaldo for this impressing explanation.

Some more differences between irb and script:

def foo

end

p Object.private_methods  -&gt; normaly foo is here included, not so in irb, as irb starts as public, so you have to type private to have the same behavior

