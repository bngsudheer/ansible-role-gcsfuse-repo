import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_repo_exists(host):
    repo = host.file('/etc/yum.repos.d/gcsfuse.repo')
    assert repo.exists == True
    assert repo.is_file == True
    assert repo.contains('packages.cloud.google.com/yum/repos/gcsfuse-el7-x86_64')


def test_package(host):
    package = host.package("gcsfuse")
    assert package.is_installed
