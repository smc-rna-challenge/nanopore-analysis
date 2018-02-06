FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y g++ make perl python python-numpy python-scipy unzip wget zlib1g-dev 

WORKDIR /opt

# Install SpliceMap
RUN wget https://web.stanford.edu/group/wonglab/SpliceMap/SpliceMap3352_linux-64.zip && \
    unzip SpliceMap3352_linux-64.zip

# Install Bowtie2
RUN wget https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.3.4/bowtie2-2.3.4-linux-x86_64.zip && \
    unzip bowtie2-2.3.4-linux-x86_64.zip 
 
# Install STAR
RUN wget https://github.com/alexdobin/STAR/archive/STAR_2.4.0i.tar.gz && \
    tar -zxvf STAR_2.4.0i.tar.gz

# Install GMAP
RUN wget http://research-pub.gene.com/gmap/src/gmap-gsnap-2017-11-15.tar.gz && \
    tar -zxvf gmap-gsnap-2017-11-15.tar.gz && \
    cd gmap-2017-11-15 && \
    ./configure && \
    make && \
    make install

# Install IDP-fusion
RUN wget https://www.healthcare.uiowa.edu/labs/au/IDP-fusion/files/IDP-fusion_1.1.1.tar.gz && \
    tar -zxvf IDP-fusion_1.1.1.tar.gz
    

ENV PATH=/opt/IDP-fusion_1.1.1:/opt/SpliceMap3352_linux-64/bin:/opt/bowtie2-2.3.4-linux-x86_64:/opt/STAR-STAR_2.4.0i/bin/Linux_x86_64:/usr/local/bin:$PATH
