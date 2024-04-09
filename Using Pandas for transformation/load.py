import pandas as pd
import os
from extraction import import_data
from transformation import apply_cleaning

Raw_data_folder = os.getenv("raw_data_folder")
Cleaned_data_folder = os.getenv("cleaned_data_folder")


def load_raw_data():
    Movies_dataframes = import_data()
    for table_name, df in Movies_dataframes.items():
        file_path = os.path.join(Raw_data_folder, f"{table_name}.csv")
        df.to_csv(file_path, index=False)


def load_cleaned_data():
    Movies_dataframes = apply_cleaning()
    for table_name, df in Movies_dataframes.items():
        file_path = os.path.join(Cleaned_data_folder, f"{table_name}.csv")
        df.to_csv(file_path, index=False)

