FROM ubuntu:14.04

ENV container=docker

RUN apt-get update && \
    apt-get install -y \
    python \
    openssh-server \
    dbus \
    && rm -rf /var/lib/apt/lists/*

CMD ["/sbin/init"]
