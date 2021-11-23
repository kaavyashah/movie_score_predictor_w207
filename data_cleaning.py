import pandas as pd
import numpy as np
import json

movies = pd.read_csv("data/tmdb_5000_movies.csv")
credits = pd.read_csv("data/tmdb_5000_credits.csv")

unnest = lambda x: [val['name'] for val in json.loads(x)]

# nested data
movies['genre'] = movies['genres'].apply(unnest)
movies['keyword'] = movies['keywords'].apply(unnest)
movies['language'] = movies['spoken_languages'].apply(unnest)
movies['companies'] = movies['production_companies'].apply(unnest)
movies['countries'] = movies['production_countries'].apply(unnest)

# date and time values
movies['release_date'] = pd.to_datetime(movies['release_date'])
movies["year"] = pd.DatetimeIndex(movies["release_date"]).year
movies['month'] = pd.DatetimeIndex(movies['release_date']).month
decade = movies.groupby((movies.release_date.dt.year//10)*10).count()
movies['decade'] = (movies.release_date.dt.year//10)*10

# homepage binarization
movies['homepage'].fillna(0, inplace = True)
movies['homepage_binary'] = np.where(movies['homepage'] == 0, 0, 1)

# budget in millions
movies['budget_mln'] = movies['budget']/1000000

# export cleaned data
movies.to_csv("data/cleaned_movies.csv")
