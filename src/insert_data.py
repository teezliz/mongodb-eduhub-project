from db_connect import db

sample_students = [
    {
        "student_id": "NG001",
        "name": "Aisha Bello",
        "age": 22,
        "gender": "Female",
        "email": "aisha.bello@example.com",
        "phone": "+2348012345678",
        "address": "Lagos, Nigeria",
        "course": "Data Science",
        "enrollment_date": "2024-01-15"
    },
    {
        "student_id": "NG002",
        "name": "Chinedu Okafor",
        "age": 25,
        "gender": "Male",
        "email": "chinedu.okafor@example.com",
        "phone": "+2348023456789",
        "address": "Abuja, Nigeria",
        "course": "Web Development",
        "enrollment_date": "2024-02-20"
    },
    {
        "student_id": "NG003",
        "name": "Fatima Yusuf",
        "age": 28,
        "gender": "Female",
        "email": "fatima.yusuf@example.com",
        "phone": "+2348034567890",
        "address": "Kano, Nigeria",
        "course": "Cloud Engineering",
        "enrollment_date": "2024-03-10"
    }
]


students_collection = db["students"]
result = students_collection.insert_many(sample_students)

print(f"Inserted {len(result.inserted_ids)} students successfully!")

