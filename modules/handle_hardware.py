import datetime
from modules.collect_queues import extract_queue
from modules.handle_csv import write_csv_file
from modules import config


def handle_releng_hardware(worker_list):
    """
    Handles releng_hardware queues
    :param worker_list:
    :return:
    """
    url_list = []
    cluster_list = ["date"]
    response_list = [str(datetime.datetime.utcnow())]

    base_url = worker_list \
        .get("releng-hardware") \
        .get("base_link")

    for key in worker_list.get("releng-hardware").get("clusters"):
        cluster_list.append(worker_list
                            .get("releng-hardware")
                            .get("clusters")
                            .get(str(key)))

        url_list.append(base_url + worker_list
                        .get("releng-hardware")
                        .get("clusters")
                        .get(str(key)))

    for url in url_list:
        if config.VERBOSE:
            print("Working on:", url)
        response_list.append(extract_queue(url))

    if config.VERBOSE:
        print("Cluster list", cluster_list)
        print("Response list", response_list)

        response_dictionary = {cluster: response for cluster, response in
                               zip(cluster_list, response_list)}
        print("Response dictionary:", response_dictionary)

    write_csv_file("./csv_data/releng_hardware_data.csv", response_list,
                   worker_list, True)


def handle_aws_provisioned_hardware(worker_list):
    """
    Handles aws-provisioned queues
    :param worker_list:
    :return:
    """
    url_list = []
    cluster_list = ["date"]
    response_list = [str(datetime.datetime.utcnow())]

    base_url = worker_list \
        .get("aws_provisioner") \
        .get("base_link")

    for key in worker_list.get("aws_provisioner").get("clusters"):
        cluster_list.append(worker_list
                            .get("aws_provisioner")
                            .get("clusters")
                            .get(str(key)))

        url_list.append(base_url + worker_list
                        .get("aws_provisioner")
                        .get("clusters")
                        .get(str(key)))

    for url in url_list:
        if config.VERBOSE:
            print("Working on:", url)
        response_list.append(extract_queue(url))

    if config.VERBOSE:
        print("Cluster list", cluster_list)
        print("Response list", response_list)

        response_dictionary = {cluster: response for cluster, response in
                               zip(cluster_list, response_list)}

        print("Response dictionary:", response_dictionary)

    write_csv_file("./csv_data/aws_provisioner_data.csv", response_list,
                   worker_list, True)
