Title: Mounting ext4-filesystem with newer Kernels
Date: 2008-05-14
Category: Linux
Tags: debugfs, ext4, linux, mount
Summary: flags for development code

Trying to mount my ext4 partiton with a 2.6.25 kernel i get this errormessage:

    EXT4-fs: hda3: not marked OK to use with test code.

There is a new special flag you have to set to mount development code, so do:

    :::bash
    [root]# debugfs -w /dev/hda3
    debugfs 1.40.9 (27-Apr-2008)
    debugfs:  set_super_value s_flags 4
    debugfs:  quit

More info, debugfs, ext4dev, [here](https://fedoraproject.org/wiki/FedoraExt4).
