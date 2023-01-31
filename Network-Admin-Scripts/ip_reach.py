import subprocess


def ip_reach(iplist):

    while True:
        for ip in iplist:
            ip = ip.rstrip("\n")

            # Linux command
            ping_reply = subprocess.call(["ping", "-c", "2", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            # Windows command
            # ping_reply = subprocess.call("ping %s /n 2" % ip, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            if ping_reply == 0:
                print("\n--> {} is reachable.".format(ip))

            else:
                print("\n--> {} is not reachable. Check connectivity and try again.".format(ip))
