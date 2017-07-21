# Version: 0.0.2
FROM ubuntu:latest
MAINTAINER Andrey <akrush24@gmail.com>
RUN apt-get update \
 && apt-get install -y python3 vim bash-completion
RUN echo 'set tabstop=3\n\
set nocompatible\n\
set number\n\
highlight LineNr term=bold cterm=NONE ctermfg=DarkGrey ctermbg=NONE gui=NONE guifg=DarkGrey guibg=NONE\n'\
>> ~/.vimrc
RUN echo 'cd /home/akrush/py' >> ~/.bashrc

EXPOSE 8080
VOLUME ["/home/akrush/py"]
