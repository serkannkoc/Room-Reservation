from tinydb import TinyDB, Query
from room import Room
import room_http_messages

ROOM_DB = TinyDB('room_db.json')
room_query = Query()


def add(params):
    room_name = params.split('=')[1]
    print('start controller add room')
    if not ROOM_DB.search(room_query.name == room_name):
        room = Room(room_name).__dict__
        ROOM_DB.insert(room)
        response = room_http_messages.add_room_message(200, room_name)
    else:
        response = room_http_messages.add_room_message(403, room_name)
    print('end controller add room')
    return response


def remove(params):
    room_name = params.split('=')[1]
    print(room_name)
    print('start remove room')
    if ROOM_DB.search(room_query.name == room_name):
        ROOM_DB.remove(room_query.name == room_name)
        response = room_http_messages.remove_message(200, room_name)
    else:
        response = room_http_messages.remove_message(403, room_name)
    print("end remove room")
    return response


def reserve(params):
    req_params = params.split('&')
    array = []
    for par in req_params:
        x = par.split('=')[0]
        y = par.split('=')[1]
        array.append(x)
        array.append(y)

    room_name = array[1]

    try:
        day = int(array[3])
    except:
        return room_http_messages.day_message()

    try:
        hour = int(array[5])
    except:
        return room_http_messages.hour_message()

    try:
        duration = int(array[7])
    except:
        return room_http_messages.duration_message()

    print('start reserve room')

    if not ROOM_DB.search(room_query.name == room_name):
        return room_http_messages.remove_message(403, room_name)
    elif day < 1 or day > 7:
        return room_http_messages.day_message()
    elif hour < 9 or hour > 17:
        return room_http_messages.hour_message()
    elif not isinstance(duration, int):
        return room_http_messages.duration_message()
    else:
        print()
        x = ROOM_DB.search(room_query.name == room_name)
        print(x)
        print()
        day = day - 1
        hour_array = []
        for h in range(hour, duration + hour):
            hour_array.append(h)
        print(hour_array)
        available_hours = x[0].get('available_hours')
        if is_sub_array(available_hours[day], hour_array, len(available_hours[day]), len(hour_array)):
            print("YES")
            for h in hour_array:
                available_hours[day].remove(h)
            print(available_hours[day])
            print(x)
            ROOM_DB.update({'available_hours': available_hours}, room_query.name == room_name)
            x = ROOM_DB.search(room_query.name == room_name)
            print(x)
            response = room_http_messages.reserve_message(200, room_name)
        else:
            print("NO")
            response = room_http_messages.reserve_message(403, room_name)

    return response


def check_availability(params):
    req_params = params.split('&')
    array = []
    for par in req_params:
        x = par.split('=')[0]
        y = par.split('=')[1]
        array.append(x)
        array.append(y)

    room_name = array[1]
    try:
        day = int(array[3])
    except:
        return room_http_messages.day_message()

    if not ROOM_DB.search(room_query.name == room_name):
        return room_http_messages.remove_message(403, room_name)
    elif day < 1 or day > 7:
        return room_http_messages.day_message()
    else:
        x = ROOM_DB.search(room_query.name == room_name)
        day = day - 1
        available_hours = x[0].get('available_hours')[day]
        av_hour = ""
        for i in available_hours:
            av_hour += str(i) + " "
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
