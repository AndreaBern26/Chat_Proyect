import uuid

class GlobalMessage():

    id = uuid.uuid4()

    def __init__(self, user_id, message, message_date):
        self.user_id = user_id
        self.message = message
        self.message_date = message_date