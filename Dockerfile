FROM python:3.7.5-alpine3.10

MAINTAINER nownabe

RUN apk add --update --no-cache build-base

ENV MECAB_VERSION 0.996
ENV IPADIC_VERSION 2.7.0-20070801
ENV mecab_url https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE
ENV ipadic_url https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM
ENV build_deps 'curl git bash file sudo openssh'
ENV dependencies 'openssl'

RUN apk add --update --no-cache ${build_deps}

# Install dependencies
RUN apk add --update --no-cache ${dependencies}

# Install MeCab
RUN curl -SL -o mecab-${MECAB_VERSION}.tar.gz ${mecab_url} \
    && tar zxf mecab-${MECAB_VERSION}.tar.gz \
    && cd mecab-${MECAB_VERSION} \
    && ./configure --enable-utf8-only --with-charset=utf8 \
    && make \
    && make install \
    && cd


# Install Neologd
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
    && mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -y

ADD requirements.txt /
RUN pip install -r requirements.txt