from tinydb import TinyDB, Query
from activity import Activity
import activity_http_messages

# Create a database instance to store activity records
ACTIVITY_DB = TinyDB('activity_db.json')

# Create a query instance to search the database
activity_query = Query()


def add(params):
    """
    Add a new activity to the database.

    Parameters:
    params (str): A string containing the name of the activity to be added.

    Returns:
    str: A message indicating the success or failure of the operation.
    """
    # Extract the name of the activity from the parameters
    activity_name = params.split('=')[1]

    # Check if the activity already exists in the database
    if not ACTIVITY_DB.search(activity_query.name == activity_name):
        # Create a new activity instance
        activity = Activity(activity_name).__dict__

        # Add the activity to the database
        ACTIVITY_DB.insert(activity)

        # Generate a success message
        response = activity_http_messages.add_message(200, activity_name)
    else:
        # Generate a failure message
        response = activity_http_messages.add_message(403, activity_name)
    return response


def remove(params):
    """
    Remove an activity from the database.

    Parameters:
    params (str): A string containing the name of the activity to be removed.

    Returns:
    str: A message indicating the success or failure of the operation.
    """
    # Extract the name of the activity from the parameters
    activity_name = params.split('=')[1]

    # Check if the activity exists in the database
    if ACTIVITY_DB.search(activity_query.name == activity_name):
        # Remove the activity from the database
        ACTIVITY_DB.remove(activity_query.name == activity_name)

        # Generate a success message
        response = activity_http_messages.remove_message(200, activity_name)
    else:
        # Generate a failure message
        response = activity_http_messages.remove_message(403, activity_name)
    return response


def check(params):
    """
    Check if an activity exists in the database.

    Parameters:
    params (str): A string containing the name of the activity to be checked.

    Returns:
    str: A message indicating whether the activity exists in the database.
    """
    # Extract the name of the activity from the parameters
    activity_name = params.split('=')[1]

    # Check if the activity exists in the database
    if not ACTIVITY_DB.search(activity_query.name == activity_name):
        # Generate a failure message
        return activity_http_messages.check_message(404, activity_name)
    else:
        # Generate a success message
        return activity_http_messages.check_message(200, activity_name)