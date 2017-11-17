# CHANGELOG

## MASTER

## 1.4.5
* Move groups of tasks from the main bootstrap file to individual files.
* Store journald data persistently on storage.

## 1.4.4
* Make sure D-Bus is present before executing commands that need it.

## 1.4.3
* Use a task to restart the SSH server instead of a handler.

## 1.4.2
* Fix deprecation warnings for using include.

## 1.4.1
* Move GitHub known host to the varible sb_debian_base_known_host

## 1.4.0
* Remove rvm dependecies instalation task.

## 1.3.4
* Fix deprecation warning about using remote_user as a role parameter

## 1.3.3
* Added sb_debian_base_supplementary_packages variable to allow the installation of more packages additionally to sb_debian_base_extra_packages

## 1.3.2
* Don't disable IPv6 connections on Debian's firewall
* Minor cleanups

## 1.3.1
* Add support for Debian 9 "Stretch"
* Fix Galaxy tag

## 1.3.0
* Use variables instead of files to configure SSH private and authorized keys for `admin` and `deploy` users.
  * Read `admin` user SSH authorized keys from `sb_debian_base_admin_user_authorized_keys` variable.
  * Read `deploy` user SSH private key from `sb_debian_base_deploy_user_private_key` variable.
  * Read `deploy` user SSH authorized keys from `sb_debian_base_deploy_user_authorized_keys` variable.
* Definitive fix for sb_debian_base_deploy_user default value.
* Add galaxy_tags to meta/main.yml
* Fix typo on platform for Debian 'Jessie' name.
* Remove unused role dependecies (jdauphant.ssl-certs, jdauphant.nginx,
  ANXS.postgresql).

## 1.2.2
* Add cache_valid_time to apt upgrade
* Remove duplicate code for updating SSH keys
* Fix sb_debian_base_deploy_user default value

## 1.2.1
* Fix disabling of firewall
* Use the same boolean form consistently

## 1.2.0
* Variable names are now standardized, prefixed with `sb_debian_base_`.
* UFW task can now be disabled setting `sb_debian_base_firewall` to `no`
* By default email alerts will be send to the admin user on the localhost.
* Fix for Unix deploy group variable name
* Fix two variables in tests
* Simplify and order task's filenames
* README.md updates

## 1.1.5
* This Galaxy is now tested on every commit running against Docker containers on Travis
* The supported platforms are now `Debian 8 "Jessie"`, `Ubuntu 14.04 "Trusty"` and `Ubuntu 16.04 "Xenial"`.
* The time zone is now set using the Ansible module `timezone` (requieres Ansible 2.2).
* Ansible 2.2.1 is now required.

## 1.1.4
* Remove atsar from the default package installation list (not available in Ubuntu).
* Fix an Ansible warning
* Use a more legible YAML format
* Remove duplicate code

## 1.1.3
* Move the list of extra installed packages to the `defaults` directory.
  * Add `tree` and `bash-completion` packages.

## 1.1.2
* Use fixed version of the external dependencies.

## 1.1.1
* This release includes a fix for amazon machine images:
  * Make sure that the admin ssh keys are present in the bootstrap section.

## 1.1.0
* This release includes:
  * systemd-timesyncd as NTP client (removing geerlingguy.ntp dependency)
  * Code cleanup
  * Minor bug fixes

## 1.0.2
* Fix typo in variable name.

## 1.0.1
* Fix `deploy_username` tasks that were running when `deploy_usename` was not defined.

## 1.0.0

* This version contains:
  * Use control execution flow instead of tags.
  * Update tasks to use Ansible 2.0+

* To improve the compatibility with AWS and Ubuntu, this version includes some
  tweaks also changes the default `admin_user` from `administrator` to `admin` and
  is now set as a default variable.

## 0.0.2
* Compatible with Ansible version 1.9.

## 0.0.1 First release
* First release that packages this base package as a proper external role.
