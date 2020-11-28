#FROM nvidia/cuda:10.1-cudnn7-runtime-ubuntu18.04
FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    git \
    curl \
    ca-certificates \
    python3 \
    python3-pip \
    sudo \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m user

RUN chown -R user:user /home/user/

COPY --chown=user *.* /home/user/app/

USER user
RUN mkdir /home/user/data/

RUN cd /home/user/app/ && pip3 install -r requirements.txt
RUN pip3 install mkl

WORKDIR /home/user/app

