Title: Java nada when libX11 compiled with xcb useflag
Date: 2007-12-22
Category: Linux
Summary: The fun of compiling code

Put

    :::bash
    LIBXCB_ALLOW_SLOPPY_LOCK=1

in your /etc/env.d/99local
