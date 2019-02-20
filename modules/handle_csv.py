"""
These functions handle all of the things related to the CSV files including
reading, writing and generation/updating of the CSV files.
"""
import csv


def csv_is_empty(file_name):
    with open(file_name, mode="r") as csv_file:
        csv_dict = [row for row in csv.DictReader(csv_file)]
    if len(csv_dict) == 0:
        return True


def write_header(file_name, clusters, header):
    if csv_is_empty(file_name):

        for cluster in clusters:
            header.append(cluster)

        with open(file_name, mode="w") as csv_file:
            csv_file.write(",".join(map(str, header)) + "\n")
            csv_file.close()


def generate_cluster_keys(cluster_type, provisioned, logger=False):
    """

    :param cluster_type:
    :param provisioned:
    :param logger:
    :return:
    """
    clusters = []
    if cluster_type == "releng-hardware" or cluster_type == "aws_provisioner":
        for key in provisioned.get(cluster_type).get("clusters"):
            clusters.append(provisioned
                            .get(cluster_type)
                            .get("clusters")
                            .get(str(key)))
    else:
        if logger:
            print("No valid cluster was chosen... \nExiting...")
        exit()
    return clusters


def write_csv_file(file_name, data, provisioned, logger=False):
    """

    :param file_name: file that needs to be written to.
    :param data: needs to be a dictionary with the proper keys.
    :param provisioned: configuration file.
    :param logger:
    :return:
    """
    clusters = []

    if file_name == "./csv_data/releng_hardware_data.csv":
        clusters = generate_cluster_keys("releng-hardware", provisioned,
                                         logger)

    elif file_name == "./csv_data/aws_provisioner_data.csv":
        clusters = generate_cluster_keys("aws_provisioner", provisioned,
                                         logger)
    else:
        if logger:
            print("No valid file name has been chosen... \nExiting...")
        exit()

    header = ["date", ]
    if clusters:
        write_header(file_name, clusters, header)
        pass

    for cluster in clusters:
        header.append(cluster)

    with open(file_name, mode="a") as csv_file:
        csv_file.write(",".join(map(str, data)) + "\n")
        csv_file.close()
