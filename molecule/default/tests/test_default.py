import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_admin_user(host):
    u = host.user('admin')

    assert u.shell == '/bin/bash'
    assert u.groups == ['admin', 'sudo']


def test_admin_authorized_keys_file(host):
    f = host.file('/home/admin/.ssh/authorized_keys')

    assert f.exists
    assert f.user == 'admin'
    assert f.group == 'admin'
    assert f.contains('ADMIN_USER_1')
    assert f.contains('ADMIN_USER_2')


def test_bash_history_config(host):
    f = host.file('/home/admin/.bashrc')

    assert f.exists
    assert f.contains('HISTSIZE=6000')
    assert f.contains('HISTFILESIZE=3000')
    assert f.contains('HISTTIMEFORMAT=%c%t')
