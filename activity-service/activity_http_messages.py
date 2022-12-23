def add_message(status_code, activity_name):
    if status_code == 200:
        str = '<HTML> <HEAD> <TITLE>' + 'Activity Added' + '</TITLE> </HEAD> <BODY>' + 'Activity with name ' \
              + activity_name \
              + ' is successfully added.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 200 OK\n\n' + str
    elif status_code == 403:
        str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Activity with name ' + activity_name \
              + ' already exists in database.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 403 Forbidden\n\n' + str
    return response


def remove_message(status_code, activity_name):
    if status_code == 200:
        str = '<HTML> <HEAD> <TITLE>' + 'Activity Deleted' + '</TITLE> </HEAD> <BODY>' + 'Activity with name ' \
              + activity_name \
              + ' is successfully deleted.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 200 OK\n\n' + str
    elif status_code == 403:
        str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Activity with name ' + activity_name \
              + ' does not exists in database.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 403 Forbidden\n\n' + str
    return response


def check_message(status_code, activity_name):
    if status_code == 200:
        str = '<HTML> <HEAD> <TITLE>' + 'Activity Exists' + '</TITLE> </HEAD> <BODY>' + 'Activity with name ' \
              + activity_name \
              + ' does exists in database.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 200 OK\n\n' + str
    elif status_code == 404:
        str = '<HTML> <HEAD> <TITLE>' + 'Error' + '</TITLE> </HEAD> <BODY>' + 'Activity with name ' + activity_name \
              + ' does not exists in database.' + '</BODY> </HTML>'
        response = 'HTTP/1.0 404 Not Found\n\n' + str
    return response
