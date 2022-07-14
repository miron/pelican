Title: Invalid char when starting scripts
Date: 2007-06-11
Tags: ruby, unicode, vim, invalid, character
Category: Vim
Summary: bomb or nobomb, that is here the question (it's nobomb)

foobar.rb:1: Invalid char `\357' in expression
foobar.rb:1: Invalid char `\273' in expression
foobar.rb:1: Invalid char `\277' in expression

Your script gives you this error and and vim shows nothing ? Try to set :set nobomb and save the file.

When you start vim in binarymode, vim -b foobar.rb, than you see the invalid chars

