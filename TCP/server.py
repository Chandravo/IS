import socket
# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the address and port
server_address = ('localhost', 8080) # Use localhost for testing on the same machine
server_socket.bind(server_address)
# Listen for incoming connections
server_socket.listen(1)
print('Server is running and waiting for connections...')
# Accept a connection
connection, client_address = server_socket.accept()
try:
    print('Connection from', client_address)
    while True:
        # Receive data from the client
        data = connection.recv(1024).decode()
        if data:
            print('Received:', data)
        if data.lower() == 'exit':
            print('Client has exited. Closing connection...')
            break
        # Send response back to client
        message = input('Enter response message: ')
        connection.sendall(message.encode())
finally:
    # Clean up the connection
    connection.close()