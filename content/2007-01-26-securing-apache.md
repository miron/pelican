Title: securing apache
Date: 2007-01-26
Tags: apache, linux, security
Category: Linux
Summary: everything has to be rewritten, I said everything

Try to summarize some settings to secure apache:

*) Disable TRACE:

<span class="body"></span>
<pre>RewriteEngine On
RewriteCond %{REQUEST_METHOD} ^TRACE
RewriteRule .* - [F]</pre>
mod_rewrite is needed, also has to be done in the
&lt;VirtualHost www.example.com&gt; section.

