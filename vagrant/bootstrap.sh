#!/bin/sh -e

print_usage () {
  echo "Install vagrant dependencies"
  }

export DEBIAN_FRONTEND=noninteractive

PROVISIONED_ON=/etc/vm_provision_on_timestamp
if [ -f "$PROVISIONED_ON" ]
then
  echo "VM was already provisioned at: $(cat $PROVISIONED_ON)"
  echo "To run system updates manually login via 'vagrant ssh' and run 'apt-get update && apt-get upgrade'"
  echo ""
  print_usage
  exit
fi

apt-get install software-properties-common
apt-add-repository ppa:ansible/ansible
apt-get update
apt-get install -y ansible

# Tag the provision time:
date > "$PROVISIONED_ON"

