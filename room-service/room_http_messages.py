def add_room_message(status_code, room_name):
    # Initialize the response string to an empty string
    response = ""

    # If the status code is 200 (meaning the room was successfully added)
    if status_code == 200:
        # Create a string containing an HTML page with a success message
        str = '<HTML> <HEAD> <TITLE>' + 'Room Added' + '</TITLE> </HEAD> <BODY>' + 'Room with name ' + room_name \
              + ' is successfully added.' + '</BODY> </HTML>'
        # Set the response to a 200 OK status code and the HTML page
        response = 'HTTP/1.0 200 OK\n\n' + str
    # If the status code is 403 (meaning the room already exists in the database)
    elif status_code == 403:
        # Create a string containing an HTML page with an error message
        str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Room with name ' + room_name \
              + ' already exists in database.' + '</BODY> </HTML>'
        # Set the response to a 403 Forbidden status code and the HTML page
        response = 'HTTP/1.0 403 Forbidden\n\n' + str
    # Return the response
    return response


def remove_message(status_code, room_name):
    # Initialize the response string to an empty string
    response = ""

    # If the status code is 200 (meaning the room was successfully deleted)
    if status_code == 200:
        # Create a string containing an HTML page with a success message
        str = '<HTML> <HEAD> <TITLE>' + 'Room Deleted' + '</TITLE> </HEAD> <BODY>' + 'Room with name ' + room_name \
              + ' is successfully deleted.' + '</BODY> </HTML>'
        # Set the response to a 200 OK status code and the HTML page
        response = 'HTTP/1.0 200 OK\n\n' + str
    # If the status code is 403 (meaning the room does not exist in the database)
    elif status_code == 403:
        # Create a string containing an HTML page with an error message
        str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Room with name ' + room_name \
              + ' does not exists in database.' + '</BODY> </HTML>'
        # Set the response to a 403 Forbidden status code and the HTML page
        response = 'HTTP/1.0 403 Forbidden\n\n' + str
    # Return the response
    return response


def day_message():
    # Create a string containing an HTML page with an error message
    str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Enter day value between 1 and 7' \
          + '</BODY> </HTML>'
    # Set the response to a 400 Bad Request status code and the HTML page
    response = 'HTTP/1.0 400 Bad Request\n\n' + str
    # Return the response
    return response


def hour_message():
    # Create a string containing an HTML page with an error message
    str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Enter hour value between 9 and 17' \
          + '</BODY> </HTML>'
    # Set the response to a 400 Bad Request status code and the HTML page
    response = 'HTTP/1.0 400 Bad Request\n\n' + str
    # Return the response
    return response


def duration_message():
    # Create a string containing an HTML page with an error message
    str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Enter duration value as an integer' \
          + '</BODY> </HTML>'
    # Set the response to a 400 Bad Request status code and the HTML page
    response = 'HTTP/1.0 400 Bad Request\n\n' + str
    # Return the response
    return response


def reserve_message(status_code, room_name):
    # Initialize the response string to an empty string
    response = ""

    # If the status code is 200 (meaning the reservation was successful)
    if status_code == 200:
        # Create a string containing an HTML page with a success message
        str = '<HTML> <HEAD> <TITLE>' + 'Reservation Successful' + '</TITLE> </HEAD> <BODY>' + \
              'Room with name ' + room_name + " is reserved for you." + '</BODY> </HTML>'
        # Set the response to a 200 OK status code and the HTML page
        response = 'HTTP/1.0 200 OK\n\n' + str
    # If the status code is 403 (meaning the room is already reserved)
    elif status_code == 403:
        # Create a string containing an HTML page with an error message
        str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Room with name ' + room_name \
              + ' is already reserved!' + '</BODY> </HTML>'
        # Set the response to a 403 Forbidden status code and the HTML page
        response = 'HTTP/1.0 403 Forbidden\n\n' + str
    # Print the response (this line can be removed if desired)
    print(response)
    # Return the response
    return response


def check_available_hours_for_day(room_name, day, available_hours):
    # Initialize the dayInString variable to an empty string
    dayInString = ""

    # Convert the day number to a string representation of the day
    if day == "1":
        dayInString = "Monday"
    elif day == "2":
        dayInString = "Tuesday"
    elif day == "3":
        dayInString = "Wednesday"
    elif day == "4":
        dayInString = "Thursday"
    elif day == "5":
        dayInString = "Friday"
    elif day == "6":
        dayInString = "Saturday"
    elif day == "7":
        dayInString = "Sunday"

    # Create a string containing an HTML page with a message about the available hours for the specified day
    str = f'<HTML> <HEAD> <TITLE> Available Hours </TITLE> </HEAD> <BODY> On day {dayInString} room with name {room_name} is available for the following hours: ' \
          f'{available_hours} </BODY> </HTML>'
    # Print the HTML page (this line can be removed if desired)
    print(str)
    # Set the response to a 200 OK status code and the HTML page
    response = 'HTTP/1.0 200 OK\n\n' + str
    # Return the response
    return response

