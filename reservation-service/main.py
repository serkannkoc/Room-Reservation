import socket
import reservation_controller

def handle_request(request,addr,conn):
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

    # Check the endpoint and call the appropriate function from the reservation_controller module
    if endpoint[0] == '/reserve':
        response = reservation_controller.reserve(endpoint[1],addr,conn)
    elif endpoint[0] == '/listavailability':
        response = reservation_controller.list_availability(endpoint[1],addr,conn)
    elif endpoint[0] == '/display':
        response = reservation_controller.display(endpoint[1],conn)
    else:
        # Return a bad request response if the endpoint is invalid
        response = 'HTTP/1.0 400 Bad Request\n\n Wrong endpoint!!'

    # Return the response
    return response






# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 7004

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
    response = handle_request(request,client_address,client_connection)

    #client_connection.sendall(response.encode())

    # Close connection
    client_connection.close()

# Close socket
server_socket.close()