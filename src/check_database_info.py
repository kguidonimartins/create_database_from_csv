import pandas as pd
import sqlite3


def check_table_names(database_name):
    db = sqlite3.connect(database_name)
    cursor = db.cursor()
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    cursor.execute(query)
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]
    cursor.close()
    return table_names


def extract_tables_to_csv(database_name, dir_to_store):
    db = sqlite3.connect(database_name)
    cursor = db.cursor()
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    cursor.execute(query)
    tables = cursor.fetchall()
    for table_name in tables:
        table_name = table_name[0]
        query_table = f"SELECT * from '{table_name}'"
        table = pd.read_sql_query(query_table, db)
        table_name_to_save = dir_to_store + '/' + table_name + '.csv'
        table.to_csv(table_name_to_save, index_label='index')
    cursor.close()
    db.close()


def read_table_from_database(table_name, database_name):
    db = sqlite3.connect(database_name)
    query_table = f"SELECT * from '{table_name}'"
    table = pd.read_sql_query(query_table, db)
    return table


def check_table_structure(table_name, database_name):
    db = sqlite3.connect(database_name)
    cursor = db.cursor()
    query = f"SELECT sql FROM sqlite_master WHERE name = '{table_name}'"
    cursor.execute(query)
    table_structure = cursor.fetchall()
    cursor.close()
    db.close()
    format_table_structure = list(table_structure[0])[0].split('\n\t')
    return format_table_structure
