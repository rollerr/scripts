import yaml

def convert_string_data_structure(string):
    formatted_string = ''
    if type(string) == str:
        formatted_string = [item.split('\t') for item in string.splitlines()]
    else:
        formatted_string = [item.split('\t') for item in string]
    return formatted_string


def convert_array_dict(array):
    dict_ = {}
    for element in array:
        local_device = element[0]
        local_interface = element[1].lower()
        local_ip = element[2]
        remote_neighbor = element[3]
        remote_interface = element[4].lower()
        remote_ip = element[5]

        inside_dict_local = {'name': local_interface, 'address': local_ip, 'description': '"{} | {}"'.format(remote_neighbor, remote_interface)}
        inside_dict_remote = {'name': remote_interface, 'address': remote_ip, 'description': '"{} | {}"'.format(local_device, local_ip)}

        try:
            dict_[local_device]['interfaces']
        except KeyError:
            dict_[local_device] = {'interfaces': []}
        try:    
            dict_[remote_neighbor]['interfaces']
        except KeyError:
            dict_[remote_neighbor] = {'interfaces': []}

        dict_[local_device]['interfaces'].append(inside_dict_local)
        dict_[remote_neighbor]['interfaces'].append(inside_dict_remote)

    #yaml does alphabetical sort before printing
    return (dict_, yaml.dump(dict_, default_flow_style=False))


