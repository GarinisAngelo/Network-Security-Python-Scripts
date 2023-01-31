import os.path
import sys


def ip_file_valid():

    ip_file = input("Enter the path to the IP file (example: D:\\MyFiles\\File.txt): ")
    if os.path.isfile(ip_file) is True:
        print("\n- The file was found\n")
    else:
        print("\n- The file wasn't found\n")
        sys.exit()

    selected_ip_file = open(ip_file, 'r')
    selected_ip_file.seek(0)

    ip_list = selected_ip_file.readlines()

    selected_ip_file.close()

    return ip_list
