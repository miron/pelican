Title: Create directories using brace expansion
Date: 2007-05-30
Tags: linux, terminal, mkdir, expansion, brace
Category: Linux
Summary: the hidden mysteries of the braces

Say you wan't to create several directories, for example rc0.d to rc6.d (vmware needs them for example to install)

you type:

`mkdir rc{0..6}.d`


