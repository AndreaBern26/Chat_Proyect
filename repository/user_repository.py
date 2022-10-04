from models.users import User
import mysql.connector

class UserRepository():

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='SomosCoders2022',
        database='db_lifechat'
    )

    def get_user_by_email(self, email: str):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute('select * from users where email = %s', (email,))
        user = self.__compound_user(cursor.fetchone())
        cursor.close()
        return user

    def add(self, user: User):
        cursor = self.connection.cursor()
        cursor.execute('insert into users values (%s,%s,%s, %s)', (user.id, user.username, user.email, user.password))
        self.connection.commit()
        cursor.close()
    
    
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
        # rows = cursor.fetchall()
        # for row in rows:
        #     user_list.append(self.__compound_user(row))
        # cursor.close()
        return user_list


    def __compound_user(self, row):
        if row is None:
            return None

        user = User(
            row['username'],
            row['email'],
            row['password'],
            row['is_admin']
        )

        user.id = row['id']
        user.password = row['password']
    
        return user