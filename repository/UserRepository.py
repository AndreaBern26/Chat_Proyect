from models import User
import mysql.connector

class UserRepository():

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='SomosCoders2022',
        database='db_lifechat'
    )

    def send_global_message(message:str):
        return True

    def send_message(message:str):
        return True

    def delete_message(id:int):
        return True

    def delete_account(self):
        cursor = self.connection.cursor()
        cursor.execute('delete from users where id = %s', (self.id))
        self.connection.commit()
        cursor.close()
    
    def list_all(self):
        user_list = []
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute('select * from users')
        #rows = cursor.fetchall()
        # for row in rows:
        #     user_list.append(self.__compound_user(row))
        # cursor.close()
        return user_list


    # def __compound_user(self, row):
    #     if row is None:
    #         return None

    #     user = User(
    #         row['username'],
    #         row['email'],
    #         row['password'],
    #         row['is_admin']
    #                 )
    #     user.id = row['id']
    #     user.password = row['password']