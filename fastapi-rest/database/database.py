import os
import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = os.environ.get("USER", "user")
password = os.environ.get("PASSWORD", "password")
hostname = os.environ.get("HOSTNAME", "localhost")
dbname = os.environ.get("DB", "todos")
dbport = os.environ.get("DB_PORT", "3306")

DATABASE_URL = f"mysql+pymysql://{user}:{password}@{hostname}/{dbname}"

max_attempts = 5
curr_attempt = 0

while curr_attempt < max_attempts:
    time.sleep(10)
    try:
        engine = create_engine(DATABASE_URL)
        SessionLocal = sessionmaker(engine, autocommit=False, autoflush=False)
        Base = declarative_base()
        break
    except Exception as e:
        print(f"Attempt {curr_attempt} failed: {e}")
        curr_attempt += 1
