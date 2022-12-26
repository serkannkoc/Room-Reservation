import json


def add_message(status_code, room_name, activity_name, day, hour,duration,id):
    dayInString = "string"

    if day == 1:
        dayInString = "Monday"
    elif day == 2:
        dayInString = "Tuesday"
    elif day == 3:
        dayInString = "Wednesday"
    elif day == 4:
        dayInString = "Thursday"
    elif day == 5:
        dayInString = "Friday"
    elif day == 6:
        dayInString = "Saturday"
    elif day == 7:
        dayInString = "Sunday"

    totalHour = hour + duration
    if status_code == 200:
        str = f'<HTML> <HEAD> <TITLE>Reservation Successful</TITLE> </HEAD> <BODY>Room {room_name} is reserved for activity {activity_name} on {dayInString}  ' \
              f'{hour}:00-{totalHour}:00. \nYour reservation ID is {id}. </BODY> </HTML>'
        response = 'HTTP/1.0 200 OK\n\n' + str
    elif status_code == 403:
        str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Activity with name ' + activity_name \
              + ' already exists in database.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 403 Forbidden\n\n' + str
    return response

def day_message():
    str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Enter day value between 1 and 7' \
          + '</BODY> </HTML>'
    response = 'HTTP/1.0 400 Bad Request\n\n' + str
    return response


def hour_message():
    str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Enter hour value between 9 and 17' \
          + '</BODY> </HTML>'
    response = 'HTTP/1.0 400 Bad Request\n\n' + str
    return response


def duration_message():
    str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Enter duration value as an integer' \
          + '</BODY> </HTML>'
    response = 'HTTP/1.0 400 Bad Request\n\n' + str
    return response

def remove_message(status_code, room_name):
    if status_code == 200:
        str = '<HTML> <HEAD> <TITLE>' + 'Room Deleted' + '</TITLE> </HEAD> <BODY>' + 'Room with name ' + room_name \
              + ' is successfully deleted.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 200 OK\n\n' + str
    elif status_code == 403:
        str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Room with name ' + room_name \
              + ' does not exists in database.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 403 Forbidden\n\n' + str
    return response

def checkId(status_code,reservationid,room,activity,day,hours,duration):

    dayInString = "Monday"
    if day == 1:
        dayInString = "Monday"
    elif day == 2:
        dayInString = "Tuesday"
    elif day == 3:
        dayInString = "Wednesday"
    elif day == 4:
        dayInString = "Thursday"
    elif day == 5:
        dayInString = "Friday"
    elif day == 6:
        dayInString = "Saturday"
    elif day == 7:
        dayInString = "Sunday"



    totalHour = hours + duration
    if status_code == 200:
        str = f"<HTML><HEAD><TITLE>Reservation Info</TITLE></HEAD><BODY> Reservation ID:{reservationid} <BR>Room: {room} <BR>Activity: {activity} <BR>" \
              f"When: {dayInString} {hours}:00-{totalHour}:00. </BODY></HTML>"
        response = 'HTTP/1.0 200 OK\n\n' + str
    elif status_code == 404:
        str = f'<HTML> <HEAD> <TITLE>Error</TITLE> </HEAD> <BODY>There is no entry with the id: {reservationid} </BODY> </HTML>'
        response = 'HTTP/1.0 404 Bad Request\n\n' + str
    print(response)


    return response