Title: Error when installing instiki with RubyGems
Date: 2007-06-19
Tags: ruby, instiki, error
Category: Ruby
Summary: Errors, errors, love them

clean_logger.rb:13:in `remove_const': constant Logger::Format not defined (NameError)

change from this:

remove_const "Format"

to this:
<pre>
remove_const "Format" if const_defined? "Format"</pre>
because the newer version of logger.rb does not include the line:

Format = "%s, [%s#%d] %5s -- %s: %s\n"

Edit:

The instikiversion in rubygems is so outdated, just download latest version from  http://www.instiki.org/ which works fine.

