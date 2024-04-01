tables = {
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

file_names = ['top_20_for_each_Franchise', 'Domestic_Box_Office_Franchises', 'Domestic_Box_Office_Franchises_Marvel_Cinematic', 'World_Wide_Box_Office_All_Time_Top_1000', 'movies_Id', 'tags']

table_names = ['top_20_for_each_Franchise', 'Domestic_Box_Office_Franchises', 'Domestic_Box_Office_Franchises_Marvel_Cinematic', 'World_Wide_Box_Office_All_Time_Top_1000', 'movies_Id', 'tags']

csv_table_pairs = [
    ("data\processed_data.csv\cleaned data\Domestic_Box_Office_Franchises_Marvel_Cinematic.csv", "Domestic_Box_Office_Franchises_Marvel_Cinematic"),
    ("data\processed_data.csv\cleaned data\Domestic_Box_Office_Franchises.csv", "Domestic_Box_Office_Franchises"),
    ("data\processed_data.csv\cleaned data\top_20_for_each_Franchise.csv", "top_20_for_each_Franchise"),
    ("data\processed_data.csv\cleaned data\World_Wide_Box_Office_All_Time_Top_1000.csv", "World_Wide_Box_Office_All_Time_Top_1000"),
    ("data\processed_data.csv\cleaned data\movies_Id.csv", "movies_Id"),
    ("data\processed_data.csv\cleaned data\tags.csv", "tags")

]