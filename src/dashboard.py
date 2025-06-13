from db_connect import db
from datetime import datetime

students_collection = db["students"]

total_students = students_collection.count_documents({})

pipeline_courses = [
    {
        "$group": {
            "_id": "$course",
            "count": {"$sum": 1}
        }
    }
]
course_distribution = students_collection.aggregate(pipeline_courses)


pipeline_age = [
    {
        "$group": {
            "_id": None,
            "average_age": {"$avg": "$age"}
        }
    }
]
average_age_result = list(students_collection.aggregate(pipeline_age))
average_age = average_age_result[0]["average_age"] if average_age_result else 0

# Enrollments this year
current_year = datetime.now().year
pipeline_recent = [
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
            "$expr": {
                "$eq": [{"$year": "$enrollment_date_parsed"}, current_year]
            }
        }
    }
]
recent_enrollments = list(students_collection.aggregate(pipeline_recent))
recent_enrollments_count = len(recent_enrollments)

print("==== EduHub Analytics Dashboard ====")
print(f"Total Students: {total_students}")
print(f"Average Age: {average_age:.2f}")

print("\nStudents per Course:")
for course in course_distribution:
    print(f"{course['_id']}: {course['count']}")

print(f"\nEnrollments in {current_year}: {recent_enrollments_count}")
