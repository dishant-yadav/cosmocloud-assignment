from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


MONGO_URI = os.getenv("MONGODBURI")
DB_NAME = os.getenv("DB_NAME", "student_management")

client = MongoClient(MONGO_URI)
database = client.get_database(DB_NAME)
