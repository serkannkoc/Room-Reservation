def add_room_message(status_code, room_name):
    if status_code == 200:
        str = '<HTML> <HEAD> <TITLE>' + 'Room Added' + '</TITLE> </HEAD> <BODY>' + 'Room with name ' + room_name \
              + ' is successfully added.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 200 OK\n\n' + str
    elif status_code == 403:
        str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Room with name ' + room_name \
              + ' already exists in database.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 403 Forbidden\n\n' + str
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


def reserve_message(status_code, room_name):
    if status_code == 200:
        str = '<HTML> <HEAD> <TITLE>' + 'Reservation Successful' + '</TITLE> </HEAD> <BODY>' + \
              'Room with name' + room_name + "is reserved for you." + '</BODY> </HTML>'
        response = 'HTTP/1.0 200 OK\n\n' + str
    elif status_code == 403:
        str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Room with name ' + room_name \
              + ' is already reserved!' + '</BODY> </HTML>'
        response = 'HTTP/1.0 403 Forbidden\n\n' + str
    return response


def check_available_hours_for_day(room_name, day, available_hours):
    str = '<HTML> <HEAD> <TITLE> Available Hours </TITLE> </HEAD> <BODY>' + \
          'On day ' + day + " room with name " + room_name + ' is available for the following hours: ' + \
          available_hours \
          + '</BODY> </HTML>'
    print(str)
    response = 'HTTP/1.0 200 OK\n\n' + str
    return response
