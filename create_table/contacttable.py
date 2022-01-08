import pymysql

connection=pymysql.connect(
    host="localhost",
    user="root",
    db="ppmp" #Change the name according to your xampp mysql db
    )

cur=connection.cursor()

s='''create table contact(
f_name varchar(20),
l_name varchar(20),
email_id varchar(30),
level varchar(15),
msg_type varchar(10),
msg varchar(250)
)'''

cur.execute(s)

connection.close()
