import pandas as pd

def import_data(tables):
    movies = {}
    for url, table_name in tables.items():
        if url.endswith('.csv'):
            movies[table_name] = pd.read_csv(url, engine="python")
        elif url.endswith('.tsv'):
            movies[table_name] = pd.read_csv(url, delimiter='\t', engine="python")
    return movies
