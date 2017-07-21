# Version: 0.0.1
FROM ubuntu:16.04
MAINTAINER Andrey <akrush24@gmail.com>
RUN apt-get update
RUN apt-get install -y python3 vim bash-completion openssh-client git
#EXPOSE 2222
VOLUME ["/home/akrush/py"]
