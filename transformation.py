import sqlite3
import query
import os

query_top20 = '''SELECT franchise, rank, release, 
CAST(REPLACE(REPLACE(lifetime_gross, '$', ''), ',', '') AS INTEGER) as lifetime_gross, max_theaters, 
CAST(REPLACE(REPLACE(opening_gross, '$', ''), ',', '') AS INTEGER) as opening_gross, open_theaters, 
release_date, distributor FROM top_20_for_each_Franchise'''

query_domestic = '''SELECT franchise, no_of_movies, 
CAST(REPLACE(REPLACE(Domestic_box_office, '$', ''), ',', '') AS INTEGER) as Domestic_box_office,
CAST(REPLACE(REPLACE(Infl_Adj_Dom_Box_Office, '$', ''), ',', '') AS INTEGER) as Infl_Adj_Dom_Box_Office,
CAST(REPLACE(REPLACE(Worldwide_Box_Office, '$', ''), ',', '') AS INTEGER) as Worldwide_Box_Office, first_year, last_year,
No_of_years FROM Domestic_Box_Office_Franchises'''

query_marvel_domestic = '''SELECT Release_date, title, 
CAST(REPLACE(REPLACE(Production_Budget, '$', ''), ',', '') AS INTEGER) as Production_Budget,
CAST(REPLACE(REPLACE(Opening_Weekend, '$', ''), ',', '') AS INTEGER) as Opening_Weekend,
CAST(REPLACE(REPLACE(Domestic_Box_Office, '$', ''), ',', '') AS INTEGER) as Domestic_Box_Office,
CAST(REPLACE(REPLACE(Worldwide_Box_Office, '$', ''), ',', '') AS INTEGER) as Worldwide_Box_Office
 FROM Domestic_Box_Office_Franchises_Marvel_Cinematic'''

query_World_Wide_Box_Office_All_Time_Top_1000 = "SELECT * FROM World_Wide_Box_Office_All_Time_Top_1000"

query_movies_Id = "SELECT * FROM movies_Id"

query_Tags = "SELECT* FROM tags"


def curate_data():
    def curate_top20():
        result_top20 = query.query_raw_data(query_top20)  
        return result_top20
    def curate_domestic_box_office():
        result_domestic = query.query_raw_data(query_domestic)   
        return result_domestic
    def curate_marvel_domestic():
        result_marvel_domestic = query.query_raw_data(query_marvel_domestic)  
        return result_marvel_domestic
    def Curate_World_top_1000():
      result_world_top_1000 = query.query_raw_data(query_World_Wide_Box_Office_All_Time_Top_1000)  
      return result_world_top_1000
    def curated_movies_id():
      result_movies_id = query.query_raw_data(query_movies_Id)  
      return result_movies_id
    def curated_tags():
      result_tags = query.query_raw_data(query_Tags) 
      return result_tags
    return curate_top20(), curate_domestic_box_office(), curate_marvel_domestic(), Curate_World_top_1000(), curated_movies_id(), curated_tags()


query_top20_cleaned = '''SELECT franchise, Worldwide_Box_office FROM Domestic_Box_Office_Franchises Order by 2 DESC LIMIT 20'''
query_no_of_movies_cleaned = '''SELECT franchise, No_of_Movies FROM Domestic_Box_Office_Franchises order by 2 DESC LIMIT 20'''
query_avg_revenue_cleaned = '''SELECT
        Franchise,
        (Total/numbers_of_Movies) as AVG_Revenue_per_Movies
    FROM (
        SELECT
            Franchise,
            SUM(Lifetime_Gross) as Total,
            COUNT(*) as numbers_of_Movies
        FROM
            top_20_for_each_Franchise
        GROUP BY
            Franchise
    )
    ORDER BY
        AVG_Revenue_per_Movies DESC
    LIMIT
        20'''

query_season_releases_cleaned = '''SELECT
        Count(*) as Number_of_Release_per_season,
        Released_season
    FROM (
        SELECT
            Franchise,
            Release,
            Lifetime_Gross as Total_Gross,
            Release_Date,
            CASE
                WHEN Release_Date LIKE '%Dec%' OR Release_Date LIKE '%Jan%' OR Release_Date LIKE '%Feb%' THEN 'Winter'
                WHEN Release_Date LIKE '%Mar%' OR Release_Date LIKE '%Apr%' OR Release_Date LIKE '%May%' THEN 'Spring'
                WHEN Release_Date LIKE '%Jun%' OR Release_Date LIKE '%Jul%' OR Release_Date LIKE '%Aug%' THEN 'Summer'
                ELSE 'Fall'
            END AS Released_season
        FROM
            top_20_for_each_Franchise
        ORDER BY
            3 DESC
        LIMIT 50
    )
    GROUP BY
        Released_season'''


def tranformed_data():
   # Ranking The Top 20 franchise based on Gross Revenue
   def rank_top20_based_on_gross_revenue():
      result_gross_top20 = query.query_on_cleaned(query_top20_cleaned)
      return result_gross_top20
   # Ranking Franchise based on the number of Movies Released
   def rank_franchise_based_on_no_of_movies():
      result_no_of_movies = query.query_on_cleaned(query_no_of_movies_cleaned)
      return result_no_of_movies
   # Franchise average revenue per movie
   def franchise_avg_revenue_per_movie():
      result_avg_revenue = query.query_on_cleaned(query_avg_revenue_cleaned)
      return result_avg_revenue
   # Weather season releases with top performing movies
   def season_releases():
        result_season_releases = query.query_on_cleaned(query_season_releases_cleaned)
        return result_season_releases
   return rank_top20_based_on_gross_revenue(), rank_franchise_based_on_no_of_movies(), franchise_avg_revenue_per_movie(), season_releases() 

if __name__ == "__main__":
    # curate_data()
    tranformed_data()