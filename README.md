**Warning:** This library has been deprecated and is no longer maintained. It will not receive any further security patches, features, or bug fixes and is preserved here at GitHub for archival purposes. If you want to use it, we suggest forking the repository and auditing the codebase before use. For more information contact us at info@stackbuilders.com.

**Recommended Roles:**

- https://github.com/dev-sec/ansible-collection-hardening

# Stack Builders - Debian Base

[![Build Status](https://travis-ci.org/stackbuilders/sb-debian-base.svg?branch=master)](https://travis-ci.org/stackbuilders/sb-debian-base)
[![Ansible Galaxy](https://img.shields.io/badge/role-sb--debian--base-blue.svg)](https://galaxy.ansible.com/stackbuilders/sb-debian-base/)

Generic Debian image for servers. This Galaxy requires Ansible 2.7.0

## Supported Platforms

- Debian
  - 10 (buster)
  - 9  (stretch)

- Ubuntu
  - 18.04 (bionic)
  - 16.04 (xenial)

## BREAKING CHANGES:
* Haskell tasks were removed from this role so `install_haskell_stack` and
  `install_haskell_dependencies` variables for calling haskell installation
  tasks are no longer being used.

## How to use this role
The current version uses Ansible flow control (when: foo is defined) to run 
tasks for the different stages, but it keeps some useful tags like to set the
hostname or create the deploy directory.

First make sure you create the `requirements.yml` file and add the reference
to this repository, as following:
```yaml
---
- src: git@github.com:stackbuilders/sb-debian-base.git
  version: <tag, commit or branch>
  path: external-roles
```
After that, you need to run the following command:
```
ansible-galaxy install -r requirements.yml
```

### Create a playbook
Create a playbook file and in the roles section set the group of tasks that
you need to run. As an example you can use `tests/site.yml` or the one below:

```yaml
# site.yml
- hosts: all
  remote_user: foo
  vars:
    sb_debian_base_admin_user_authorized_keys:
      - ssh-rsa AAAAB3NzaC1yc1E ADMIN_USER_1
      - ssh-rsa AAAAB3Nzac2Yc2e ADMIN_USER_2
    sb_debian_base_deploy_user_authorized_keys:
      - ssh-rsa AAAAB3NzaC1yc1E DEPLOY_USER_1
      - ssh-rsa AAAAB3Nzac2Yc2e DEPLOY_USER_2
  roles:
    - role: sb-debian-base
      prebootstrap: yes
    - role: sb-debian-base
      bootstrap: yes
      add_remove_keys: yes
      vars:
        sb_debian_base_deploy_user: deployer
        sb_debian_base_supplementary_packages: [ "pkg-config", "traceroute" ]
        sb_debian_base_environment_variables:
          ONE: "uno"
          TWO: "dos"
```

You can also run ad-hoc tasks, although it's not the recommended way:
```
ansible-playbook -l local -i hosts site.yml -k -u root -e "prebootstrap: yes"
```

Run the playbook this way:
```
# Basic image
ansible-playbook -l local -i hosts site.yml -k -u root

# Administrator account
ansible-playbook -l local -i hosts site.yml -u administrator
```

## The following groups of tasks are available:

### Prebootstrap (prebootstrap)
This tag contains basic setup tasks, such as:
- Add administrator user
    - Default is `admin` in Debian, `ubuntu` in Ubuntu. You can define
      the variable {{ sb_debian_base_admin_user }}
- Update packages cache
- Install sudo package
- Use sudo without a password for the sudo group
- Set up authorized SSH keys for administrator users
    - You need to define {{ sb_debian_base_admin_user_authorized_keys }}

### Bootstrap (bootstrap)
This tag contains more advance setup tasks, such as:

- Disallow password authentication for SSH sessions
- Disallow SSH access for root user
- Set hostname
    - You can define {{ hostname }}
- Set time zone
    - You can define {{ sb_debian_base_ntp_timezone }}
- Enable NTP using systemd-timesyncd
- Make sure to store journald data persistently
- Upgrade all packages
- Install basic packages
    - e.g.: vim, tmux, htop, atop, tree, ufw, emacs, git, curl
- Install supplementary packages - not just sb_debian_base_extra_packages
- Enable firewall using UFW
    - Open general ports (e.g. SSH port, HTTP port; by default SSH)
        - You can define {{ ports }}
    - Open specific ports for specific IPs
        - You can define {{ port_ips }}
    - You can disable UFW with `sb_debian_base_firewall: no`
- Set and update environment variables
    - You need to define {{ sb_debian_base_environment_variables }}
- Create Unix user and group for deployer user
    - You need to define the var {{ sb_debian_base_deploy_user }}
      (e.g. deployer)
    - Optionally define the var {{ sb_debian_base_deploy_user_group }}
      (e.g. deployer) otherwise, it will be the same as
      {{ sb_debian_base_deploy_user }}
- Create application deploy directory
- Add SSH keys for GitHub's «Deploy keys»
- Set up authorized SSH keys for the deployer user
    - You need to define {{ sb_debian_base_deploy_user_authorized_keys }}
- Ensure github.com is a known host
    - You need to define {{ sb_debian_base_deploy_user }}
    - This variable adds by default GitHub as a known host, but it's possible
      to change it overwriting {{ sb_debian_base_known_hosts }}
- Set global bash history configuration to the format bellow:
    `285  Thu 08 Aug 2019 01:43:40 PM UTC some comand`
    See bellow for available variables.

#### Set hostname (set-hostname)
- Set hostname to host-specific variable
    - You need to define {{ hostname }}

#### Set bash history configuration:
- Enable/disable the history configuration
  `sb_debian_base_bash_history: true`
    
- Under `sb_debian_base_bash_history_config:`
  - Set the amount of lines to keep in the history buffer
    `histsize: '5000'`
  - Set the amount of lines to keep in the history file
    `histfilesize: '3000'`
  - Set the time format to append before each history command (see
    `man history` for complete options)
    `histtimeformat: '%c%t'`


#### Create app directory (create-app-directory)
- Create the application deploy directory
    - When {{ sb_debian_base_deploy_user }} is defined

#### External dependencies (Galaxies) included in this group of bootstrap tasks
- kamaln7.swapfile (Set up the swapfile)
    - You can define the var {{ sb_debian_base_swap_file_size }} (e.g. 2048MB)
- Install unattended-upgrades for security patches only
    - You can define the var {{ sb_debian_base_uu_email_alerts }} (e.g.
      example@example.com)

### Update authorized SSH keys (add-remove-keys)
- Updates SSH authorized keys:

    - You need to define the following list of variables containing the SSH
      public-keys for both the administrator and the deploy users respectively:

```
{{ sb_debian_base_admin_user_authorized_keys }}
{{ sb_debian_base_deploy_user_authorized_keys }}
```

License
-------

MIT, see the [LICENSE](LICENSE) file in this repository.

Author Information
------------------

Justin Leitgeb, Stack Builders Inc.
