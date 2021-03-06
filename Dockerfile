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
RUN mkdir /home/user/app/

ADD requirements.txt /home/user/app/
WORKDIR /home/user/app
RUN pip3 install -r requirements.txt
RUN pip3 install mkl
ADD . /home/user/app/

RUN chown -R user:user /home/user/
USER user

RUN mkdir /home/user/data/
EXPOSE 5000
RUN chmod +x /home/user/app/src/init.sh
WORKDIR /home/user/app/src
ENTRYPOINT [ "./init.sh" ]
