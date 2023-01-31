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


def packet_log(packet1):

    try:
        if packet1[0][1].src not in valid_ips and str(packet1[0][2].type) == '8':
            print("\n! ! ! Malicious IP Detected ! ! !\nIP Address = " + packet1[0][1].src)
    except AttributeError:
        pass


valid_ips = open("/home/agg/Desktop/IP Check/net_ips.txt").read()
valid_ips.split("\n")

print("[*] Network Scanning: Started [*]".center(os.get_terminal_size().columns))
capture = sniff(iface="enp0s8", prn=packet_log)

print("\n\nProgram terminated by the user. Now exiting...")
