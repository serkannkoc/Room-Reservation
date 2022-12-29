import socket
import activity_controller

# This function handles the HTTP request
def handle_request(request):
    """Handles the HTTP request."""

    # Split the request into separate lines and extract the endpoint
    headers = request.split('\n')
    endpoint = headers[0].split()[1].split('?')

    # Print the endpoint for debugging purposes
    print("endpoint ->>")
    print(endpoint)

    # Print the headers[0].split() list for debugging purposes
    print("headers[0].split() ->>")
    print(headers[0].split())

    # Check the endpoint and call the appropriate function from the activity_controller module
    if endpoint[0] == '/add':
        response = activity_controller.add(endpoint[1])
    elif endpoint[0] == '/remove':
        response = activity_controller.remove(endpoint[1])
    elif endpoint[0] == '/check':
        response = activity_controller.check(endpoint[1])
    else:
        # Return a bad request response if the endpoint is invalid
        response = 'HTTP/1.0 400 Bad Request\n\n Wrong endpoint!!'

    # Return the response
    return response


# Define the socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 7003

# Create the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the REUSEADDR socket option to 1 to allow the socket to be bound to an address that is already in use
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the host and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Start listening for client connections
server_socket.listen(1)

# Print a message to let the user know the server is listening
print('Listening on port %s ...' % SERVER_PORT)

# Run the server indefinitely
while True:
    # Wait for a client connection
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # Handle the request and get the response
    response = handle_request(request)

    # Send the response to the client
    client_connection.sendall(response.encode())

    # Close the client connection
    client_connection.close()

# Close the server socket
server_socket.close()
