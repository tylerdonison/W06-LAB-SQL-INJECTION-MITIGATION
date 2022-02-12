def genQueryWeak(username, password):
    #provides basic mitigation through editing inputs to create desired or allowed inputs.
    invalid = ['-', ':', ';', '/', 'OR', 'UNION SELECT', ]
    count= 0
    length = len(username)
    for x in range(length):
        if x + 1 == length:
            break
        if username[x - count] in invalid:
            username = username.replace(username[x - count], '')
            length -= 1
            count += 1
    length = len(password)
    count = 0
    for x in range(length):
        if x + 1 == length:
            break
        if password[x - count] in invalid:
            password = password.replace(password[x - count], '')
            length -= 1
            count += 1
    return username, password