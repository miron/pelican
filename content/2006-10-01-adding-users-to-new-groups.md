Title: Adding users to new groups
Date: 2006-10-01
Tags: irc
Category: Linux
Summary: schizoalism, many users, many personalities

If you want to add an user to a new group without to specify the groups he is allready in, use:

gpasswd -a &lt;user&gt; &lt;group&gt;
Then to make the group available without logging out from X, as user you can type:

newgrp &lt;group&gt;
