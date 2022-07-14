Title: rsync over ssh without rsync --daemon
Date: 2011-06-10
Category: Linux
Tags: linux, terminal
Summary: If you want to rsync without a daemon

    :::bash
    rsync -e ssh -l somefile someuser@someip: