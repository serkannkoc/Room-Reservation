from tinydb import TinyDB, Query
from reservation import Reservation
import reservation_http_messages
import uuid
Reservation_DB = TinyDB('reservation_db.json')

reservation_query = Query()

import socket


def list_availability(params,client_address,client_connection):
    # Split the params string into a list of key-value pairs
    req_params = params.split('&')

    # Create an empty list to store the extracted params
    array = []

    # Iterate over the list of key-value pairs
    for par in req_params:

        # Split each key-value pair into separate key and value strings
        x = par.split('=')[0]
        y = par.split('=')[1]
        # Add the key and value to the array
        array.append(x)
        array.append(y)

    # Get the room name from the array
    room_name = array[1]

    #if day value is in the array
    if (len(array) >2) :

        #initialize the day value from array
        day = int(array[3])

        # create the socket
        sockRoom = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the room server
        sockRoom.connect(('0.0.0.0', 7005))

        #initialize the request to send room controller
        request_message = f"GET /checkavailability?name={room_name}&day={day} HTTP/1.1\r\nHost: 0.0.0.0\r\n\r\n"

        print(request_message)
        #send request to room socket
        sockRoom.send(request_message.encode())

        # get reply from the room server
        replyRoom = sockRoom.recv(1024)

        #send reply to client
        client_connection.send(replyRoom)

    else:
        # if the day value not given
        day = 1
        #initialize the reply value as empty string
        replyRoom = ""

        #iterate all days
        while day < 7:

            #create a new socket
            sockRoom = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Connect to the server
            sockRoom.connect(('0.0.0.0', 7005))
            #initialize the request message
            request_message = f"GET /checkavailability?name={room_name}&day={day} HTTP/1.1\r\nHost: 0.0.0.0\r\n\r\n"

            #send request message to room server
            sockRoom.send(request_message.encode())

            #get reply from the room server
            replyRoomString = sockRoom.recv(1024)

            #decode reply string from byte to string and replace the new line character with its string value
            replyRoom = replyRoom +replyRoomString.decode().replace('\n','\\n')

            # if reply contains '403' break
            if replyRoom.find('403') != -1:
                break

            #update the day value
            day = day + 1

        #clear the http  OK status from the reply if any
        replyRoom = replyRoom.replace('HTTP/1.0 200 OK\\n\\n',"")

        # clear the http Forbidden status if any
        replyRoom = replyRoom.replace('HTTP/1.0 403 Forbidden\\n\\n',"")

        #clear the html tag at the end of the http message
        replyRoom = replyRoom.replace('</HTML>', '')

        #concenate string with the html opening and closing tags
        replyRoom = '<HTML>' + replyRoom + '</HTML>'

        # add new line tag to print entries as a list
        replyRoom = replyRoom.replace('</BODY>','<br></BODY>')

        #add http OK message in front of the reply
        replyRoom = 'HTTP/1.0 200 OK\n\n' + replyRoom

        #send reply to the client
        client_connection.send(replyRoom.encode())

        return

    return


