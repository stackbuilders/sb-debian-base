FROM debian:9

ENV container=docker

RUN apt-get update && \
    apt-get install -y \
    python \
    openssh-server \
    dbus \
    && rm -rf /var/lib/apt/lists/*

RUN touch /var/log/auth.log

CMD ["/usr/lib/systemd/systemd"]
