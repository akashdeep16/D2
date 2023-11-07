import pymongo
from pprint import pprint 
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.StudentDB 
collection = db.students
#Insert
collection.insert_one({"roll": 3313, "name": "Aryan","marks": { "CNS": 85, "DBMS": 70, "SPOS": 80, "TOC": 80 }})
print("\nAfter insert update:") 
collection.insert_many([{ "roll": 3304, "name": "Akashdeep", "marks": { "CNS": 80, "DBMS": 80, "SPOS": 80, "TOC": 80 }},{ "roll": 3320, "name": "Deewan", "marks": { "CNS": 75, "DBMS": 90, "SPOS": 90, "TOC": 70 }}]);

for x in collection.find():
    pprint(x)
print()
#Update
collection.update_one(
    { "roll": 3313 },
    { "$set": { "name": "Aryan Deswal" } }
);
print("\nAfter Update:")
for x in collection.find():
    pprint(x)
print()
#delete
collection.delete_one(
    { "roll": 3313 }
);
print("\nAfter Delete:") 
for x in  collection.find():
    pprint(x)
print()