users = {}

while True:
    in_line = input()
    if 'login' == in_line:
        break

    [username, password] = filter(None, in_line.split(" -> "))

    users[username] = password

unsuccessful_login_attempts = 0

while True:
    in_line = input()
    if 'end' == in_line:
        break

    [username, password] = filter(None, in_line.split(" -> "))

    if username in users and users[username] == password:
        print(f'{username}: logged in successfully')
    else:
        print(f'{username}: login failed')
        unsuccessful_login_attempts += 1

print(f'unsuccessful login attempts: {unsuccessful_login_attempts}')
