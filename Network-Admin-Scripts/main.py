import sys
import os
from ip_file_valid import ip_file_valid
from ip_addr_valid import ip_addr_valid
from ip_reach import ip_reach
# from ssh_connection import ssh_connection
# from create_threads import create_threads

os.system("clear")

ip_list = ip_file_valid()
try:
    ip_addr_valid(ip_list)
except KeyboardInterrupt:
    print("\n\nProgram terminated by the network administrator. Now exiting...\n")
    sys.exit()

try:
    ip_reach(ip_list)
except KeyboardInterrupt:
    print("\n\nProgram terminated by the network administrator. Now exiting...\n")
    sys.exit()

# create_threads(ip_list, ssh_connection)
