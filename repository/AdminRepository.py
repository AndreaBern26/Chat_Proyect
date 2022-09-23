import mysql.connector
from models import User
from models import Admin


class UserRepository():

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='db_lifechat'
    )


def createUser(self, user:User):

    user = User() #Genera automaticamente una id por el user?

    cursor = self.connection.cursor()
    cursor.execute('insert into users values (%s, %s, %s, %s)',
                       (
                           #id = uuid.uuid4(),
                           user.username,
                           user.email,
                           user.password,
                           user.is_admin
                        ))

    self.connection.commit()
    cursor.close()


def deleteUser(self, user:User):
        cursor = self.connection.cursor()
        cursor.execute('delete from users where id = %s', (user.id))
        self.connection.commit()
        cursor.close()


def deleteGlobalMessage(messageId:int):
    return True