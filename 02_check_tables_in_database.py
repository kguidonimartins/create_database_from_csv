import pandas as pd
import sqlite3
from src.check_database_info import (
                                     check_table_names, 
                                     read_table_from_database, 
                                     extract_tables_to_csv, 
                                     check_table_structure
                                     )

database_name = ('test_small_db.db')

check_table_names(database_name)

table_list = check_table_names(database_name)

read_table_from_database(table_list[0], database_name)

extract_tables_to_csv(database_name, 'data/output')
