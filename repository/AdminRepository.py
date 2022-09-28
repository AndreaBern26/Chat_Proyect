import mysql.connector
from models import User
from models import Admin


class AdminRepository():

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Coders_1',
        database='db_lifechat'
    )

    def list_all(self):
        user_list = []
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute('select * from users')
        #rows = cursor.fetchall()
        # for row in rows:
        #     user_list.append(self.__compound_user(row))
        # cursor.close()
        return user_list

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