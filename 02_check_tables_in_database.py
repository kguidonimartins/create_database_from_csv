import sqlite3

import pandas as pd

from src.check_database_info import (
    check_table_names,
    check_table_structure,
    extract_tables_to_csv,
    read_table_from_database,
)

database_name = "test_small_db.db"

check_table_names(database_name)

table_list = check_table_names(database_name)

read_table_from_database(table_list[0], database_name)

print(check_table_structure(table_list[0], database_name))

extract_tables_to_csv(database_name, "data/output")
