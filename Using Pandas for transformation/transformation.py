import pandas as pd
from extraction import import_data
import numpy as np



columns_to_remove_the_dollar_sign = {
    'Domestic_Box_Office_Franchises': ['Domestic_Box_Office', 'Infl_Adj_Dom_Box_Office', 'Worldwide_Box_Office'],
    'Domestic_Box_Office_Franchises_Marvel_Cinematic': ['Production_Budget', 'Opening_Weekend', 'Domestic_Box_Office', 'Worldwide_Box_Office'],
    'top_20_for_each_Franchise': ['Lifetime_Gross','Opening_Gross','Max_Theaters']
}


def apply_cleaning():
    Movies_dataframes = import_data()
    for table_name, columns in columns_to_remove_the_dollar_sign.items():
        for column in columns:
            print(column)
            if Movies_dataframes[table_name][column].dtype == 'object':
                Movies_dataframes[table_name][column] = Movies_dataframes[table_name][column].str.replace('$', '').str.replace(',', '')
    return Movies_dataframes

