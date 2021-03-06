Title: Enable And Disable Spell-Checking In Vim
Date: 2007-09-24
Category: Vim
Tags: terminal, vim
Summary: Spellcheckers unite

First you choose the language which you want to use:

`:setlocal spell spelllang=en_us`

or 

`:setlocal spell spelllang=de_at`

For the German spell files you have to:

`emerge vim-spell-de`

You can disable spellchecking with:

`:set nospell`

`]s` move to next misspelled word, `[s` move to prev. misspelled word
`z=` suggests correctly spelled words under cursor,
`1z=` takes the first word from the suggestion list
`^Xs` does the same in insert mode.
`:spellr` repeats replacements done with `z=` for all matches

For more info about spellchecking in vim:

`:h spell`
