FROM ubuntu:18.04

RUN apt-get update \
 && apt-get install -y mecab \
 && apt-get install -y libmecab-dev \
 && apt-get install -y mecab-ipadic-utf8\
 && apt-get install -y git\
 && apt-get install -y make\
 && apt-get install -y curl\
 && apt-get install -y xz-utils\
 && apt-get install -y file\
 && apt-get install -y sudo\
 && apt-get install -y wget

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git\
 && cd mecab-ipadic-neologd\
 && bin/install-mecab-ipadic-neologd -n -y

RUN apt-get install -y software-properties-common vim
RUN add-apt-repository -r ppa:jonathonf/python-3.6
RUN apt-get update -q

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN python3.6 -m pip install pip --upgrade

RUN pip install flask
RUN pip install mecab-python3