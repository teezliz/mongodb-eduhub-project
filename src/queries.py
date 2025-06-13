from db_connect import db

students_collection = db["students"]

all_students = students_collection.find()

for student in all_students:
    print(student)
