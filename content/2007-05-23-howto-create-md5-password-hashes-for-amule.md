Title: Howto create md5 password-hashes for amule
Date: 2007-05-23
Tags: terminal, md5, amule, md5sum
Category: Linux
Summary: Safety first

to connect to your amuled you need to save your password as md5-hash in your .aMule/amule.conf.

Here is how you create one:

`echo -n password | md5sum | cut -d ' ' -f 1`


