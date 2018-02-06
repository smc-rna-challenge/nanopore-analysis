FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y g++ make wget bzip2 zlib1g-dev 

WORKDIR /opt
RUN wget https://github.com/lh3/minimap2/releases/download/v2.7/minimap2-2.7_x64-linux.tar.bz2 && \
    tar -xjf minimap2-2.7_x64-linux.tar.bz2 && \
    cp minimap2-2.7_x64-linux/minimap2 minimap2-2.7_x64-linux/misc/k8 /usr/local/bin/
