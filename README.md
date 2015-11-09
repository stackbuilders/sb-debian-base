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
$ ansible-galaxy install jdauphant.ssl-certs
```

The bootstrap process in this script also sets the system hostname
based on the hostname used in the inventory. If you'd prefer to override
the hostname, you can set the host variable "hostname" and that value
will be preferred. The following uses the hostname value rather than
127.0.0.1:

```
127.0.0.1:2222 hostname=staging.stackbuilders.net
```

## Use Vagrant to test provisioning

To use vagrant and ansible is essential to have vagrant and Virtual Box for our configuration. [Download vagrant](https://www.vagrantup.com/downloads.html) [Donwload Virtual Box](https://www.virtualbox.org/wiki/Downloads)
How to use vagrant and :
* Into the project folder type ```vagrant up``` which use the Vagrantfile to provide the information to start the VM.
* Connect by ssh type ```vagrant ssh``` into the project folder.
* Stop machine ```vagrant halt``` into the project folder.
* Destroy machine ```vagrant destroy``

