Title: Compare Directories with diff
Date: 2008-05-15
Tags: compare, diff, directories, linux, terminal
Category: Linux 
Summary: So many files, deduplicate

Its easier than i thought, just type:

    :::bash
    diff -rq Dir1 Dir2

-r stands for rekursive

-q output only wether content differ
