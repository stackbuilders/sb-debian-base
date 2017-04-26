# Stack Builders - Debian Base

[![Build Status](https://travis-ci.org/stackbuilders/sb-debian-base.svg?branch=master)](https://travis-ci.org/stackbuilders/sb-debian-base)

Generic Debian image for servers. Ansible 2.2.1 is required.

## How to use this repo
First make sure you create the requirements.yml file
and add the reference to this repository, as following:

```
---
- src: git@github.com:stackbuilders/sb-debian-base.git
  scm: git
  version: remotes/origin/master
  path: external-roles
```
After that you need to run the following command:

```
ansible-galaxy install -r requirements.yml
```
## Tasks available in this repo
The current version uses Ansible flow control (when: foo is defined) to run tasks for the diferent stages but keep some useful tags like set hostname or create deploy folder.

### How to use
Create a playbook file and in roles section set the group of tasks that you need to run.
```
# site.yml
- hosts: all
  remote_user: foo
  roles:
    - { role: sb-debian-base, prebootstrap: true }
    - { role: sb-debian-base, bootstrap: true }
    - { role: sb-debian-base, basic_postgres: true }
```

Run group of task ad-hoc
```
ansible-playbook -l local -i allservers site.yml -k -u root -e "prebootstrap: true"
```
#### How to execute/run these playbooks directly
```
# Basic image
ansible-playbook -l local -i allservers site.yml -k -u root

# Administrator account
ansible-playbook -l local -i allservers site.yml -u administrator
```
The following group of tasks are available:

### Prebootstrap (prebootstrap)
This tag contains basic setup tasks, such as:
- Add administrator user
    - Default is `admin` in Debian, `ubuntu` in others. You can define the var {{ admin_user }}
- Enable default repositories for Debian
- Update packages
- Install sudo package
- Remove password for sudoers group
- Setup authorized ssh keys for administrator users
    - You need to define this file: keys/administrators

### Bootstrap (bootstrap)
This tag contains more advance setup tasks, such as:

- Disallow password authentication for SSH sessions.
- Disallow SSH access for root user
- Upgrade all packages
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
- Set time zone
- Enable NTP using systemd-timesyncd
- Enable UFW
- Open general ports ( e.g. ssh port, http port)
    - You need to define {{ ports }}
- Open specific ports for specific IPs
    - You need to define {{ port_ips }}
- This tag ensures github.com is a known host
    - You need to define {{ deploy_username }}

#### External dependencies (galaxy) included in this group of tasks bootstrap
- kamaln7.swapfile (Setup the swapfile)
    - You need to define the var {{ swap_file_size }} (e.g. 2048MB)
- nickjj.fail2ban (Install and configure fail2ban)

### Haskell build dependencies (haskell_build_dependencies)
- Install common Haskell build dependencies
    - (s.a libpcre3-dev, libsqlite3-dev, libpq-dev)

### Haskell stack (haskell_stack)
- Add FPCO PGP public key
- Add FPCO Deb repository
- Update packages cache
- Install Stack package

### Set hostname
- Set hostname to host-specific
    - You need to define {{ hostname }}
- Set hostname in the inventory
    - You need to define {{ inventory_hostname }}

### Create app directory
- name: Set up application deploy directory
    - You need to define {{ user_owner_app_directory }} and {{ user_group_app_directory }}

## Available group of tasks from external roles
### - basic_postgres
- external dependency ANXS.postgresql which installs and configures PostgreSQL, extensions, databases and users

### - nginx_https
- external dependency jdauphant.nginx to install and manage NGINX configuration

## Group of tags available for expecific tags
### - ruby-dependencies
- Install dependencies for rvm
    - (s.a. build-essential, tklib,zlib1g-dev,libssl-dev,libreadline-gplv2-dev,libxml2,libxml2-dev,libxslt1-dev)

### - add-remove-keys
- deploy listed ssh-keys into key files, first remove/add  unneeded/needed keys on keys/* folder

## Files you need to create
You should have the following list of files containing the SSH public-keys for both the administrator and deployer users, respectively.

```
keys/administrators
keys/deploy_users
```

License
-------

MIT, see the LICENSE file in this repo.

Author Information
------------------

Justin Leitgeb, Stack Builders Inc.
