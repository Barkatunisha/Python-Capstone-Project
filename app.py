# Importing required modules
from flask import Flask, request, render_template
import requests
import pandas as pd
import random

app = Flask(__name__)

# API Key taken from TMDB
API_KEY = '5304510a12ddff3661c7b092583a3c4f'

# 1st function to get movie data from TMDB
def movie_data(query):
    try:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={query}"
        response = requests.get(url)
        response.raise_for_status()
        movies = response.json().get('results', [])
        
        if movies:
            df_movies = pd.DataFrame(movies)
            return df_movies
        else:
            return pd.DataFrame()
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movies: {e}")
        return pd.DataFrame()

# 2nd function to get random movie sorting by popularity
def get_random_movie():
    try:
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&sort_by=popularity.desc"
        response = requests.get(url)
        response.raise_for_status()
        movies = response.json().get('results', [])
        if movies:
            return random.choice(movies)
        else:
            return {}
    except requests.exceptions.RequestException as e:
        print(f"Error fetching random movie: {e}")
        return {}

# homepage route
@app.route('/')
def home():
    return render_template('index.html')

#  movie search random route 
@app.route('/recommend', methods=['POST'])
def recommend():
    query = request.form.get('query')
    random_movie = request.form.get('random_movie')
    
    if random_movie:
        movie = get_random_movie()
        if movie:
            return render_template('index.html', movie=movie)
        else:
            return render_template('index.html', error="No random movie found")
    
    df_movies = movie_data(query)
    
    if not df_movies.empty:
        return render_template('index.html', movie=df_movies.iloc[0].to_dict())
    else:
        return render_template('index.html', error="No movies found with the given name")

if __name__ == "__main__":
    app.run(debug=True)
