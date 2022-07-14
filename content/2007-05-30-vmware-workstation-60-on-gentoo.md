Title: Vmware-Workstation 6.0 On Gentoo
Date: 2007-05-30
Category: Linux
Tags: linux, virtualisation, error, gentoo, vmware
Summary: If it doesn't work, just write an ebuild

Today i installed VMware-workstation-.0.0.45731. if you get this error:

/opt/vmware/workstation/lib/vmware/bin/vmware: symbol lookup error: /opt/vmware/workstation/lib/vmware/lib/libvmwareui.so.0/libvmwareui.so.0: undefined symbol: _ZN3Gtk6Widget14get_accessibleEv

start it like this:

VMWARE_USE_SHIPPED_GTK=yes vmware

btw, the vmwareinstaller needs the runleveldirectories rc0.d-rc6.d, just create symlinks to the runlevels of gentoo,

there is also an <a href="http://bugs.gentoo.org/show_bug.cgi?id=177876" title="vmware ebuild" target="_blank">ebuild</a> on bugs.gentoo.org, somebody pointed out to get it working after some modifications to i386.

Edit: vmware-workstation-6 is allready in portage, just unmask it and also unmask latest  vmware-modules.

