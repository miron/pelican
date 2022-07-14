Title: Omni-completion (aka "Intelisense") in vim using tab-key
Date: 2006-10-27
Tags: code, vim, completion, tab
Category: Vim
Summary: vimscript is a scripting language, so it is possible to use vim to write scripts

Just add this fine piece of code to your ~/.vimrc:
<pre>
 function! CleverTab()
           if pumvisible()
             return "\"
           endif
   if strpart( getline('.'), 0, col('.')-1 ) =~ '^s*$'
      return "\"
           elseif exists('&amp;omnifunc') &amp;&amp; &amp;omnifunc != ''
              return "\"
           else
              return "\"
          endif
endfunction
inoremap  =CleverTab()</pre>
<pre></pre>
Edit:
Found a site which describes quite well how to enable the built in omnicompletion using ^X^O <a href="http://amix.dk/blog/viewEntry/19021" title="omnicompletion in vim" target="_blank">here</a>.

^X^F completes filenames and directories.

Some other completion methods:

<a href="http://blog.rosejn.net/articles/2006/02/28/snippetmagic-0-02" title="another textmate snippets in vim" target="_blank">SnippetMagic:</a>

Works for my but the arrow keys  are not correctly mapped so use better

<a href="http://vim.sourceforge.net/scripts/script.php?script_id=1318" title="textmates snippets for vim" target="_blank">snippetsEmu:</a>

witch worked out of the box for me, just create  ~/.vim/after/ftplugin, open the vimball, source it with :so and use it with your tab-key.