def reserve(params,client_address,client_connection):
        # Split the params string into a list of key-value pairs
        req_params = params.split('&')

        # Create an empty list to store the extracted params
        array = []

        # Iterate over the list of key-value pairs
        for par in req_params:
            # Split each key-value pair into separate key and value strings
            x = par.split('=')[0]
            y = par.split('=')[1]
            # Add the key and value to the array
            array.append(x)
            array.append(y)

        # Get the room name from the array
        room_name = array[1]

        #get the activity name from the array
        activity_name = array[3]

        try:
            #try to convert day value to integer
            day = int(array[5])
        except:
            #if fails return the relevant http message
            return reservation_http_messages.day_message()

        try:
            #try to convert hour value to integer
            hour = int(array[7])
        except:
            #if fails return the relevant http message
            return reservation_http_messages.hour_message()
        try:
            #try to convert duration value to integer
            duration = int(array[9])
        except:
            #if fails return the relevant http message
            return reservation_http_messages.duration_message()

        #create an hours array
        hours = []

        #initialize time value from hour
        time = hour

        #add reserved hours to the array
        while time < hour + duration:
            hours.append(time)
            time = time +1




        # Create the activity socket
        sockActivity = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #create the room socket
        sockRoom = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the room server
        sockActivity.connect(('0.0.0.0',7003))

        #connect to the activity server
        sockRoom.connect(('0.0.0.0',7005))

        #initialize the request message
        request_message = f"GET /check?name={activity_name} HTTP/1.1\r\nHost: 0.0.0.0\r\n\r\n"

        #send request to activity socket
        sockActivity.send(request_message.encode())

        while 1:
            #get activity socket response
            replyActivity = sockActivity.recv(1024)

            #if response not empty
            if (len(replyActivity) > 0):

                #initialize the activity response
                checkReplyActivityInString = f"HTTP/1.0 200 OK\n\n<HTML> <HEAD> <TITLE>Activity Exists</TITLE> </HEAD> <BODY>Activity with name {activity_name} does exists in database.</BODY> </HTML>"

                #convert response to bytes
                checkReplyActivityInBytes = checkReplyActivityInString.encode()

                #if the response is equal to actual response
                if(replyActivity == checkReplyActivityInBytes):

                    #initialize the request message to send room server
                     request_message = f"GET /reserve?name={room_name}&day={day}&hour={hour}&dduration={duration} HTTP/1.1\r\nHost: 0.0.0.0\r\n\r\n"

                     # encode and send request message to room server
                     sockRoom.send(request_message.encode())

                     while True:
                         #get reply from room server
                         replyRoom = sockRoom.recv(1024)

                         #if response is not empty
                         if (len(replyRoom) > 0):
                              #initialize a response for comparing with actual response
                             checkReplyRoomInString = f"HTTP/1.0 200 OK\n\n<HTML> <HEAD> <TITLE>Reservation Successful</TITLE> </HEAD> <BODY>Room with name {room_name} is reserved for you.</BODY> </HTML>"

                             #convert response to bytes
                             checkReplyRoomInByte = checkReplyRoomInString.encode()

                              #check if response equals to actual response
                             if(replyRoom == checkReplyRoomInByte):

                                 #get all entries from database in docs value
                                 docs = Reservation_DB.all()

                                 #get max id from the database
                                 max_id = max((doc.doc_id for doc in docs), default=0)

                                 #for new entry increment the id value
                                 max_id = max_id +1

                                 #load the requested reservation into reservation variable
                                 reservation = Reservation(room_name, activity_name, day, hours, duration, max_id).__dict__

                                 #insert the reservation value to the database
                                 Reservation_DB.insert(reservation)

                                 #return back succesfull http message
                                 response = reservation_http_messages.add_message(200,room_name,activity_name,day,hour,duration,max_id)

                                 #send response to the client
                                 client_connection.send(response.encode())

                             else:
                                 #if the response is not equal to expected response, sends the actual response to the client
                                 client_connection.send(replyRoom)
                         else:
                             break

                         #initialize the dar value as lenght of the room server reply
                         dar = float(len(replyRoom))
                         #divide 1024 for receiving buffer size is 1024
                         dar = float(dar / 1024)

                         dar = "%.3s" % (str(dar))

                         dar = "%s KB" % (dar)

                         #print the client address to the console
                         print("[*] Request Done: %s => %s <=" % (str(client_address[0]), str(dar)))
                     return
                else:
                    #if activity does not exist send the relevant http message from the activity server
                    client_connection.send(replyActivity)
            else:
                break
        # initialize the dar value as lenght of the room server reply
        dar = float(len(replyActivity))

        # divide 1024 for receiving buffer size is 1024
        dar = float(dar / 1024)

        dar = "%.3s" % (str(dar))

        dar = "%s KB" % (dar)

        # print the client address to the console
        print("[*] Request Done: %s => %s <=" % (str(client_address[0]), str(dar)))


        return




def display(params,conn):
    # Split the params string into a list of key-value pairs
    req_params = params.split('&')

    # Create an empty list to store the extracted params
    array = []

    # Iterate over the list of key-value pairs
    for par in req_params:
        # Split each key-value pair into separate key and value strings
        x = par.split('=')[0]
        y = par.split('=')[1]
        # Add the key and value to the array
        array.append(x)
        array.append(y)

    #get reservation id from the array
    reservationid = array[1]

    #get relevant reservation from the database according to given reservation id
    query = Reservation_DB.get(doc_id=reservationid)

    #initialize room, activity, day, hours and duraiton as empty string
    room = ""

    activity = ""

    day = ""

    hours = ""

    duration = ""

    #if the reservation found in the database
    if  query is not None :

        #inialize the room, activity, day, hours and duration values from the relevant reservation found in the database
        room = query.get('name')

        activity = query.get('activity')

        day = query.get('day')

        hours = query.get('hours')[0]

        duration = query.get('duration')

        #send succesfull http message to the user
        response = reservation_http_messages.checkId(200, reservationid,room,activity,day,hours,duration)

    else:
        #if the relevant reservation is not found in the database send a 404 not found http message to the user
        response = reservation_http_messages.checkId(404, reservationid,room,activity,day,hours,duration)


    conn.sendall(response.encode())
    return ""

def extract_string(string, start, end):
    #fro extracting substring in a string
    start_index = string.split(start)[1]
    end_index = start_index.split(end)[0]
    return end_index


