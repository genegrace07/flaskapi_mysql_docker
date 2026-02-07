import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

db = mysql.connector.connect(
    host=os.getenv('dbhost'),
    user=os.getenv('dbuser'),
    password=os.getenv('dbpassword'),
    database=os.getenv('dbdatabase')
)

dbcursor=db.cursor(dictionary=True)
##flaskapi_mysql_docker table and columns
# querry = ("create table users("
#           "id int auto_increment primary key,"
#           "name varchar(50) not null,"
#           "email varchar(100) not null)")
querry = ("show columns from users")
dbcursor.execute(querry)
# db.commit()
print(dbcursor.fetchall())



