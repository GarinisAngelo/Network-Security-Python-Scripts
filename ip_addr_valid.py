import sys


def ip_addr_valid(list1):

    for ip in list1:
        ip = ip.rstrip("\n")
        octet_list = ip.split(".")

        # Multicast, Broadcast and IP addresses reserved for future use: 224.x.x.x<
        # Loopback interface: 127.x.x.x
        # Windows reserved(Link-Local): 169.254.x.x

        if (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and \
           (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and (0 <= int(octet_list[1]) <= 255 and
           0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
            continue

        else:
            print("\nThere was an invalid IP address in the file: {}\n".format(ip))
            sys.exit()
