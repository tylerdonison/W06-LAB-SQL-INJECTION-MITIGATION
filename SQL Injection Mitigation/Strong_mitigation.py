def genQueryStrong(username, password):
    #Provides strong mitiation through changing any invalid input to "invalid", thus denying
    #malicious attacks.
    invalid_characters = ['-', ':', ';', '/', 'OR', 'UNION SELECT', ]
    for item in invalid_characters:
        if item in username:
            username = "Invalid"
        if item in password:
            password = "Invalid"
    return username, password
