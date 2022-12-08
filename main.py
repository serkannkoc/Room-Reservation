import socket
from room import Room
from tinydb import TinyDB, Query
ROOM_DB = TinyDB('room.json')


def  add(params):
    room_name = params.split('=')[1]
    print(room_name)
    print('start add room')
    room_query = Query()
    if not ROOM_DB.search(room_query.name == room_name):
        room = Room(room_name).__dict__
        ROOM_DB.insert(room)
        str = '<HTML> <HEAD> <TITLE>'+ 'Room Added' +'</TITLE> </HEAD> <BODY>' + 'Room with name '+ room_name \
              +' is successfully added.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 200 OK\n\n' + str
    else:
        str = str = '<HTML> <HEAD> <TITLE>'+ 'Error' +'</TITLE> </HEAD> <BODY>' + 'Room with name '+ room_name \
              +' already exists in database.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 403 Forbidden\n\n' + str
    print('end add room')
    return response


def  remove(params):
    print('handling remove')

def  reserve(params):
    print('handling reserve')

def  chechk_availability(params):
    print('handling checking availability')
def handle_request(request):
    """Handles the HTTP request."""

    headers = request.split('\n')
    filename = headers[0].split()[1]
    endpoint = headers[0].split()[1].split('?')
    print(endpoint)
    print(headers[0].split())

    if endpoint[0] == '/add':
        response = add(endpoint[1])
    elif endpoint[0] == '/remove':
        remove(endpoint[1])
    elif endpoint[0] == '/reserve':
        reserve(endpoint[1])
    elif endpoint[0] == '/checkavailability':
        chechk_availability(endpoint[1])
    else:
        response = 'HTTP/1.0 400 Bad Request\n\n Wrong endpoint!!'


    return response



# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

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