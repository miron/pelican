Title: Cannot connect with ipw2000 module
Date: 2007-08-11
Category: Linux
Tags: hardware, linux, ipw2000, module, crypto, wlan
Summary: Module load error

Building a new kernel i couldn't connect annymore to my wlan-router, allthough i had the same configuration as my other kernel. Whell, almost, under Cryptographic options i build the  AES cipher algorithms  as module therefore  the  ieee80211_crypt_ccmp module could not find  it , though i made a depmod. It gave me the errormessage:

ieee80211_crypt_ccmp: could not allocate crypto API aes

So apparently you have to build this into the kernel for wlan
