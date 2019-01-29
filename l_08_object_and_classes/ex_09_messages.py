class User:
    def __init__(self, name):
        self._username = name
        self._received_message = []

    def save_message(self, message):
        self._received_message.append(message)

    def get_username(self):
        return self._username

    def get_messages_from(self, user):
        return list(filter(lambda msg: msg.get_sender() == user, self._received_message))


class Message:
    def __init__(self, content, sender):
        self._content = content
        self._sender = sender

    def get_sender(self):
        return self._sender

    def __str__(self):
        return self._content


users = {}

while True:
    line = input()
    if "exit" == line:
        break

    tokens = line.split(" ")

    if "register" == tokens[0]:
        username = tokens[1]
        if username not in users:
            users[username] = User(username)
    else:
        message_sender = tokens[0]
        message_receiver = tokens[2]
        message_content = tokens[3]

        if message_sender in users and message_receiver in users:
            users[message_receiver].save_message(Message(message_content, message_sender))

first_user, second_user = input().split(" ")

if first_user in users and second_user in users:
    first_user_sent_messages = users[second_user].get_messages_from(first_user)
    second_user_sent_messages = users[first_user].get_messages_from(second_user)
    max_count = max(len(first_user_sent_messages), len(second_user_sent_messages))

    if len(first_user_sent_messages) == 0 and len(second_user_sent_messages) == 0:
        print("No messages")
        pass

    for i in range(max_count):
        if i < len(first_user_sent_messages):
            print(f"{first_user}: {first_user_sent_messages[i]}")
        if i < len(second_user_sent_messages):
            print(f"{second_user_sent_messages[i]} :{second_user}")
