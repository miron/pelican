Title: Redirect And Save Tcpdump Output To Other Host
Date: 2007-09-28
Category: Linux
Tags: linux, networking, terminal
Summary: This are the times

So you have one of those fancy Linksys-Routers with OpenWrt on it and want to save the output of tcpdump. As the local storage is limited and OpenWrt does not support a monitoring-port you have to redirect the output to save on another host.

But first lets enlarge onto that monitoring-port.
For what i know DD-Wrt's iptables supports by default the ROUTE target with the `--tee` parameter:

    :::bash
    --tee
    Make a copy of the packet, and route that copy to the given destination. 
    For the original, uncopied packet, behave like a non-terminating target
    and continue traversing the rules.
    Not valid in combination with --iif or --continue

I tried to patch OpenWrt's iptables with the ROUTE target, but no luck as this extensions seems not to be maintained anymore.

As DD-Wrt is OpenWrt-based, i supose i only need the ipkg from them and can install it on my router, have to investigate that further.

Far less complicated is to start tcpdump on your router and redirect the output to your PC like this:

    :::bash
    tcpdump -i any ! host 192.168.1.2 -s 0 | ssh someone@192.168.1.2 "cat > dump.txt"

Change tcpdump filters to your liking.
