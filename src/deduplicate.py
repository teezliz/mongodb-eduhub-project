from db_connect import db

students_collection = db["students"]

unique_students = {}

all_students = list(students_collection.find())

for student in all_students:
    student_id = student["student_id"]
    if student_id not in unique_students:
        unique_students[student_id] = student["_id"]


deleted_count = 0

for student in all_students:
    student_id = student["student_id"]
    if student["_id"] != unique_students[student_id]:
        students_collection.delete_one({"_id": student["_id"]})
        deleted_count += 1

print(f"Deduplication complete. {deleted_count} duplicate(s) removed.")
