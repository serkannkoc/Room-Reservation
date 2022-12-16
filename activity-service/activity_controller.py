from tinydb import TinyDB, Query
from activity import Activity
import activity_http_messages

ACTIVITY_DB = TinyDB('activity_db.json')
activity_query = Query()


def add(params):
    activity_name = params.split('=')[1]
    print('start controller add activity')
    if not ACTIVITY_DB.search(activity_query.name == activity_name):
        activity = Activity(activity_name).__dict__
        ACTIVITY_DB.insert(activity)
        response = activity_http_messages.add_message(200, activity_name)
    else:
        response = activity_http_messages.add_message(403, activity_name)
    print('end controller add room')
    return response


def remove(params):
    activity_name = params.split('=')[1]
    print('start remove activity')
    if ACTIVITY_DB.search(activity_query.name == activity_name):
        ACTIVITY_DB.remove(activity_query.name == activity_name)
        response = activity_http_messages.remove_message(200, activity_name)
    else:
        response = activity_http_messages.remove_message(403, activity_name)
    print("end remove activity")
    return response


def check(params):
    activity_name = params.split('=')[1]

    if not ACTIVITY_DB.search(activity_query.name == activity_name):
        return activity_http_messages.check_message(404, activity_name)
    else:
        return activity_http_messages.check_message(200,activity_name)
