import mysql.connector
from dotenv import load_dotenv
import os
from pydantic import BaseModel

load_dotenv()

db = mysql.connector.connect(
    host=os.getenv('dbhost'),
    user=os.getenv('dbuser'),
    password=os.getenv('dbpassword'),
    database=os.getenv('dbdatabase')
)

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




