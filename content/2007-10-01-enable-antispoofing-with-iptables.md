Title: Enable Antispoofing With Iptables
Date: 2007-10-01
Category: Linux
Tags: networking
Summary: Write to that proc filesystem



    :::bash
    for i in /proc/sys/net/ipv4/*/rp_filter
    do
       echo 1 > $f
    done

Or simply

    :::bash
    echo 1 > /proc/sys/net/ipv4/*/rp_filter
(depends on your shell)

This compares the source adress against the routing table

More info about the ~50  options you can find at /usr/src/linux/Documentation/networking/ip-sysctl.txt
