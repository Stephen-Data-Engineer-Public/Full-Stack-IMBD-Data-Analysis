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

folder_path = 'data\processed data csv\cleaned data csv'

def perform_sql_query_on_cleaned(folder_path, query):
    result_df = pd.DataFrame()
    # Loop through CSV files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            df = pd.read_csv(file_path)
            query_result = df.query(query)
            result_df = pd.concat([result_df, query_result], ignore_index=True)
    
    return result_df

