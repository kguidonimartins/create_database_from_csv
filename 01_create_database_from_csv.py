import glob
import os
from sqlalchemy import create_engine
from src.insert_csv_into_database import insert_csv_in_db

small_files = [f for f in glob.glob("data/input/small_csv*.csv")]

small_db = create_engine('sqlite:///./test_small_db.db')

[insert_csv_in_db(x, 1000, small_db) for x in small_files]

huge_db = create_engine('sqlite:///./test_huge_db.db')

insert_csv_in_db('data/input/huge_csv.csv', 1000, huge_db)
