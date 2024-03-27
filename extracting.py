import requests
import pandas as pd
from tables import tables
import sqlite3
import os

def read_data_to_sql(url, table_name):
    conn = sqlite3.connect('movie_data.db')
    for url, table_name in tables.items():
        if url.endswith('.csv'):
            df = pd.read_csv(url)
            df.to_sql(table_name, conn, if_exists='replace', index=False)
        elif url.endswith('.tsv'):
            df = pd.read_csv(url, delimiter='\t')
            df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()


