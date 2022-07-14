Title: How to change default Soundcard under linux
Date: 2006-10-20
Tags: linux, alsa, default, soundcard
Category: Linux
Summary: life without soundcards would be a mistake

First i find out the name of the card:
<em>cat /proc/asound/cards</em>

gets me Audigy2.<em>
</em>

Then i add this lines to my /etc/asound.conf
<pre><code>
pcm.!default {
  type hw
  card Audigy2
}
  ctl.!default {
  type hw
  card Audigy2
}</code></pre>

