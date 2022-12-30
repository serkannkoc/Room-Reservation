import json


def add_message(status_code, room_name, activity_name, day, hour,duration,id):

    # convert integer day value to relevant string day value
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

    #calculate end of reservation
    totalHour = hour + duration

    # Create a string containing an HTML page with a success message
    if status_code == 200:
        str = f'<HTML> <HEAD> <TITLE>Reservation Successful</TITLE> </HEAD> <BODY>Room {room_name} is reserved for activity {activity_name} on {dayInString}  ' \
              f'{hour}:00-{totalHour}:00. \nYour reservation ID is {id}. </BODY> </HTML>'
        # Set the response to a 200 OK status code and the HTML page
        response = 'HTTP/1.0 200 OK\n\n' + str

        # Create a string containing an HTML page with error message
    elif status_code == 403:
        str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Activity with name ' + activity_name \
              + ' already exists in database.' + '</BODY> </HTML>'
        # Set the response to a 403 Forbidden status code and the HTML page
        response = 'HTTP/1.0 403 Forbidden\n\n' + str
    return response

def day_message():
    # Create a string containing an HTML page with error message
    str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Enter day value between 1 and 7' \
          + '</BODY> </HTML>'
    response = 'HTTP/1.0 400 Bad Request\n\n' + str
    return response


def hour_message():
    # Create a string containing an HTML page with error message
    str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Enter hour value between 9 and 17' \
          + '</BODY> </HTML>'
    response = 'HTTP/1.0 400 Bad Request\n\n' + str
    return response


def duration_message():
    # Create a string containing an HTML page with error message
    str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Enter duration value as an integer' \
          + '</BODY> </HTML>'
    response = 'HTTP/1.0 400 Bad Request\n\n' + str
    return response

def remove_message(status_code, room_name):
    # Initialize the response string to an empty string
    response = ""

    # If the status code is 200 (meaning the room was successfully deleted)
    if status_code == 200:
        str = '<HTML> <HEAD> <TITLE>' + 'Room Deleted' + '</TITLE> </HEAD> <BODY>' + 'Room with name ' + room_name \
              + ' is successfully deleted.' + '</BODY> </HTML>'
        # Set the response to a 200 OK status code and the HTML page
        response = 'HTTP/1.0 200 OK\n\n' + str

    elif status_code == 403:
        # If the status code is 403 (meaning the room does not exist in the database)
        str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Room with name ' + room_name \
              + ' does not exists in database.' + '</BODY> </HTML>'
        # Set the response to a 403 Forbidden status code and the HTML page
        response = 'HTTP/1.0 403 Forbidden\n\n' + str
    return response

def checkId(status_code,reservationid,room,activity,day,hours,duration):

    # convert integer day value to relevant string day value
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

    # Create a string containing an HTML page with a success message
    if status_code == 200:
        str = f"<HTML><HEAD><TITLE>Reservation Info</TITLE></HEAD><BODY> Reservation ID:{reservationid} <BR>Room: {room} <BR>Activity: {activity} <BR>" \
              f"When: {dayInString} {hours}:00-{totalHour}:00. </BODY></HTML>"
        # Set the response to a 200 OK status code and the HTML page
        response = 'HTTP/1.0 200 OK\n\n' + str
        # Create a string containing an HTML page with error message
    elif status_code == 404:
        str = f'<HTML> <HEAD> <TITLE>Error</TITLE> </HEAD> <BODY>There is no entry with the id: {reservationid} </BODY> </HTML>'
        response = 'HTTP/1.0 404 Bad Request\n\n' + str
        # Set the response to a 404 Bad Request status code and the HTML page
    print(response)


    return response