#  create user '3340'@'localhost' identified by '123456789';
#  grant all privileges on *.* to '3340'@'localhost' with grant option;
#  flush privileges;
#  create database assignment8;
#  use assignment8;

# Python program to connect
# to mysql database


import mysql.connector


# Connecting from the server
conn = mysql.connector.connect(user = '3340',
							host = 'localhost',
							database = 'assignment8',
                            password='123456789')

# if conn.is_connected():
#     db_Info=conn.get_server_info()
#     print("connected to mysql",db_Info)
#     cursor=conn.cursor()
#     cursor.execute("select database();")
#     record=cursor.fetchone()
#     print("you are connected to:",record)

cursor = conn.cursor()
print("This is python program for interacting with the student information table which contains rollno, name, marks, you can see the details, delete, update etc via terminal only, moreover you can perform some queries")

while(1):
    print("\nMENU:\n1. SEE DETAILS\n2. INSERT DATA\n3. UPDATE MARKS\n4. DELETE RECORD\n5. SEE ALL DETAILS\n6. EXIT\n")
    n = int(input("ENTER CHOICE: "))
    if(n==1):
        m=int(input("ENTER ROLL NO: "))
        cursor.execute("select * from t1 where rollno=%d;"%m)
        a=cursor.fetchall()[0]
        if len(a)==0:
            print("NO DATA FOUND\n")
            continue
        print(f"\nROLL NO: {a[0]}\nNAME: {a[1]}\nMARKS: {a[2]}\n")
        #print(cursor.fetchall(),"\n")
    elif n==2:
        rollno = input("ENTER ROLL NO: ")
        name = input("ENTER NAME: ")
        marks = input("ENTER MARKS: ")
        q = f"INSERT INTO t1 (rollno, name, marks) VALUES ({rollno}, '{name}', {marks});"
        cursor.execute(q)
        conn.commit()
    elif(n==3):
        r=input("ENTER ROLL NO: ")
        m=input("ENTER NEW MARKS: ")
        cursor.execute(f"update t1 set marks={m} where rollno={r};")
        conn.commit()
    elif(n==4):
        r=input("ENTER ROLL NO: ")  
        cursor.execute(f"delete from t1 where rollno={r};")
        conn.commit()
    elif(n==5):
        cursor.execute("select * from t1;")
        a=cursor.fetchall()
        #print(a)
        for i in a:
            print(f"\nROLL NO: {i[0]}\nNAME: {i[1]}\nMARKS: {i[2]}\n")
    elif(n==6):exit()
    


        
# Disconnecting from the server
conn.close()

