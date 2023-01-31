By executing the main.py script, the network administrator can check if all the IPs that he has set for his machines inside the network are responding,
meaning that they are connected successfully to the network.

The first method that is called is the ip_file_valid() which reads a txt file containing the IPs of the network and saves them in a list.

Then ip_addr_valid() checks if the IPs inside the returned list are of correct format and validity.

Finally ip_reach() sends out 2 ping requests for every IP in the list and if both requests return a response, then is prints a message of a success.
Otherwise it informs the network admin that this IP didnt respond and he should check the connectivity.


By executing the ip_detect.py script, the network administrator can monitor the traffic inside the network and check if all the IPs that are requesting and sending 
packets are the ones that he has set as valid when he built the network.

Using the tool "Scapy" this script checks all the packet IPs that are sent or received to see if they are supposed to be in his network. If an IP that is trading packets
is not supposed to be in his network, then a warning is displayed showing the malicious IP so that he can take actions against it.
