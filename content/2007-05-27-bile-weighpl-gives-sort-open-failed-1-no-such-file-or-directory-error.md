Title: BiLE-weigh.pl: sort: open failed: +1: No such file or directory
Date: 2007-05-27
Category: CLI 
Tags: code, terminal, sort, perl, bile
Slug: Bile sorting with perl 
Author: streetyogi
Summary: Command line voodoo

Simply change this line from:

```bash
`cat temp | sort -r -t ":" +1 -n &gt; @ARGV[1].sorted`;
```

to:

```bash
`cat temp | sort -r -t ":"  -k 1 -n &gt; @ARGV[1].sorted`;
```

