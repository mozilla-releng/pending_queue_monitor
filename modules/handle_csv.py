import csv, json


def generate_cluster_keys(cluster_type, logger=False):
    clusters = []
    if cluster_type is "releng-hardware" or "aws_provisioner":
        for key in provisioned.get(cluster_type).get("clusters"):
            clusters.append(provisioned
                            .get(cluster_type)
                            .get("clusters")
                            .get(str(key)))
    else:
        print("No valid cluster was choosen... \nExiting...")
        exit()
    return clusters


def write_csv_file(file_name, data, provisioned, logger=False):
    clusters = []
    if file_name is "releng_hardware_data.csv":
        clusters = generate_cluster_keys("releng-hardware", logger)

    elif file_name is "aws_provisioner_data.csv":
        clusters = generate_cluster_keys("aws_provisioner", logger)
    else:
        if logger:
            print("No valid file name has been chosen... \nExiting...")
        exit()
    if clusters:
        with open(file_name, mode="w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=clusters)

            writer.writeheader()
            writer.writerow()


if __name__ == "__main__":
    try:
        provisioned_data = open("../provisioners.json").read()
        provisioned = json.loads(provisioned_data)

    except IOError:
        print("Cannot read provisioners.json file.")
        exit()

    data = "test_string"
    write_csv_file(".csv_data/test.csv", data, provisioned, logger=True)

