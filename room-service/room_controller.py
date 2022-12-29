from tinydb import TinyDB, Query
from room import Room
import room_http_messages

# Initialize the database and define a query object
ROOM_DB = TinyDB('room_db.json')
room_query = Query()


def add(params):
    """Adds a new room to the database.

    Args:
        params (str): The query string containing the name of the room to add.

    Returns:
        str: A response indicating the result of the operation.
    """
    # Extract the room name from the query string
    room_name = params.split('=')[1]
    print('start controller add room')

    # Check if the room already exists in the database
    if not ROOM_DB.search(room_query.name == room_name):
        # Create a new Room object and add it to the database
        room = Room(room_name).__dict__
        ROOM_DB.insert(room)

        # Generate a successful response
        response = room_http_messages.add_room_message(200, room_name)
    else:
        # Generate a response indicating that the room already exists
        response = room_http_messages.add_room_message(403, room_name)
    print('end controller add room')
    return response


def remove(params):
    """Removes a room from the database.

    Args:
        params (str): The query string containing the name of the room to remove.

    Returns:
        str: A response indicating the result of the operation.
    """
    # Extract the room name from the query string
    room_name = params.split('=')[1]
    print(room_name)
    print('start remove room')

    # Check if the room exists in the database
    if ROOM_DB.search(room_query.name == room_name):
        # Remove the room from the database
        ROOM_DB.remove(room_query.name == room_name)
        # Generate a successful response
        response = room_http_messages.remove_message(200, room_name)
    else:
        # Generate a response indicating that the room does not exist
        response = room_http_messages.remove_message(403, room_name)
    print("end remove room")
    return response


def reserve(params):
    # Split the params string into a list of key-value pairs
    req_params = params.split('&')
    array = []
    for par in req_params:
        # Split each key-value pair into separate variables
        x = par.split('=')[0]
        y = par.split('=')[1]
        # Append the variables to the array
        array.append(x)
        array.append(y)

    # Get the room name from the array
    room_name = array[1]

    try:
        # Convert the day to an integer
        day = int(array[3])
    except:
        # Return an error message if the day is not a valid integer
        return room_http_messages.day_message()

    try:
        # Convert the hour to an integer
        hour = int(array[5])
    except:
        # Return an error message if the hour is not a valid integer
        return room_http_messages.hour_message()

    try:
        # Convert the duration to an integer
        duration = int(array[7])
    except:
        # Return an error message if the duration is not a valid integer
        return room_http_messages.duration_message()

    # Print a message indicating that the reservation process has started
    print('start reserve room')

    if not ROOM_DB.search(room_query.name == room_name):
        # Return an error message if the room is not found in the database
        return room_http_messages.remove_message(403, room_name)
    elif day < 1 or day > 7:
        # Return an error message if the day is not within the valid range
        print(day)
        return room_http_messages.day_message()
    elif hour < 9 or hour > 17:
        # Return an error message if the hour is not within the valid range
        return room_http_messages.hour_message()
    elif not isinstance(duration, int):
        # Return an error message if the duration is not an integer
        return room_http_messages.duration_message()
    else:
        print()
        # Get the room object from the database
        x = ROOM_DB.search(room_query.name == room_name)
        print(x)
        print()
        # Subtract 1 from the day to adjust for the indexing of the available_hours list
        day = day - 1
        hour_array = []
        for h in range(hour, duration + hour):
            hour_array.append(h)
        print(hour_array)
        # Get the list of available hours for the specified day
        available_hours = x[0].get('available_hours')
        if is_sub_array(available_hours[day], hour_array, len(available_hours[day]), len(hour_array)):
            print("YES")
            # Remove the reserved hours from the available_hours list
            for h in hour_array:
                available_hours[day].remove(h)
            print(available_hours[day])
            print(x)
            # Update the room object in the database with the updated available_hours list
            ROOM_DB.update({'available_hours': available_hours}, room_query.name == room_name)
            # Get the updated room object from the database
            x = ROOM_DB.search(room_query.name == room_name)
            print(x)
            # Return a success message
            response = room_http_messages.reserve_message(200, room_name)
        else:
            print("NO")
            # Return an error message if the requested hours are not available
            response = room_http_messages.reserve_message(403, room_name)

    return response


def check_availability(params):
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
    try:
        # Try to convert the day value to an integer
        day = int(array[3])
    except:
        # If the conversion fails, return an error message
        return room_http_messages.day_message()

    # Check if the room name is not in the database
    if not ROOM_DB.search(room_query.name == room_name):
        # If the room name is not in the database, return an error message
        return room_http_messages.remove_message(403, room_name)
    # Check if the day value is not within the valid range of 1 to 7
    elif day < 1 or day > 7:
        # If the day value is not within the valid range, return an error message
        return room_http_messages.day_message()
    else:
        # If the room name is in the database and the day value is valid,
        # search the database for the room with the given name
        x = ROOM_DB.search(room_query.name == room_name)
        # Print the search result for debugging purposes
        print(x)
        # Subtract 1 from the day value to convert it to an index
        day = day - 1
        # Get the available hours for the given day from the search result
        available_hours = x[0].get('available_hours')[day]
        # Create an empty string to store the available hours
        av_hour = ""
        # Iterate over the list of available hours
        for i in available_hours:
            # Add each hour to the string
            av_hour += str(i) + " "
        # Return a message with the available hours for the given day
        return room_http_messages.check_available_hours_for_day(room_name, str(day + 1), av_hour)


def is_sub_array(a, b, n, m):
    # Two pointers to traverse the arrays
    i = 0
    j = 0

    # Traverse both arrays simultaneously
    while i < n and j < m:
        # If element matches
        # increment both pointers
        if a[i] == b[j]:
            i += 1
            j += 1

            # If array B is completely
            # traversed
            if j == m:
                return True

        # If not,
        # increment i and reset j
        else:
            i = i - j + 1
            j = 0

    return False
