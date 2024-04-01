from tables import tables, file_names, table_names, csv_table_pairs
import extracting
import sqlite3
import os
import pandas as pd
import transformation
import csv

def save_raw_data_as_csv(output_folder):
    conn = sqlite3.connect('movie_data.db')
    for url, table_name in tables.items():
        extracting.read_data_to_sql(url, table_name)
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        output_file = os.path.join(output_folder, f"{table_name}.csv")
        df.to_csv(output_file, index=False)
    conn.close()

def save_curate_data_as_csv(folder_path):
    data = transformation.curate_data()
    for i, dataset in enumerate(data):
        with open(os.path.join(folder_path, f'{file_names[i]}.csv'), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(dataset.columns)  # Write column names
            writer.writerows(dataset.values.tolist()) 

def save_curated_tags_as_csv(folder_path): 
    # Call the curated_tags function to get the data
    result_tags = transformation.curate_data()
    # Check if result_tags is not None and not empty
    if result_tags is not None and not result_tags.empty:
        # Define the file path for saving the CSV file
        file_path = os.path.join(folder_path, 'tags.csv')
        result_tags.to_csv(file_path, index=False)


database_name = "movie_cleaned_data.db"

def store_csv_data_in_database(csv_table_pairs, database_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    for csv_file, table_name in csv_table_pairs:
        df = pd.read_csv(csv_file)
        df.to_sql(table_name, conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()

