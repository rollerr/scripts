import paramiko


def setup_paramiko():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    private_key = paramiko.RSAKey.from_private_key_file("/home/ricroller/.ssh/id_rsa")
    try:
        client.connect(hostname="192.168.2.254", username="ubnt", pkey=private_key)
    except paramiko.AuthenticationException:
        # TODO write test case? publish to cloudwatch
        print("Authentication failed when connecting to")
    return client


def run_show_command(client, command):
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read().decode("utf-8")
    client.close()
    return output


def get_wan_ip():
    command_to_run = 'ip addr show eth0 | grep "inet " | awk "{print $2}"'
    wan_ip = run_show_command(setup_paramiko(), command_to_run)
    wan_ip = parse_for_ipv4_address(wan_ip)
    return wan_ip


def parse_for_ipv4_address(ip_address_stdout):
    parts = ip_address_stdout.strip().split()
    ip_address = parts[1].split("/")[0]
    return ip_address
