let mapleader = ','
let g:mapleader = ','
filetype on
filetype indent on
filetype plugin on
filetype plugin indent on
if filereadable(expand("~/.vimrc.bundles"))
    source ~/.vimrc.bundles
endif
set autoread
"显示行号
set nu
set nowrap
set showmode
set showcmd
set scrolloff=5
"高亮当前行
set cursorline
"用空格代替tab
set expandtab
"自动缩进
set autoindent
set smartindent
set smarttab
set cindent
set softtabstop=4
"缩进宽度
set tabstop=4
set shiftwidth=4

set foldenable
set foldmethod=indent
set foldlevel=20
"语法高亮
syntax on

"禁止在makefile中将tab转换成空格
autocmd FileType make set noexpandtab 

set relativenumber number
au FocusLost * :set norelativenumber number
au FocusGained * :set relativenumber
autocmd InsertEnter * :set norelativenumber number
autocmd InsertLeave * :set relativenumber
function! NumberToggle()
    if(&relativenumber == 1)
        set norelativenumber number
    else
        set relativenumber
    endif
endfunc
nnoremap <C-n> :call NumberToggle()<cr>

function! HideNumber()
    if(&relativenumber == &number)
        set relativenumber! number!
    elseif(&number):
        set number!
    else
        set relativenumber!
    endif
    set number?
endfunc
nnoremap <F2> : call HideNumber()<CR>
nnoremap <F4> : set wrap! wrap?<CR>
set pastetoggle=<F5>
au InsertLeave * set nopaste
nnoremap <F6>:exec exists('syntax_on') ? 'syn off' : 'syn on'<CR>

map <C-j> <C-W>j
map <C-k> <C-W>k 
map <C-h> <C-W>h
map <C-l> <C-W>l

map <space> /
map <Leader>sa ggVG" 
nmap t o<ESC>k
nmap T O<ESC>j
autocmd BufNewFile *.sh,*py exec ":call AutoSetFileHead()"
function! AutoSetFileHead()
    if &filetype == 'sh'
        call setline(1,"\#!/bin/bash")
    endif

    if &filetype == 'python'
        call setline(1,"\#!/usr/bin/env python")
        call append(1,"\# coding: utf-8")
    endif

    normal G
    normal o
    normal o
endfunc
"plugin taglist
let Tlist_Ctags_Cmd = '/usr/bin/ctags'
let Tlist_Show_One_File = 1
let Tlist_Exit_OnlyWindow = 1
let Tlist_Use_Right_Window = 1
nmap <F9> :TlistToggle<cr>
