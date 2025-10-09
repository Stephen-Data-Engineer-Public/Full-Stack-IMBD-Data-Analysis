from extraction import import_data
from transformation import apply_cleaning, transform_data
from load import load_data
#import os

def main(
        RAW_DATA_FOLDER, CLEAN_DATA_FOLDER, TRANSFORMED_DATA_FOLDER,
        TABLES, COLUMNS_TO_REMOVE_THE_DOLLAR_SIGN
    ):
        # ETL pipeline logic
    data = import_data(TABLES)
    load_data(data, RAW_DATA_FOLDER)

    transformed = apply_cleaning(data, COLUMNS_TO_REMOVE_THE_DOLLAR_SIGN)
    load_data(transformed, CLEAN_DATA_FOLDER)

    transformed_data = transform_data(transformed)
    load_data(transformed_data, TRANSFORMED_DATA_FOLDER)


if __name__ == "__main__":
    # Defining constants
    
    RAW_DATA_FOLDER = "/Workspace/Users/peculiarstephen@gmail.com/Full-Stack-IMBD-Data-Analysis/src/RAW_DATA_FOLDER"
    CLEANED_DATA_FOLDEER = "/Workspace/Users/peculiarstephen@gmail.com/Full-Stack-IMBD-Data-Analysis/src/CLEAN_DATA_FOLDER"
    TRANSFORMED_DATA_FOLDER = "/Workspace/Users/peculiarstephen@gmail.com/Full-Stack-IMBD-Data-Analysis/src/TRANSFORMED_DATA_FOLDER"
    
    TABLES = {
    "https://raw.githubusercontent.com/mansik95/IMDB-Analysis/master/Data/MovieLens_movies.csv": "movies_Id",
    "https://raw.githubusercontent.com/mansik95/IMDB-Analysis/master/Data/IMDb%20BoxOfficeMojo%20-%20Brands%20(US%20%26%20Canada).tsv": "brands_US_and_Canada",
    "https://raw.githubusercontent.com/mansik95/IMDB-Analysis/master/Data/IMDb%20BoxOfficeMojo%20-%20Brand_%20Marvel%20Comics.tsv": "brand_marvel_comics",
    "https://raw.githubusercontent.com/mansik95/IMDB-Analysis/master/Data/The%20Numbers%20-%20Domestic%20Box%20Office%20Daily%20-%20The%20Avengers.tsv": "Domestic_Box_Office_Daily_The_Avengers",
    "https://raw.githubusercontent.com/mansik95/IMDB-Analysis/master/Data/The%20Numbers%20-%20Domestic%20Box%20Office%20-%20Franchises.tsv": "Domestic_Box_Office_Franchises",
    "https://raw.githubusercontent.com/mansik95/IMDB-Analysis/master/Data/The%20Numbers%20-%20Domestic%20Box%20Office%20-%20Franchises%20-%20Marvel%20Cinematic%20Universe.tsv": "Domestic_Box_Office_Franchises_Marvel_Cinematic",
    "https://raw.githubusercontent.com/mansik95/IMDB-Analysis/master/Data/World%20Wide%20Box%20Office%20All%20Time%20Top%201000.tsv": "World_Wide_Box_Office_All_Time_Top_1000",
    "https://raw.githubusercontent.com/mansik95/IMDB-Analysis/master/Data/IMDb%20BoxOfficeMojo%20-%20Franchises%20(US%20%26%20Canada).tsv": "Franchises_us_and_Canada",
    "https://raw.githubusercontent.com/mansik95/IMDB-Analysis/master/Data/IMDb%20BoxOfficeMojo%20-%20Franchise_%20top20.tsv": "top_20_for_each_Franchise",
    "https://raw.githubusercontent.com/mansik95/IMDB-Analysis/master/Data/MovieLens_tags.csv": "tags"
    }
    COLUMNS_TO_REMOVE_THE_DOLLAR_SIGN = {
    'Domestic_Box_Office_Franchises': ['Domestic_Box_Office', 'Infl_Adj_Dom_Box_Office', 'Worldwide_Box_Office'],
    'Domestic_Box_Office_Franchises_Marvel_Cinematic': ['Production_Budget', 'Opening_Weekend', 'Domestic_Box_Office', 'Worldwide_Box_Office'],
    'top_20_for_each_Franchise': ['Lifetime_Gross','Opening_Gross','Max_Theaters']
}

    main(RAW_DATA_FOLDER, CLEANED_DATA_FOLDEER, TRANSFORMED_DATA_FOLDER, TABLES, COLUMNS_TO_REMOVE_THE_DOLLAR_SIGN)
   