##How to use this repo:
First make sure you create the requirements.yml file
and add the reference to this repository, as following:

```
---
- src: jnv.unattended-upgrades
  version: v1.1.0
  path: external-roles

- src: git@github.com:stackbuilders/sb-debian-base.git
  scm: git
  version: remotes/origin/master
  path: external-roles
```
After that you need to run the following command:

```
ansible-galaxy install -r requirements.yml
```

## Tags available in this repo
The following tags are available:

### - prebootstrap
This tag contains basic setup tasks, such as:
- Add administrator User
- Enable default repositories for Debian
- Update packages
- Install sudo packages
- Remove password for sudoers group
- Setup authorized ssh keys for administrator users
    - You need to define this file: keys/administrators

### - bootstrap
This tag contains more advance setup tasks, such as:

- Disallow password authentication for SSH sessions.
- Disallow ssh access for root user
- Upgrade Dist packages
- Install Unattended-Upgrades for security patches only
    - You need to define the var {{ uu_email_alerts }} (e.g. example@example.com)
- Install basic packages
    - s.a: vim, tmux, htop, atop, ufw, emacs, atsar, git, curl
- Create group for deployer user
    - You need to define the var {{ deploy_username }} (e.g. user_to_deploy, user_without_privileges)
- Create deployer user and create ssh keys (public and private)
    - You need to define the var {{ deploy_username }} (e.g. user_to_deploy, user_without_privileges)
- Setup authorized ssh keys for the deployer user
    - You need to define the files: keys/deploy_users, e.g. keys/ci-staging
- Set hostname to host-specific
    - You need to define {{ hostname }}
- Set hostname in the inventory
    - You need to define {{ inventory_hostname }}
- Enable UFW
- Open general ports ( e.g. ssh port, http port)
    - You need to define {{ ports }}
- Open specific ports for specific IPs
    - You need to define {{ port_ips }}
- This tag ensures github.com is a known host
    - You need to define {{ deploy_username }}

#### External dependencies (galaxy) included in this tag -bootstrap
- kamaln7.swapfile (Setups the swapfile)
    - You need to define the var {{ swap_file_size }} (e.g. 2048)
- nickjj.fail2ban (Install and configure fail2ban)
- geerlingguy.ntp (Installs NTP)


### - set-hostname
- Set hostname to host-specific
    - You need to define {{ hostname }}
- Set hostname in the inventory
    - You need to define {{ inventory_hostname }}

### - create-app-directory
- name: Set up application deploy directory
    - You need to define {{ user_owner_app_directory }} and {{ user_group_app_directory }}

### - haskell-build-dependencies
- Install common Haskell build dependencies
    - (s.a libpcre3-dev, libsqlite3-dev, libpq-dev)

### - haskell-stack
- Add FPCO Deb Key
- Add FPCO Deb repository
- Update packages
- Install Stack packges

### - ruby-dependencies
- Install dependencies for rvm
    - (s.a. build-essential, tklib,zlib1g-dev,libssl-dev,libreadline-gplv2-dev,libxml2,libxml2-dev,libxslt1-dev)

### - basic-postgres
- external dependency ANXS.postgresql which installs and configures PostgreSQL, extensions, databases and users

### - nginx-https
- external dependency jdauphant.nginx to install and manage nginx configuration

### - add-remove-keys
- deploy listed ssh-keys into key files, first remove/add  unneeded/needed keys on keys/* folder

## Files you need to create
You should have the following list of files containing the SSH public-keys for both the administrator and deployer users, respectively.

```
keys/administrators
keys/deploy_users
```

## How to execute/run these playbooks

```
# Basic image
ansible-playbook -l local -i allservers.yml --tag prebootstrap site.yml -vvv -k -u root

# Administrator account
ansible-playbook -l local -i allservers.yml --tag bootstrap site.yml -vvv -u administrator
```

License
-------

MIT, see the LICENSE file in this repo.

Author Information
------------------

Justin Leitgeb, Stack Builders Inc.
