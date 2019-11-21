from pathlib import Path
import pandas as pd


def insert_csv_in_db(csv_, chunk_size, db_name): 
    file = pd.read_csv(csv_, chunksize=chunk_size)
    name_table = Path(csv_).stem
    for chunk in file:
        chunk.to_sql(name=name_table, if_exists='append', con=db_name)
