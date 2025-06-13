# EduHub MongoDB Project

📚 **EduHub** is a fully functional e-learning platform database project, built with **MongoDB** and **Python**, simulating core functionalities of modern online education systems: course management, enrollments, and performance tracking.

---

## 🚀 Project Highlights

This project demonstrates:

- 🏗️ Flexible NoSQL schema design
- 🔄 Full CRUD operations via PyMongo
- 🧹 Data cleaning & deduplication techniques
- 📊 Aggregation pipelines for analytics and reporting
- 🖥️ CLI-based database interaction

---

## 🛠 Tech Stack

- Python 3
- MongoDB
- PyMongo
- Anaconda (for virtual environment)
- Command Line Interface (CLI)

---

## 📂 Project Structure

bash
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

⚙️ Installation

1️⃣ Clone the repository:

bash
git clone https://github.com/teezliz/mongodb-eduhub-project.git
cd mongodb-eduhub-project

2️⃣ Create and activate virtual environment:

bash
python -m venv venv
venv\Scripts\activate   

3️⃣ Install project dependencies:

bash
pip install -r requirements.txt

4️⃣ Make sure MongoDB server is installed and running locally.

🏃‍♀️ Usage
Run any of the following scripts inside src/ to perform database operations:

Insert data → insert_data.py

Update data → update_data.py

Perform queries → queries.py

Deduplicate → deduplicate.py

Run analytics → analytics.py

Launch dashboard → dashboard.py

Example:

bash
python src/insert_data.py

🤝 Contributing
Contributions are welcome.
Feel free to fork this repository and submit pull requests.

📄 License
This project is for educational & learning purposes only.
Open to the public for non-commercial use.

👩‍💻 Author
Ogundipe Elizabeth

✅ Project Status: Completed ✅