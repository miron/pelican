Title: ettercap on openwrt (whiterussian 0.9)
Date: 2007-05-16
Category: Linux
Tags: linux, terminal,  openwrt, linksys, ettercap
Summary: No wonder its called whiterussian

Tried to install ettercap on a Linksys WRT54GL, but the version in the repository misses some dependencies.

You have to install zlib and libpthread. Also the libncurses package misses some libraries, thats why i downloaded it from <a href="http://openwrt.vcp-springe.de/experimental/ettercap/" title="libncurses with missing libraries" target="_blank">here</a> and installed it with ipkg install libncurses_5.2-8_mipsel.ipk


