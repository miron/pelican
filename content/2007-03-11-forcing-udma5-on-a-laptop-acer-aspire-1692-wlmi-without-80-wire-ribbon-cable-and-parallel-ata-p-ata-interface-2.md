Title: Forcing udma5 on laptop (Acer Aspire 1692 wlmi) 
Date: 2007-03-11
Category: Linux
Tags: hardware, linux, udma2, udma5, ata, ide, laptop, hdparm
Summary: without 80 wire ribbon cable and parallel ATA (P-ATA) interface

<p class="snap_preview">For some time past i bought a hitachi
travelstar 7k100 and to my surprise i could not set udma5 with hdparm,
the kernel restricted the settings to udma2 because it could not find a
80 wire ribbon cable. as i am not willing to solder one in my notebook,
i added  the kernelparameter ide0=ata66 to my grub.conf and now i can
change to udma5 with hdparm. hopefully this parameter will stay for
long time as its allready depreciated and i don’t know if it will be
replaced by something else.
<p class="snap_preview">&nbsp;</p>
<p class="postfeedback">&nbsp;</p>

