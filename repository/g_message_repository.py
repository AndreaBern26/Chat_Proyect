from models.global_message import GlobalMessage

import app

class GlobalMessageRepository():

    session = app.db.session

    def get(self, message_id):
        return self.session.query(GlobalMessage).filter_by(id=message_id).one_or_none()
    
    def get_by_user_id (self, user_id):
        return self.session.query(GlobalMessage).filter_by(user_id=user_id).one_or_none()

    def list(self):
        return self.session.query(GlobalMessage).all()

    def add(self, message: GlobalMessage):
        self.session.add(message)
        self.session.commit()

    def delete(self, message: GlobalMessage):
        self.session.delete(message)
        self.session.commit()
    