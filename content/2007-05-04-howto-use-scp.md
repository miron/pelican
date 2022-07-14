Title: Howto use scp
Date: 2007-05-04
Tags: linux, terminal, scp
Category: Linux
Summary: Not one times, not two times, but always I forget

Forgetful as i am here a simple reminder how to use scp:

`scp /some/file root@192.168.1.1:newnameoffile`

or simpy:

`scp /some/file root@192.168.1.1:`

to copy the file under the same name.

Want to copy a whole directory ?

`scp -r some/dir root@192.168.1.1:`
