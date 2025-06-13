from db_connect import db

students_collection = db["students"]

result = students_collection.update_one(
    {"student_id": "NG002"},  # find student by student_id
    {"$set": {"course": "AI & Machine Learning"}}  # update course field
)

if result.modified_count > 0:
    print("Student record updated successfully.")
else:
    print("No matching student found or data already up-to-date.")
