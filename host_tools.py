#!/usr/bin/env python2.7

import argparse

from paramiko import AutoAddPolicy, SSHClient
from paramiko.ssh_exception import SSHException
from pysnmp.entity.rfc3413.oneliner import cmdgen
from scp import SCPClient

#move to yaml
snmp_pass = 'CLEARPASS'
hostname_mib = 'iso.3.6.1.2.1.1.5.0'
username = 'vyos'
password = 'vyos'
filename =  '/home/ubuntu/.ssh/id_rsa_orch.pub'
remote_path = '/tmp'


class CouldNotConnect(Exception):
    pass


def validate_host_snmp(hostname):
    '''
    Assert that what SNMP returns matches the IP address
    '''

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
    cmdgen.CommunityData(snmp_pass),
    cmdgen.UdpTransportTarget((hostname, 161)),
    hostname_mib)

    if varBinds:
        mib, hostname_new = [(name.prettyPrint(), value.prettyPrint()) for name, value in varBinds][0]
        return hostname_new

    raise CouldNotConnect
    

def setup_argparse():

    parser = argparse.ArgumentParser()
    parser.add_argument('--validate', help='Validate hosts', action='store_true')
    parser.add_argument('--transfer', help='Validate hosts', action='store_true')
    parser.add_argument('--host', help='Name of host to update')

    return parser.parse_args()


def transfer_pub_key(hostname, filename, remote_path):
    assert_host_snmp(hostname)
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    try:
        ssh.connect(hostname, username=username, password=password)

        scp = SCPClient(ssh.get_transport())
        print('Transferring files to {}'.format(hostname))
        scp.put(files=filename, remote_path=remote_path)

        ssh.close()
    except SSHException as e:
        print("Could not connect to: {} over 22. Error: {}".format(hostname, e))


def assert_host_snmp(hostname):

    try:
        returned_hostname_snmp = validate_host_snmp(hostname)
        assert hostname == returned_hostname_snmp           
        print('Hostname: {} matches'.format(hostname))
    except AssertionError:
        print('Warning returned hostname {} does not match supplied hostname {}'.format(returned_hostname_snmp, hostname))
    except CouldNotConnect:
        print('Error. Couldn\'t connect to {}. Is the SNMP community defined?'.format(hostname))


def main():

    args = setup_argparse()

    if not args.host:

        with open('/etc/hosts') as f:
            for line in f:
                line = line.strip()
                if line.startswith('10'):
                    ip_address, hostname  = line.split()

                    if args.validate:
                        assert_host_snmp(hostname)
                    if args.transfer:
                        transfer_pub_key(hostname, filename, remote_path)
        print('Exiting')
        exit(0)
    if not args.validate:
        transfer_pub_key(args.host, filename, remote_path)
        exit(0)
    assert_host_snmp(args.host)
     

if __name__ == '__main__':
    main()

