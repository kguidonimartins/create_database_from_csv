from pathlib import Path

import pandas as pd


def insert_csv_in_db(csv_path, chunk_size, database_connection):
    """Insert a csv file into a database.

    Args:
        csv_path (str): Path to csv file
        chunk_size (int): Block size adjustment for use with huge files
        database_connection (str): Database connection
    """
    file = pd.read_csv(csv_path, chunksize=chunk_size)
    name_table = Path(csv_path).stem
    for chunk in file:
        chunk.to_sql(
            name=name_table, if_exists="append", con=database_connection
        )
