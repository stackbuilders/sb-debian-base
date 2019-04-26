import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_admin_user(host):
    u = host.user('admin')

    assert u.shell == '/bin/bash'
    assert u.groups == ['admin', 'sudo']


def test_sudoers_owner(host):
    f = host.file('etc/sudoers')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.contains('NOPASSWD: ALL')


def test_admin_authorized_keys_file(host):
    f = host.file('/home/admin/.ssh/authorized_keys')

    assert f.exists
    assert f.user == 'admin'
    assert f.group == 'admin'
    assert f.contains('ADMIN_USER_1')
    assert f.contains('ADMIN_USER_2')


def test_sshd_is_installed(host):
    sshd = host.package("openssh-server")
    assert sshd.is_installed


def test_sshd_config(host):
    f = host.file('/etc/ssh/sshd_config')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.contains('PasswordAuthentication no')
    assert f.contains('PermitRootLogin no')


def test_deploy_user(host):
    u = host.user('deploy')
    assert u.shell == '/bin/bash'
    assert u.home == '/home/deploy'


def test_deploy_authorized_keys_file(host):
    f = host.file('/home/deploy/.ssh/authorized_keys')

    assert f.exists
    assert f.user == 'deploy'
    assert f.group == 'deploy'
    assert f.contains('DEPLOY_USER_1')
