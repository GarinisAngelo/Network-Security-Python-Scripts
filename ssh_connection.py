import os.path
import sys
import paramiko
import time
import re


# Username/Password file validation
user_file = input("\nEnter the path to the User file (example: D:\\MyFiles\\File.txt): ")
if os.path.isfile(user_file) is True:
    print("\n- Username and password file is valid.")
else:
    print("\n- File {} doesn't exist. Try again.".format(user_file))
    sys.exit()

# Commands file validation
cmd_file = input("\nEnter the path to the Commands file (example: D:\\MyFiles\\File.txt): ")
if os.path.isfile(cmd_file) is True:
    print("\n- Commands file is valid. Sending command(s) to device(s)...")
else:
    print("\n- File {} doesn't exist. Try again.".format(cmd_file))
    sys.exit()


# SSH connection to the device
def ssh_connection(ip):
    global user_file
    global cmd_file

    try:
        selected_user_file = open(user_file, 'r')
        selected_user_file.seek(0)
        username = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")
        selected_user_file.seek(0)
        password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")

        # Logging into device
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username, password=password)

        # Starting an interactive shell session on the router
        connection = session.invoke_shell()

        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)

        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)

        selected_cmd_file = open(cmd_file, 'r')
        selected_cmd_file.seek(0)

        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + '\n')
            time.sleep(2)

        selected_user_file.close()
        selected_cmd_file.close()

        # Checking command output for IOS syntax errors
        router_output = connection.recv(65535)

        if re.search(b"% Invalid input", router_output):
            print("There was at least one IOS syntax error on device {}".format(ip))
        else:
            print("\nDONE for device {}".format(ip))
            
            # Command output
            # print(re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", str(router_output))[1])
            # print(str(router_output) + "\n")
                
        # Closing the connection
        session.close()

    except paramiko.AuthenticationException:
        print("Invalid username or password\nPlease check the username/password file or the device configuration.")
        print("Closing program...")
