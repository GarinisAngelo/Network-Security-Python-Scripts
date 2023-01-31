import sys
import logging
import os

os.system("clear")
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.getLogger("scapy.interactive").setLevel(logging.ERROR)
logging.getLogger("scapy.loading").setLevel(logging.ERROR)

try:
    from scapy.all import *

except ImportError:
    print("Scapy package for Python is not installed on your system.")
    sys.exit()

subprocess.call(["ifconfig", "enp0s8", "promisc"], stdout=None, stderr=None, shell=False)

file_name = input("Please give a name to the log file: ")
sniffer_log = open(file_name, "w")
count = 1


def packet_log(packet1):

    global count
    print("------------ PACKET " + str(count) + " ------------\nTime: " + str(datetime.now().strftime("%Y.%m.%d %X %p"))
          + "\n" + packet1[0].summary() + "\n", file=sniffer_log)
    count += 1
    packet1.show()


os.system("clear")
print("[*] Started the capturing of packets...\n")

capture = sniff(iface="enp0s8", prn=packet_log)

print("\n\nPlease check the %s file to see the captured packets.\n" % file_name)

sniffer_log.close()
