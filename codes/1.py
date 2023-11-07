# Python program to connect
# to mysql database


import mysql.connector


# Connecting from the server
conn = mysql.connector.connect(user = 'new_user',
							host = 'localhost',
							database = '3318_DB',password='password')

cursor = conn.cursor()
print("This is python program for interacting with the student information table which contains rollno, name, marks, you can see the details, delete, update etc via terminal only, moreover you can perform some queries")

while(1):
    print("\nMENU:\n1. SEE DETAILS\n2. INSERT DATA\n3. UPDATE MARKS\n4. DELETE RECORD\n5. SEE ALL DETAILS\n6. EXIT\n")
    n = int(input("ENTER CHOICE: "))
    if(n==1):
        m=int(input("ENTER ROLL NO: "))
        cursor.execute("select * from t1 where rollno=%d;"%m)
        arr=cursor.fetchall()
        if len(arr)==0:
            print("NO DATA FOUND\n")
            continue
        print("\nROLL NO: %d\nNAME: %s\nMARKS: %d\n"%(arr[0][0],arr[0][1],arr[0][2]))
        #print(cursor.fetchall(),"\n")
    elif n==2:
        rollno = input("ENTER ROLL NO: ")
        name = input("ENTER NAME: ")
        marks = input("ENTER MARKS: ")
        cursor.execute("INSERT INTO t1 (rollno, name, marks) VALUES (%s, %s, %s);", (rollno, name, marks))
        conn.commit()
    elif(n==3):
        r=int(input("ENTER ROLL NO: "))
        m=int(input("ENTER NEW MARKS: "))
        cursor.execute("update t1 set marks=%d where rollno=%d;"%(m,r))
        conn.commit()
    elif(n==4):
        r=int(input("ENTER ROLL NO: "))  
        cursor.execute("delete from t1 where rollno=%d;"%r)
        conn.commit()
    elif(n==5):
        cursor.execute("select * from t1;")
        a=cursor.fetchall()
        #print(a)
        for i in a:
            print("\nROLL NO: %d\nNAME: %s\nMARKS: %d\n"%(i[0],i[1],i[2]))
    elif(n==6):exit()
    


        
# Disconnecting from the server
conn.close()

