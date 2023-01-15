import param
from mock import parametrize
from ssh_handler import setup_paramiko, run_show_command, get_wan_ip, parse_wan_ip


@parametrize.parametrize('host, port, user, password, key_filename, timeout, expected', [

    
    

def test_ssh

test_1 = '    inet 70.106.247.115/24 brd 70.106.247.255 scope global eth0\n'


@parametrize
def test_parse_wan_ip():

    
import unittest

class TestIPCommand(unittest.TestCase):

    def test_ip_address(self):
        output = '    inet 70.106.247.115/24 brd 70.106.247.255 scope global eth0\n'
        ip_address = '70.106.247.115'
        netmask = '24'
        broadcast = '70.106.247.255'
        self.assertIn(ip_address, output)
        self.assertIn(netmask, output)
        self.assertIn(broadcast, output)
        
    def test_interface_name(self):
        output = '    inet 70.106.247.115/24 brd 70.106.247.255 scope global eth0\n'
        interface_name = 'eth0'
        self.assertIn(interface_name, output)
        
    def test_scope(self):
        output = '    inet 70.106.247.115/24 brd 70.106.247.255 scope global eth0\n'
        scope = 'global'
        self.assertIn(scope, output)
        
    def test_output_format(self):
        output = '    inet 70.106.247.115/24 brd 70.106.247.255 scope global eth0\n'
        parts = output.split()
        self.assertEqual(parts[0], 'inet')
        self.assertEqual(parts[-2], 'global')
        self.assertEqual(parts[-1