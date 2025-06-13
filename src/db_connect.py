import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["eduhub"]

if __name__ == "__main__":
    print("Database connection successful:", db)

