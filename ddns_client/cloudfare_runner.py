#!/usr/bin/python3

import json
import requests


ZONE_ID = "e8195e5b162db5b4d1241a2725193443"

def get_api_key() -> str:
    with open("/home/ricroller/workplace/ddns_client/api_text.txt", "r") as f:
        api_key = f.read()
    return str(api_key).strip()

get_ip_url = "http://checkip.dyndns.org"

def get_wan_ipv4_ip() -> str:
    """_summary_
    handle this case
    Cell In[23], line 15, in get_wan_ipv4_ip()
     14 def get_wan_ipv4_ip() -> str:
---> 15     ipv4_address = requests.get(get_ip_url).text.split(":")[1].split("<")[0].strip()
     16     return ipv4_address

IndexError: list index out of range


    Returns:
        str: _description_
    """
    ipv4_address = requests.get(get_ip_url).text.split(":")[1].split("<")[0].strip()
    return ipv4_address

# bw.venkasandhanna.com
cloudfare_v4_url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/2fd478b05852a396feda0e6efb8cc285"

HEADERS = {
    "Authorization": f"Bearer {get_api_key()}",
    "Content-Type": "application/json"
}

ipv4_data = {
    "type": "A",
    "name": "venkasandhanna.com",
    "content": get_wan_ipv4_ip(),
    "ttl": 1,
}


def get_cloudfare_record_id() -> None:
    url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records"
    cloudfare_response = requests.get(url, headers=HEADERS)


def publish_ipv4_to_cloudfare():
    cloudfare_response = requests.put(cloudfare_v4_url, headers=HEADERS, data=json.dumps(ipv4_data))
    print(cloudfare_response)


def main():
    publish_ipv4_to_cloudfare()
    # get_cloudfare_record_id()

if __name__ == '__main__':
    main()
