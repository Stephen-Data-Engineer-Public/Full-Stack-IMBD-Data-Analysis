import pandas as pd
import os


def load_data(movies, destination_folder):
    for table_name, df in movies.items():
        file_path = os.path.join(destination_folder, f"{table_name}.csv")
        df.to_csv(file_path, index=False)
