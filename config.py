import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_URN = os.environ.get("DB_URN")
    DB_USER = os.environ.get("DB_USER")
    DB_PASS = os.environ.get("DB_PASS")
    DB_IP = os.environ.get("DB_IP")
    DB_NAME = os.environ.get("DB_NAME")
