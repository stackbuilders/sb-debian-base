FROM ubuntu:16.04

ENV container=docker

RUN apt-get update && \
    apt-get install -y \
    python \
    openssh-server \
    dbus \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

RUN touch /var/log/auth.log

CMD ["/sbin/init"]
