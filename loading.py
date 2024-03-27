from tables import tables, file_names, table_names
import extracting
import sqlite3
import os
import pandas as pd
import transformation
import csv

def save_data_as_csv(output_folder):
    conn = sqlite3.connect('movie_data.db')
    for url, table_name in tables.items():
        extracting.read_data_to_sql(url, table_name)
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        output_file = os.path.join(output_folder, f"{table_name}.csv")
        df.to_csv(output_file, index=False)
    conn.close()

def save_curate_data_as_csv(folder_path):
    data = transformation.curate_data() # this is from the transformation script
    for i, dataset in enumerate(data):
        with open(os.path.join(folder_path, f'{file_names[i]}.csv'), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(dataset)

def save_folder_to_sqlite(folder_path, db_path):
    # Connect to SQLite database
    conn = sqlite3.connect(db_path)

    # Iterate over each file in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            table_name = os.path.splitext(file_name)[0]  # Extract table name from file name
            csv_file_path = os.path.join(folder_path, file_name)

            # Read CSV file into DataFrame
            df = pd.read_csv(csv_file_path)

            # Save DataFrame to SQLite database, replacing any existing table
            df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Commit changes and close connection
    conn.commit()
    conn.close()

def save_transformed_data_as_csv(folder_path):
    data = transformation.tranformed_data() # this is from the transformation script
    for i, dataset in enumerate(data):
        with open(os.path.join(folder_path, f'{file_names[i]}.csv'), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(dataset)



if __name__ == "__main__":
   # raw_data_folder = "data\\raw_data"
    # save_data_as_csv(raw_data_folder)
    #cleaned_data_folder = "data\processed_data.csv\cleaned data"
    #save_curate_data_as_csv(cleaned_data_folder)
    #transformed_data_folder = "data\processed_data.csv\transformed data"
    #save_transformed_data_as_csv(transformed_data_folder)
    cleaned_data_folder = "data\processed_data.csv\cleaned data"
    db_path = "movie_data.db"
    save_folder_to_sqlite(cleaned_data_folder, db_path)