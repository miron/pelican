Title: Syncing your portage tree and overlays with eix
Date: 2007-12-26
Category: Linux
Tags: configuration, gentoo, linux
Summary: Be more productive with oneliners

If you want to sync your portage tree and your layman-overlays with one command, you can use

    :::bash
    eix sync

for that.

All you have to do is to create

    :::bash
    /etc/eix-sync.conf

and place a
    :::bash
    *

in it.

If you want to have a cronjob  for that create for example a file named /etc/cron.weekly/eix.cron

and put something like

    :::bash
    #!/bin/sh
    /usr/bin/eix-sync
    
in it.

You can then delete all other cronjobs like emerge --sync and layman -S

As usual man eix has all the info you need.
