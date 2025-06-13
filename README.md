# EduHub MongoDB Project

## 📊 Project Summary

EDUHUB is an interactive e-learning platform database project built with **MongoDB** and **Python**.  
It simulates the core functionalities of a modern online education system, including course management, student enrollments, and performance tracking.

This project demonstrates practical skills in:

- Designing flexible, scalable NoSQL schemas tailored for education data
- Implementing CRUD operations using PyMongo
- Applying data cleaning and deduplication techniques
- Building aggregation pipelines for analytics
- Utilizing CLI tools for database interaction

EduHub highlights how MongoDB can effectively manage dynamic educational content and user data, serving as a strong foundation for developers aiming to build real-world NoSQL applications.

---

## 📌 Project Description

EduHub is a simple e-learning platform database built with MongoDB and Python.  
The database manages student enrollments, courses, and basic analytics for an online learning platform.

This project demonstrates MongoDB basics including:

- Database design
- CRUD operations
- Data cleaning & deduplication
- Aggregation queries
- Analytics & reporting

---

## 🛠 Tech Stack

- Python 3
- MongoDB
- PyMongo
- Anaconda (virtual environment)
- CLI (Command Line Interface)

---

## 📂 Project Structure

```bash
mongodb-eduhub-project/
│
├── data/
├── notebooks/
├── src/
│   ├── db_connect.py
│   ├── insert_data.py
│   ├── queries.py
│   ├── update_data.py
│   ├── deduplicate.py
│   ├── analytics.py
│   └── dashboard.py
├── requirements.txt
└── README.md

📥 Installation

1️⃣ Clone the repository

bash
git clone https://github.com/teezliz/mongodb-eduhub-project.git

2️⃣ Navigate to project directory

bash
cd mongodb-eduhub-project

3️⃣ Create virtual environment

bash
python -m venv venv

4️⃣ Activate virtual environment

On Windows:

bash
venv\Scripts\activate

5️⃣ Install dependencies

bash
pip install -r requirements.txt

6️⃣ Make sure MongoDB server is installed and running locally

🚀 Usage
Use the scripts inside the src/ folder to perform database operations:

Insert data → insert_data.py

Update data → update_data.py

Perform queries → queries.py

Deduplicate data → deduplicate.py

Run analytics → analytics.py

Launch dashboard → dashboard.py

Example:

bash
python src/insert_data.py

🤝 Contributing
Contributions are welcome.
Feel free to fork the repository and submit pull requests.

📄 License
This project is for learning purposes and is open to the public.

✅ Project Status: Completed
📅 Author: Ogundipe Elizabeth