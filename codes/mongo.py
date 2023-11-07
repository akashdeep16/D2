from pymongo import MongoClient

# Modify the connection string based on your provided URL
connection_string = "mongodb://localhost:27017/mydata"

try:
    conn = MongoClient(connection_string)
    print("Connected to MongoDB")
except Exception as e:
    print(f"Could not connect to MongoDB: {e}")
    exit()

# Access the "t4" collection
collection = conn.mydata.t2

while True:
    print("MENU:\n1. INSERT\n2. UPDATE\n3. DELETE\n4. SHOW TABLE\n5. EXIT\n")
    ch = int(input("ENTER CHOICE: "))
    
    if ch == 1:
        rollno = input("ENTER ROLL NO: ")
        name = input("ENTER NAME: ")
        marks = input("ENTER MARKS: ")
        record = {
            "rollno": rollno,
            "name": name,
            "marks": marks
        }
        try:
            collection.insert_one(record)
            print("Record inserted successfully.")
        except Exception as e:
            print(f"Error inserting record: {e}")

    elif ch == 2:
        rollno = input("ENTER ROLL NO: ")
        marks = input("ENTER MARKS: ")
        filter = {'rollno': rollno}
        newvalues = {"$set": {'marks': marks}}
        try:
            collection.update_one(filter, newvalues)
            print("Record updated successfully.")
        except Exception as e:
            print(f"Error updating record: {e}")

    elif ch == 3:
        rollno = input("ENTER ROLL NO: ")
        try:
            collection.delete_one({"rollno": rollno})
            print("Record deleted successfully.")
        except Exception as e:
            print(f"Error deleting record: {e}")

    elif ch == 4:
        try:
            cursor = collection.find()
            for record in cursor:
                print(record)
        except Exception as e:
            print(f"Error fetching records: {e}")

    elif ch == 5:
        conn.close()
        print("Connection to MongoDB closed.")
        exit()
