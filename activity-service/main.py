import socket
import activity_controller

def handle_request(request):
    """Handles the HTTP request."""

    headers = request.split('\n')
    endpoint = headers[0].split()[1].split('?')
    print("endpoint ->>")
    print(endpoint)
    print("headers[0].split() ->>")
    print(headers[0].split())

    if endpoint[0] == '/add':
        response = activity_controller.add(endpoint[1])
    elif endpoint[0] == '/remove':
        response = activity_controller.remove(endpoint[1])
    elif endpoint[0] == '/check':
        response = activity_controller.check(endpoint[1])
    else:
        response = 'HTTP/1.0 400 Bad Request\n\n Wrong endpointhjfhjgfjfghjfghjfghj!!'


    return response



# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 7003

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)

print('Listening on port %s ...' % SERVER_PORT)

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # Return an HTTP response
    response = handle_request(request)

    client_connection.sendall(response.encode())

    # Close connection
    client_connection.close()

# Close socket
server_socket.close()