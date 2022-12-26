from tinydb import TinyDB, Query
from reservation import Reservation
import reservation_http_messages
import uuid
Reservation_DB = TinyDB('reservation_db.json')

reservation_query = Query()

import socket








def list_availability(params,client_address,client_connection):

    req_params = params.split('&')
    array = []
    for par in req_params:
        x = par.split('=')[0]
        y = par.split('=')[1]
        array.append(x)
        array.append(y)


    room_name = array[1]

    if (len(array) >2) :
        day = int(array[3])

        sockRoom = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server
        sockRoom.connect(('0.0.0.0', 7005))

        request_message = f"GET /checkavailability?name={room_name}&day={day} HTTP/1.1\r\nHost: 0.0.0.0\r\n\r\n"
        print(request_message)
        sockRoom.send(request_message.encode())

        replyRoom = sockRoom.recv(1024)
        client_connection.send(replyRoom)
    else:
        day = 1
        replyRoom = ""
        while day < 7:
            sockRoom = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Connect to the server
            sockRoom.connect(('0.0.0.0', 7005))
            request_message = f"GET /checkavailability?name={room_name}&day={day} HTTP/1.1\r\nHost: 0.0.0.0\r\n\r\n"

            sockRoom.send(request_message.encode())

            replyRoomString = sockRoom.recv(1024)

            replyRoom = replyRoom +replyRoomString.decode().replace('\n','\\n')
            if replyRoom.find('403') != -1:
                break

            day = day + 1

        replyRoom = replyRoom.replace('HTTP/1.0 200 OK\\n\\n',"")
        replyRoom = replyRoom.replace('HTTP/1.0 403 Forbidden\\n\\n',"")
        replyRoom = replyRoom.replace('</HTML>', '')
        replyRoom = '<HTML>' + replyRoom + '</HTML>'
        replyRoom = replyRoom.replace('</BODY>','<br></BODY>')
        replyRoom = 'HTTP/1.0 200 OK\n\n' + replyRoom

        client_connection.send(replyRoom.encode())

        return

    return


def reserve(params,client_address,client_connection):
        req_params = params.split('&')
        array = []
        for par in req_params:
            x = par.split('=')[0]
            y = par.split('=')[1]
            array.append(x)
            array.append(y)


        room_name = array[1]
        activity_name = array[3]

        try:
            day = int(array[5])
        except:
            return reservation_http_messages.day_message()

        try:
            hour = int(array[7])
        except:
            return reservation_http_messages.hour_message()
        try:
            duration = int(array[9])
        except:
            return reservation_http_messages.duration_message()
        hours = []
        time = hour
        while time < hour + duration:
            hours.append(time)
            time = time +1




        # Create the socket
        sockActivity = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockRoom = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server
        sockActivity.connect(('0.0.0.0',7003))
        sockRoom.connect(('0.0.0.0',7005))

        request_message = f"GET /check?name={activity_name} HTTP/1.1\r\nHost: 0.0.0.0\r\n\r\n"


        sockActivity.send(request_message.encode())

        while 1:
            replyActivity = sockActivity.recv(1024)
            if (len(replyActivity) > 0):
                checkReplyActivityInString = f"HTTP/1.0 200 OK\n\n<HTML> <HEAD> <TITLE>Activity Exists</TITLE> </HEAD> <BODY>Activity with name {activity_name} does exists in database.</BODY> </HTML>"
                checkReplyActivityInBytes = checkReplyActivityInString.encode()
                if(replyActivity == checkReplyActivityInBytes):
                     request_message = f"GET /reserve?name={room_name}&day={day}&hour={hour}&dduration={duration} HTTP/1.1\r\nHost: 0.0.0.0\r\n\r\n"

                     sockRoom.send(request_message.encode())
                     while True:
                         replyRoom = sockRoom.recv(1024)

                         if (len(replyRoom) > 0):

                             checkReplyRoomInString = f"HTTP/1.0 200 OK\n\n<HTML> <HEAD> <TITLE>Reservation Successful</TITLE> </HEAD> <BODY>Room with name {room_name} is reserved for you.</BODY> </HTML>"
                             checkReplyRoomInByte = checkReplyRoomInString.encode()
                             if(replyRoom == checkReplyRoomInByte):
                                 docs = Reservation_DB.all()
                                 max_id = max((doc.doc_id for doc in docs), default=0)

                                 max_id = max_id +1


                                 reservation = Reservation(room_name, activity_name, day, hours, duration, max_id).__dict__
                                 Reservation_DB.insert(reservation)

                                 response = reservation_http_messages.add_message(200,room_name,activity_name,day,hour,duration,max_id)
                                 client_connection.send(response.encode())
                             else:
                                 client_connection.send(replyRoom)
                         else:
                             break
                         dar = float(len(replyRoom))
                         dar = float(dar / 1024)
                         dar = "%.3s" % (str(dar))
                         dar = "%s KB" % (dar)
                         print("[*] Request Done: %s => %s <=" % (str(client_address[0]), str(dar)))
                     return
                else:
                    client_connection.send(replyActivity)
            else:
                break

        dar = float(len(replyActivity))
        dar = float(dar / 1024)
        dar = "%.3s" % (str(dar))
        dar = "%s KB" % (dar)
        print("[*] Request Done: %s => %s <=" % (str(client_address[0]), str(dar)))


        return




def display(params,conn):

    req_params = params.split('&')
    array = []
    for par in req_params:
        x = par.split('=')[0]
        y = par.split('=')[1]
        array.append(x)
        array.append(y)

    reservationid = array[1]

    query = Reservation_DB.get(doc_id=reservationid)


    if  query is not None :
        room = query.get('name')

        activity = query.get('activity')

        day = query.get('day')

        hours = query.get('hours')[0]

        duration = query.get('duration')
        print(room)
        response = reservation_http_messages.checkId(200, reservationid,room,activity,day,hours,duration)
    else:
        room = ""

        activity = ""

        day = ""

        hours = ""

        duration = ""
        response = reservation_http_messages.checkId(404, reservationid,room,activity,day,hours,duration)

    conn.sendall(response.encode())
    return ""

def extract_string(string, start, end):
    start_index = string.split(start)[1]
    end_index = start_index.split(end)[0]
    return end_index


