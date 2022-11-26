import os
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('dns-server-slave-1')
    
def test_bind9_is_installed(host):
    bind9 = host.package('bind9')
    assert bind9.is_installed
    assert bind9.version.startswith('1:9.16.1')

def test_bind9_is_running_and_enabled(host):
    bind9 = host.service('bind9')
    assert bind9.is_running
    assert bind9.is_enabled

def test_bind9_is_configured_as_slave(host):
    file = host.file('/etc/bind/named.conf.local').contains('slave')
    assert file
