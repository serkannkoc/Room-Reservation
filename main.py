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
    room_name = params.split('=')[1]
    print(room_name)
    print('start remove room')
    room_query = Query()
    if  ROOM_DB.search(room_query.name == room_name):
        ROOM_DB.remove(room_query.name == room_name)
        str = '<HTML> <HEAD> <TITLE>' + 'Room Deleted' + '</TITLE> </HEAD> <BODY>' + 'Room with name ' + room_name \
              + ' is successfully deleted.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 200 OK\n\n' + str
    else:
        str = str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Room with name ' + room_name \
                    + ' does not exists in database.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 403 Forbidden\n\n' + str

    return response

def  reserve(params):
    req_params = params.split('&')
    array = []
    for par in req_params:
        x = par.split('=')[0]
        y = par.split('=')[1]
        array.append(x)
        array.append(y)


    room_name = array[1]
    day = int(array[3])
    hour = int(array[5])
    duration = int(array[7])


    print('start remove room')
    query = Query()
    if not ROOM_DB.search(query.name == room_name):
        str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Room with name ' + room_name \
              + ' does not exists in database.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 403 Forbidden\n\n' + str
    elif day<1 or day >7:
        str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Enter day value between 1 and 7'\
              + '</BODY> </HTML>'
        response = 'HTTP/1.0 403 Forbidden\n\n' + str

    elif hour<9 or hour>17:
        str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Enter hour value between 9 and 17' \
              + '</BODY> </HTML>'
        response = 'HTTP/1.0 403 Forbidden\n\n' + str
    elif not isinstance(duration,int):
        str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Enter duration value as an integer' \
              + '</BODY> </HTML>'
        response = 'HTTP/1.0 403 Forbidden\n\n' + str
    else:
        x = ROOM_DB.search(query.name == room_name)
        print(x)
        rn = x[0].get("name")
        print(rn)
        ROOM_DB.update({'day': day,'hour':hour},query.name == room_name)
        x = ROOM_DB.search(query.name == room_name)
        print(x)

        str = str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Room with name ' + room_name \
                    + ' does not exists in database.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 403 Forbidden\n\n' + str

    return response

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
        response = remove(endpoint[1])
    elif endpoint[0] == '/reserve':
        response = reserve(endpoint[1])
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