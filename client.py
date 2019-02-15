"""
This script has a proper function description in README.md
Be sure to check it out!

"""
import json
import time
from modules.handle_hardware import handle_releng_hardware, \
    handle_aws_provisioned_hardware


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
    while True:
        main()
        time.sleep(120)