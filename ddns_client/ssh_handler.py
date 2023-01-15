import paramiko



def setup_paramiko():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    private_key = paramiko.RSAKey.from_private_key_file('/home/ricroller/.ssh/id_rsa')
    client.connect(hostname='192.168.2.254', username='ubnt', pkey=private_key)
    return client

    
def run_show_command(client, command):
    stdin, stdout, stderr = client.exec_command(command)
    import pdb;pdb.set_trace()
    output = stdout.read().decode('utf-8')
    client.close()
    return output


def get_wan_ip():
    command_to_run = 'ip addr show eth0 | grep "inet " | awk "{print $2}"'
    run_show_command(setup_paramiko(), command_to_run)


def parse_wan_ip(ip_address_stdout):

    pass