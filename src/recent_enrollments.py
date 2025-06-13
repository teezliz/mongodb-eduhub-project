from db_connect import db
from datetime import datetime


students_collection = db["students"]


pipeline = [
    {
        "$addFields": {
            "enrollment_date_parsed": {
                "$dateFromString": {
                    "dateString": "$enrollment_date",
                    "format": "%Y-%m-%d"
                }
            }
        }
    },
    {
        "$match": {
            "enrollment_date_parsed": {
                "$gt": datetime(2024, 2, 1)
            }
        }
    }
]

recent_students = students_collection.aggregate(pipeline)

print("Students who enrolled after Feb 1, 2024:\n")
for student in recent_students:
    print(student)
