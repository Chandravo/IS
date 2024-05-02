# clientUDP.py
import socket
import time
# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Server address and port
server_address = ('localhost', 8080) # Use localhost for testing on the same machine
try:
    while True:
    # Send message to server
        # message = input("Enter the message to send to server ")
        message = "hello"
        client_socket.sendto(message.encode(), server_address)
        # Receive response from server
        response, _ = client_socket.recvfrom(1024)
        print('Server response:', response.decode())
        # Add a delay to control the rate of sending messages
        time.sleep(1)
finally:
    # Clean up the connection
    client_socket.close()