import mysql.connector
from models import User
from models import Admin


class AdminRepository():

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='db_lifechat'
    )


    def create_user(self, user:User):

        user = User() #Genera automaticamente una id por el user?

        cursor = self.connection.cursor()
        cursor.execute('insert into users values (%s, %s, %s, %s)',
                        (
                            user.username,
                            user.email,
                            user.password,
                            user.is_admin
                            ))

        self.connection.commit()
        cursor.close()


    def delete_user(self, user:User):
            cursor = self.connection.cursor()
            cursor.execute('delete from users where id = %s', (user.id))
            self.connection.commit()
            cursor.close()


    def delete_global_message(messageId:int):
        return True