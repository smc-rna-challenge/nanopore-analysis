FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y g++ make perl python python-numpy python-scipy unzip wget zlib1g-dev 

WORKDIR /opt

ADD splicemap.py /usr/local/bin/

# Install SpliceMap
RUN wget https://web.stanford.edu/group/wonglab/SpliceMap/SpliceMap3352_linux-64.zip && \
    unzip SpliceMap3352_linux-64.zip

# Install Bowtie2
RUN wget https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.3.4/bowtie2-2.3.4-linux-x86_64.zip && \
    unzip bowtie2-2.3.4-linux-x86_64.zip 

ENV PATH=/opt/SpliceMap3352_linux-64/bin:/opt/bowtie2-2.3.4-linux-x86_64:/usr/local/bin:$PATH
