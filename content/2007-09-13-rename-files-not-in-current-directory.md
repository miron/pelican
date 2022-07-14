Title: Rename Or Copy Files Not In Current Directory
Category: Linux
Date: 2007-09-13
Tags: linux, terminal
Summary: Autocompletion in zsh is the best


I often catched myself renaming a file in some other directory like this:


    :::bash
    mv some/dir/some/file some/dir/somefile_renamed                                                                               

But there is an easier way:

    :::bash
    mv some/dir/some/{file,file_renamed}

This also works for copying:

    :::bash
    cp /etc/mail/{sendmail.cf,sendmail.cf.orig}

Or vimdiff:

    :::bash
    vimdiff /etc/mail/{sendmail.cf,sendmail.cf.orig}

And thats why I love zsh so much, you can even tabcomplete after the {, try that in bash f.e. :)
Be creative, I'm sure there are many useful fields of application.
