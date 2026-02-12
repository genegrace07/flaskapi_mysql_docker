import mysql.connector
from dotenv import load_dotenv
import os
from pydantic import BaseModel
import time

load_dotenv()

for t in range(10):
    try:
        db = mysql.connector.connect(
            host=os.environ.get('dbhost'),
            user=os.environ.get('dbuser'),
            password=os.environ.get('dbpassword'),
            database=os.environ.get('dbdatabase')
        # db = mysql.connector.connect(
        #     host=os.getenv('dbhost'),
        #     user=os.getenv('dbuser'),
        #     password=os.getenv('dbpassword'),
        #     database=os.getenv('dbdatabase')
        )
        print('Connected successfully on mysql')
        break
    except mysql.connector.Error as e:
        print('waiting to connect....',e)
        time.sleep(4)


# dbcursor=db.cursor(dictionary=True)
##flaskapi_mysql_docker table and columns
# querry = ("create table users("
#           "id int auto_increment primary key,"
#           "name varchar(50) not null,"
#           "email varchar(100) not null)")
# querry = ('select * from users')
# dbcursor.execute(querry)
# # db.commit()
# print(dbcursor.fetchall())

class Users(BaseModel):
        name:str
        email:str

class Usersdb():
    def view_users(self):
        db.ping(reconnect=True)
        dbcursor = db.cursor(dictionary=True)
        querry = 'select * from users'
        dbcursor.execute(querry)
        result = dbcursor.fetchall()
        dbcursor.close()
        return result
    def add(self,name,email):
        db.ping(reconnect=True)
        dbcursor = db.cursor(dictionary=True)
        querry = 'insert into users(name,email) values(%s,%s)'
        dbcursor.execute(querry,(name,email,))
        db.commit()
        dbcursor.close()
    def update(self,name,email,id):
        db.ping(reconnect=True)
        dbcursor = db.cursor(dictionary=True)
        querry = 'update users set name=%s,email=%s where id=%s'
        dbcursor.execute(querry,(name,email,id,))
        db.commit()
        dbcursor.close()
    def delete(self,id):
        db.ping(reconnect=True)
        dbcursor = db.cursor(dictionary=True)
        querry = 'delete from users where id = %s'
        dbcursor.execute(querry,(id,))
        db.commit()
        dbcursor.close()
class Action():
    def match(self,id):
        db.ping(reconnect=True)
        dbcursor = db.cursor(dictionary=True)
        querry = 'select * from users where id = %s'
        dbcursor.execute(querry,(id,))
        result =  dbcursor.fetchone()
        dbcursor.close()
        return result
    def match_email(self,email):
        db.ping(reconnect=True)
        dbcursor = db.cursor(dictionary=True)
        querry = 'select * from users where email = %s'
        dbcursor.execute(querry,(email,))
        result = dbcursor.fetchall()
        dbcursor.close()
        return result



