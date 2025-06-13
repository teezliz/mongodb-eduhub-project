from db_connect import db

students_collection = db["students"]


total_students = students_collection.count_documents({})
print(f"Total number of students: {total_students}")

pipeline_course_count = [
    {
        "$group": {
            "_id": "$course",
            "count": {"$sum": 1}
        }
    }
]

course_counts = students_collection.aggregate(pipeline_course_count)

print("\nTotal students per course:")
for course in course_counts:
    print(f"{course['_id']}: {course['count']}")

pipeline_avg_age = [
    {
        "$group": {
            "_id": None,
            "average_age": {"$avg": "$age"}
        }
    }
]

avg_age_result = list(students_collection.aggregate(pipeline_avg_age))
if avg_age_result:
    print(f"\nAverage student age: {avg_age_result[0]['average_age']:.2f}")
