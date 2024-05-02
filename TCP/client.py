import socket
import time
# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the server's address and port
server_address = ('localhost', 8080) # Use localhost for testing on the same machine
client_socket.connect(server_address)
try:
    while True:
        # Send fixed message to server
        message = input("Enter the message to send to server ")
        # message = "hello"
        client_socket.sendall(message.encode())
        # Receive response from server
        response = client_socket.recv(1024).decode()
        print('Server response:', response)
        # Add a delay to control the rate of sending messages
        time.sleep(1) # Adjust the delay as needed
finally:
    # Clean up the connection
    client_socket.close()