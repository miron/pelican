Title: weechat: automatic identify to NickServ and BitlBee
Date: 2006-11-07
Tags: irc, linux, weechat, identify, automatic
Category: Linux
Summary: less typing, so I can type more

If you don't want to type on each start of weechat to identify yourself, do:

<em>/set freenode.server_command="/msg NickServ identify PASSWORD"</em>

Replace freenode with the server you want to connect of course if needed.

For automaticaly connect to the BitlBee-Server you have to type:

<em>/set bitlbee.server_command="/msg &amp;bitlbee identify PASSWORD"</em>
