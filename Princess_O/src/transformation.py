import pandas as pd



def apply_cleaning(data, COLUMNS_TO_TRANSFORM):
    for table_name, columns in COLUMNS_TO_TRANSFORM.items():
        for column in columns:
            print(column)
            if data[table_name][column].dtype == 'object':
                data[table_name][column] = data[table_name][column].str.replace('$', '').str.replace(',', '')
                data[table_name][column] = pd.to_numeric(data[table_name][column], errors='coerce')
    return data


def top_20_franchises_ranked_based_on_gross_revenue(data):
    selected_columns = data['Domestic_Box_Office_Franchises'][['Franchise', 'Worldwide_Box_Office']]
    sorted_data = selected_columns.sort_values(by='Worldwide_Box_Office', ascending=False)
    top_20_franchises_ranked_based_on_gross_revenue = sorted_data.head(20)
    top_20_franchises_ranked_based_on_gross_revenue.columns = ['Franchise', 'Gross Revenue']
    return top_20_franchises_ranked_based_on_gross_revenue

def ranking_franchise_based_on_the_number_of_movies_released(data):
    selected_columns = data['Domestic_Box_Office_Franchises'][['Franchise', 'No_of_Movies']]
    sorted_data = selected_columns.sort_values(by='No_of_Movies', ascending=False)
    ranking_franchise_based_on_the_number_of_movies_released = sorted_data.head(20)
    ranking_franchise_based_on_the_number_of_movies_released.columns = ['Franchise', 'Number of Movies']
    return ranking_franchise_based_on_the_number_of_movies_released

def average_revenue_per_movie_for_the_top_20_franchise(data):
    inner_query = data['top_20_for_each_Franchise'].groupby('Franchise').agg(
        Total=('Lifetime_Gross', 'sum'), 
        numbers_of_Movies=('Lifetime_Gross', 'count')
    ).reset_index()
    inner_query['Average Revenue per Movie'] = inner_query['Total'] / inner_query['numbers_of_Movies']
    result = inner_query.sort_values(by='Average Revenue per Movie', ascending=False).head(20)
    return result[['Franchise', 'Average Revenue per Movie']]

def number_of_release_per_season(data):
    inner_query = data['top_20_for_each_Franchise'].copy()
    inner_query['Released_season'] = pd.to_datetime(inner_query['Release_Date']).dt.month.map(
        lambda x: 'Winter' if x in [12, 1, 2]
        else ('Spring' if x in [3, 4, 5]
                else ('Summer' if x in [6, 7, 8]
                    else 'Fall')))
    selected_columns = inner_query[['Franchise', 'Release_Date', 'Released_season', 'Lifetime_Gross']]
    sorted_data = selected_columns.sort_values(by='Lifetime_Gross', ascending=False).head(50)
    result = sorted_data.groupby('Released_season').agg(Number_of_Release_per_season=('Released_season', 'count')).reset_index()
    return result[['Released_season', 'Number_of_Release_per_season']]


def transform_data(data):   
    top_20_gross_revenue = top_20_franchises_ranked_based_on_gross_revenue(data)
    top_20_movie_count = ranking_franchise_based_on_the_number_of_movies_released(data)
    top_20_average_revenue_per_movie = average_revenue_per_movie_for_the_top_20_franchise(data)
    release_per_season = number_of_release_per_season(data)
    
    return {
        'top_20_gross_revenue': top_20_gross_revenue,
        'top_20_movie_count': top_20_movie_count,
        'top_20_average_revenue_per_movie': top_20_average_revenue_per_movie,
        'number_of_release_per_season': release_per_season
    }

