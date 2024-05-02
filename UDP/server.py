import socket
# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Server address and port
server_address = ('localhost', 8080) # Use localhost for testing on the same machine
# Bind the socket to the address and port
server_socket.bind(server_address)
print('Server is running and waiting for connections...')
try:
    while True:
        # Receive data from the client
        data, client_address = server_socket.recvfrom(1024)
        print('Connection from', client_address)
        if data:
            print('Received:', data.decode())
        if data.decode().lower() == 'exit':
            print('Client has exited. Closing connection...')
            break
        # Send response back to client
        message = input('Enter response message: ')
        server_socket.sendto(message.encode(), client_address)
finally:
    # Clean up the connection
    server_socket.close()
