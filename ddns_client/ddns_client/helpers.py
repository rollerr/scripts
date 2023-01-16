import yaml


def get_private_key():
    with open('settings.yaml', 'r') as settings_file:
        private_key_path = yaml.loads(settings_file.read())
        return private_key_path['ssh_settings']['private_key_file']
