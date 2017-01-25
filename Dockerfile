FROM ubuntu:latest
RUN apt-get -y update
RUN apt-get -y install git
RUN apt-get -y install build-essential checkinstall
RUN apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
RUN apt-get install -y wget
RUN cd ~ && wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz && tar xzf Python-2.7.13.tgz && cd Python-2.7.13 && ./configure && make install
RUN apt-get install -y python-pip python-setuptools
RUN pip install --upgrade pip setuptools
RUN pip install requests
RUN cd ~ && git clone https://github.com/andrewchan/donorschoose.org.git
ENV PATH=${PATH}:/root/donorschoose.org
ENV PYTHONPATH=${PYTHONPATH}:/usr/local/lib/python2.7/dist-packages
 

