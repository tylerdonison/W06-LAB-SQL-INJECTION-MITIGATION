def genQueryWeak(username, password):
    #provides basic mitigation through editing inputs to create desired or allowed inputs.
    invalid = ['-', ':', ';', '/', "'", ]
    for x in invalid:
        username = username.replace(x, '')
        password = password.replace(x, '')
    return username, password
