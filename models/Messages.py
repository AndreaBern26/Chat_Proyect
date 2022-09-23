import uuid

class Messages():
    id = uuid.uuid4()

    def __init__(self, user_to, user_from, message, message_date):
        self.user_to = user_to
        self.user_from = user_from
        self.message = message
        self.message_date = message_date