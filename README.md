#           Full-Stack-IMDB-Data-Analysis
Welcome to my Full Stack Internet Movie Database(IMDB) Data Analysis repository! This comprehensive project encompasses the entire data analysis pipeline, from data extraction to insightful analysis on some set Movies on the IMDB.  
## Key Features:

1. Document Description: Provides descriptions for each document in the data.
2. Business Question Formulation: Develops a business question to be answered through data analysis.
3. Data Identification: Identifies necessary data from the data/ folder.
4. Simple Diagram Creation: Generates a straightforward diagram illustrating the interaction between selected data.
5. Data Importation: Imports the identified data as pandas DataFrame.
6. Data Quality Assessment (in Python):
- Calculates the number of null values for each column.
- Ensures proper formatting for all columns.
- Counts the number of unique, non-null values for each column.
7. Data Analysis Execution: Performs the data analysis using Python.
8. Data Cleaning: Cleans and transforms the data, including merging operations.
## Document Description : 

#### Tables: 

**Domestic box office franchise**
This table contains a comprehensive list of franchise in the IMDB database ranked by the total number of movies released, including the numbers of movies, the revenues generated both domestically and internationally, the release date  for either the first movie or series in the franchise, the expected end date for the last movie or series within the franchise.

**Marvel Cinematic Universal Franchise domestic box office**
This table is an expansion of the first row of the *Domestic box office franchise table*. It contains title of movies released by the marvel franchise, production budgets, the release date, gross revenue generated on it first weekend in the theatres, domestic and world wide gross revenue generated.

**Brands (US & Canada)**
This table holds the names of the franchise brands ranked according to their total gross, number of released movies, top performing movie and its total gross revenue over the theatrical life for each brand.

**Brand Marvel Comics** 
This table is an expansion of the first row found in the *Brands (US & Canada) Table*. It contains list of movies and their performance metrics under the Marvel comic brand.

**Top 20 Movie franchise**
This table contains informations including; list of movies title, lifetime gross, maximum number of theatre, gross for the opening day in theatres, list of distributors, and movie release dates of all the top 20 movie franchise.

**Franchise (US & Canada)**
This table contains informations about franchise in the US and Canada, which includes: the top movies, total revenue, lifetime gross for each franchise. 

**Movie Tags**
This table contains information about movies, including their Id, genre, and duration. 

**World Wide Box Office All Time Top 1000**
This table presents the information concerning the top 1000 movies of all time in the world based on their box office performance. 

**Movie Id**
This table links movie titles to their ID.

**Domestic Box Office Daily - The Avengers**
This table is an expansion of the first row within the *Marvel Cinematic Universal Franchise domestic box office table*. It shows the daily performance of the avengers movie during its theatrical life. 

#### For Information regarding the columns in each table :
Check My [column description file](https://github.com/Stephen-Data-Engineer-Public/Full-Stack-Data-Analysis/blob/main/IMDB%20MOVIES%20Analysis%20ETL%20-%20Schema%20Modeling%20(1).pdf)
## Business Questions Formulation
### Title : Navigating the Movie Franchise Market for Strategic Growth
**Franchise Performance Analysis:** Assess the performance of different movie franchises based on metrics such as total revenue, number of movies released, and average revenue per movie. Identify top-performing franchises and analyze their growth trajectories over time.

**Market Trends Exploration:** Conduct exploratory data analysis to uncover trends and patterns in the movie franchise market. This includes analyzing revenue trends over time, distribution of movies across franchises, and the impact of factors like release dates and production budgets on box office performance.

**Comparative Franchise Analysis:** Compare the performance of different franchises, genres, and release strategies to identify drivers of success and areas for improvement. Assess the relative performance of franchises in terms of revenue generation, audience engagement, and critical acclaim.

### Planned Solution
**Franchise Performance Analysis**
- Chart 1: This Line chart will present the top 20 franchises ranked by gross revenue generated over the course of the five last years.
- Chart 2: This bar chart will showcase the top 20 franchises ranked by the number of movies released.
- Chart 3: This chart will illustrate the top 20 franchises ranked by their average gross per movie. This is crucial as franchises with numerous movie releases may accumulate higher gross revenue than those with fewer releases.

**Market Trends Exploration**
- A multiple line chart depicting the revenue trend of franchises over a five-year period.
- Scatter plots to explore the correlation between production budget and generated revenue.

**Comparative Franchise Analysis**
- A pie chart to display the distribution of the most recurring genre among the top 100 movies ranked by revenue.
- A bar chart to illustrate the days of the week on which the top 100 movies were released, based on theater opening-week revenue.
