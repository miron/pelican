Title: Automatically save Foldings in vim
Date: 2007-01-26
Category: Vim
Tags: linux, vim, folding, save
Summary: folding, the essence of life

Normaly you have to type allways :mkview and :loadview to save your folds, so simply add this two lines to your ~/.vimrc:

<a href="http://applications.linux.com/article.pl?sid=06/05/18/1915233&amp;tid=13"></a>
<blockquote> au BufWinLeave * silent! mkview
au BufWinEnter * silent! loadview</blockquote>
Now, each time you close a file, its fold state will be saved and reloaded when you reopen the file in Vim.

<strike>Edit:</strike>

<strike>When I open new empty files from the shell or from Vim (:new)</strike>

<strike>I get the error message:</strike>

<strike>Error detected while processing BufWinEnter Auto commands for "*":</strike>

<strike>E32: No file name</strike>

<strike>This also happens when  opening :help window and sourcing sessions with</strike>

<strike>the shell command "vim -S session.vim". Have to find a way to run automatic :loadview only for windows that actually have a filename</strike>
