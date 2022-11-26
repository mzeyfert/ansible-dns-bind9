import os
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('dns-client-1')
    
def test_nslookup_on_client(host):
    hostnames = [
        'dns-server-master',
        'dns-server-slave-1',
        'dns-client-1',
    ]
    for hostname in hostnames:
        cmd = host.run(f'nslookup {hostname}.example.tech')
        assert cmd.succeeded