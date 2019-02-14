"""
This script has a proper function description in README.md
Be sure to check it out!

"""
import json
from modules.collect_queues import extract_queue


def handle_releng_hardware(worker_list):
    """
    Handles releng_hardware queues
    :param worker_list:
    :return:
    """
    url_list = []
    base_url = worker_list \
        .get("releng-hardware") \
        .get("base_link")

    for key in worker_list.get("releng-hardware").get("clusters"):
        url_list.append(base_url + worker_list
                        .get("releng-hardware")
                        .get("clusters")
                        .get(str(key)))

    for url in url_list:
        print("Cluster URL: ", url)
        print(extract_queue(url))


def handle_aws_provisioned_hardware(worker_list):
    """
    Handles aws-provisioned queues
    :param worker_list:
    :return:
    """
    url_list = []
    base_url = worker_list \
        .get("aws_provisioner") \
        .get("base_link")

    for key in worker_list.get("aws_provisioner").get("clusters"):
        url_list.append(base_url + worker_list
                        .get("aws_provisioner")
                        .get("clusters")
                        .get(str(key)))

    for url in url_list:
        print("Cluster URL: ", url)
        print(extract_queue(url))


def main():
    """
    Main function of the script
    :return:
    """
    try:
        provisioned_data = open("./provisioners.json").read()
        provisioned = json.loads(provisioned_data)

    except IOError:
        print("Cannot read provisioners.json file.")
        exit()

    handle_releng_hardware(provisioned)
    handle_aws_provisioned_hardware(provisioned)


if __name__ == "__main__":
    main()
