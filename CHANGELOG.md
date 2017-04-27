# CHANGELOG

## MASTER
* Move the list of extra installed packages to defaults directory, and add 'tree'.

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
