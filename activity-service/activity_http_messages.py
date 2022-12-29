def add_message(status_code, activity_name):
    """
    Generate a response message for the `add` function.

    Parameters:
    status_code (int): The HTTP status code for the response.
    activity_name (str): The name of the activity that was added or attempted to be added.

    Returns:
    str: An HTTP response message containing the status code and a description of the operation.

    """
    if status_code == 200:
        # Generate a success message
        str = '<HTML> <HEAD> <TITLE>' + 'Activity Added' + '</TITLE> </HEAD> <BODY>' + 'Activity with name ' \
              + activity_name \
              + ' is successfully added.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 200 OK\n\n' + str
    elif status_code == 403:
        # Generate a failure message
        str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Activity with name ' + activity_name \
              + ' already exists in database.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 403 Forbidden\n\n' + str
    return response


def remove_message(status_code, activity_name):
    """
    Generate an HTTP response message for deleting an activity.

    Parameters:
    - status_code: the HTTP status code for the response.
    - activity_name: the name of the activity being deleted.

    Returns:
    - response: the HTTP response message.
    """

    # Check if the status code is 200 (successful deletion)
    if status_code == 200:
        # Generate response message for successful deletion
        str = '<HTML> <HEAD> <TITLE>' + 'Activity Deleted' + '</TITLE> </HEAD> <BODY>' + 'Activity with name ' \
              + activity_name \
              + ' is successfully deleted.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 200 OK\n\n' + str
    # Check if the status code is 403 (activity does not exist in database)
    elif status_code == 403:
        # Generate response message for unsuccessful deletion
        str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Activity with name ' + activity_name \
              + ' does not exists in database.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 403 Forbidden\n\n' + str

    return response  # return the HTTP response message


def check_message(status_code, activity_name):
    """
    Generate an HTTP response message for checking if an activity exists in the database.

    Parameters:
    - status_code: the HTTP status code for the response.
    - activity_name: the name of the activity being checked.

    Returns:
    - response: the HTTP response message.
    """

    # Check if the status code is 200 (activity exists in database)
    if status_code == 200:
        # Generate response message for successful check
        str = '<HTML> <HEAD> <TITLE>' + 'Activity Exists' + '</TITLE> </HEAD> <BODY>' + 'Activity with name ' \
              + activity_name \
              + ' does exists in database.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 200 OK\n\n' + str
    # Check if the status code is 404 (activity does not exist in database)
    elif status_code == 404:
        # Generate response message for unsuccessful check
        str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Activity with name ' + activity_name \
              + ' does not exists in database.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 404 Not Found\n\n' + str

    return response  # return the HTTP response message
