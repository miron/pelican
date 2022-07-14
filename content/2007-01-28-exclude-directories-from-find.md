Title: exclude directories from find
Date: 2007-01-28
Category: Linux
Tags: linux, terminal, find, exclude, dirs, directories
Summary: not everything wants to be found

To exclude dirs from the find command:

    :::bash
    find / -path '/some/dir' -prune -o -name '*.txt' -ls
