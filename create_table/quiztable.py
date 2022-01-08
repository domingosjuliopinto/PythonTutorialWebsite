import pymysql

connection=pymysql.connect(
    host="localhost",
    user="root",
    db="ppmp" #Change the name according to your xampp mysql db
    )

cur=connection.cursor()

s='''create table quiz(
email_id varchar(30),
q1 varchar(20),
q2 varchar(20),
q3 varchar(20),
q4 varchar(20),
q5 varchar(20),
correct integer,
qdate date
)'''

cur.execute(s)

connection.close()
