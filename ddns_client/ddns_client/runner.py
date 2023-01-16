import click
import json
import requests

from ddns_client.ssh_handler import get_wan_ip


class CloudfareExecutionContext:
    def __init__(self, api_key_file: str):
        self.api_key_file = api_key_file
        self.zone_id = "e8195e5b162db5b4d1241a2725193443"
        self.record_id = "2fd478b05852a396feda0e6efb8cc285"
        self.cloudfare_root_record = f"https://api.cloudflare.com/client/v4/zones/{self.zone_id}/dns_records/{self.record_id}"
        self.api_key = self.get_api_key(api_key_file)
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        self.ipv4_data = {
            "type": "A",
            "name": "venkasandhanna.com",
            "content": "",
            "ttl": 1,
        }

    def publish_ipv4_to_cloudfare(self) -> None:
        cloudfare_response = requests.put(
            self.cloudfare_root_record,
            headers=self.headers,
            data=json.dumps(self.ipv4_data),
        )
        print(cloudfare_response)

    def get_cloudfare_record_id(self, record=None) -> None:
        url = self.cloudfare_root_record
        cloudfare_response = requests.get(url, headers=self.headers)
        return cloudfare_response

    def get_api_key(self, api_key_file) -> str:
        with open(api_key_file, "r") as f:
            api_key = f.read()
        return str(api_key).strip()


def check_for_ipv4_change(cloudfare_client: CloudfareExecutionContext) -> bool:
    wan_ipv4_ip = get_wan_ip()
    cloudfare_response = cloudfare_client.get_cloudfare_record_id()
    if cloudfare_response.status_code == 200:
        cloudfare_response = cloudfare_response.json()
        cloudfare_ipv4 = cloudfare_response["result"]["content"]
        if wan_ipv4_ip != cloudfare_ipv4:
            cloudfare_client.ipv4_data["content"] = wan_ipv4_ip
            # cloudfare_client.publish_ipv4_to_cloudfare()
            return True
        else:
            return False
    else:
        print("uh oh")
        # publish_logs_to_aws()
        return False


@click.command()
@click.option("--key-file", "-k", default="/home/ricroller/api_text.txt")
def main(key_file):
    cloudfare_client = CloudfareExecutionContext(key_file)
    check_for_ipv4_change(cloudfare_client)
    # publish_ipv4_to_cloudfare()
