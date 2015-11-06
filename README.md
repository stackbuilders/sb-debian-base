# sb-debian-base

Ansible playbooks for configuring a generic Debian server.

## Install the required playbooks

```
$ ansible-galaxy install jnv.unattended-upgrades
$ ansible-galaxy install nickjj.fail2ban
$ ansible-galaxy install geerlingguy.ntp
$ ansible-galaxy install jdauphant.nginx
$ ansible-galaxy install ANXS.postgresql
$ ansible-galaxy install kamaln7.swapfile
```

The bootstrap process in this script also sets the system hostname
based on the hostname used in the inventory. If you'd prefer to override
the hostname, you can set the host variable "hostname" and that value
will be preferred. The following uses the hostname value rather than
127.0.0.1:

```
127.0.0.1:2222 hostname=vanderbilt-staging.stackbuilders.net
```
