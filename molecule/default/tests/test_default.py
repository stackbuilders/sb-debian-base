import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_admin_authorized_keys(host):
    f = host.file('/home/admin/.ssh/authorized_keys')

    assert f.exists
    assert f.user == 'admin'
    assert f.group == 'admin'
    assert f.contains('ADMIN_USER_1')
    assert f.contains('ADMIN_USER_2')
