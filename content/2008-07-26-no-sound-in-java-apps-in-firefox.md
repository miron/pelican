Title: No Sound in Java-apps in Firefox
Date: 2008-07-26
Category: Linux
Tags: alsa, api, gentoo, java, linux, oss, sound
Summary: OSS Sequencer API

For a long time i had not sound in Firefox on Sites using Java (hobnox.com, runescape.com)

I tested the Javasound localy withe the JavaSoundDemo:

http://java.sun.com/products/java-media/sound/samples/JavaSoundDemo/

and i worked flawlessly.

I had to activate the OSS Sequencer API in the Kernel under:

Device Drivers/Sound/Advanced Linux Sound Architecture/

So even modern sites still use and need the OSS API, good to know :)
