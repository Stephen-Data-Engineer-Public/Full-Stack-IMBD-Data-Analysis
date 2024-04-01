import sqlite3
import pandas as pd
import os

def query_raw_data(query):
    conn = sqlite3.connect('movie_data.db')
    cursor = conn.cursor()
    cursor.execute(query)
    columns = [description[0] for description in cursor.description] 
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=columns)
    conn.close()
    return df

def perform_sql_query_on_cleaned(query):
    conn = sqlite3.connect('movie_cleaned_data.db')
    cursor = conn.cursor()
    cursor.execute(query)
    columns = [description[0] for description in cursor.description] 
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=columns)
    conn.close()
    return df

