from scapy.layers.inet import IP, UDP
import time
from scapy.sendrecv import send

server_ip = '127.0.0.1'
server_port = 8080
client_ip = '127.0.0.2'
client_port = 3000
payload = b'\x01\x0f'

packet = IP(dst=server_ip, src=client_ip) / UDP(sport=client_port, dport=server_port) / payload

while True:
  send(packet)
  time.sleep(1)