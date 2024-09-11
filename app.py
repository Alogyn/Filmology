from flask import Flask, render_template, request
import pandas as pd
from tmdbv3api import TMDb, Movie
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from urllib.parse import unquote

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize TMDb with your API key
tmdb = TMDb()
tmdb.api_key = 'Your_tmdp.api_key_here'

# Load the movie dataset
df = pd.read_csv("dataset/movies2.csv", delimiter=";", encoding='ISO-8859-1')

# Preprocess the data for content-based filtering
df['info'] = df[['name', 'genre', 'director', 'writer', 'star', 'company']].apply(lambda x: ' '.join(x.astype(str)),
                                                                                  axis=1)
countV = CountVectorizer(min_df=20, stop_words='english')
matrice_transform = countV.fit_transform(df['info'])
cosine_sim = cosine_similarity(matrice_transform)


def get_movie_poster(movie_title):
    """
    Fetches the movie poster URL from TMDb based on the movie title.
    """
    movie = Movie()
    try:
        search = movie.search(movie_title)
        if search:
            poster_path = search[0].poster_path
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"
    except Exception as e:
        print(f"Error fetching poster for '{movie_title}': {e}")
    return None


def film_recommander(titre, data, matrice_score, nombre=5):
    """
    Recommends movies similar to the given title based on cosine similarity.
    """
    lignes = data.index[data['name'].str.lower() == titre.lower()]
    if len(lignes) == 0:
        return [{'titre': 'Sorry ! No similar movie found.', 'poster': None}]

    ligne = lignes[0]
    if ligne >= len(matrice_score):
        return []

    films_similaires = list(enumerate(matrice_score[ligne]))
    recommandations = sorted(films_similaires, key=lambda x: x[1], reverse=True)
    top_films_recommandes = recommandations[1:nombre + 1]

    films_recommandes = []
    for i in range(len(top_films_recommandes)):
        indice_film = top_films_recommandes[i][0]
        if indice_film < len(data):
            titre_film = data.iloc[indice_film]['name']
            poster_url = get_movie_poster(titre_film)
            films_recommandes.append({'titre': titre_film, 'poster': poster_url})
    return films_recommandes


def get_movie_details(movie_title):
    """
    Fetches detailed information about a movie from TMDb based on the movie title.
    """
    movie = Movie()
    try:
        search = movie.search(movie_title)
        if search:
            movie_id = search[0].id
            return movie.details(movie_id)
    except Exception as e:
        print(f"Error fetching details for '{movie_title}': {e}")
    return None


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Renders the index page where users can input a movie title for recommendations.
    """
    return render_template('index.html')


@app.route('/recommendation', methods=['POST'])
def recommendation():
    """
    Handles the movie recommendation logic and renders the recommendations page.
    """
    utilisateur = request.form['titre']
    recommandations = film_recommander(titre=utilisateur, data=df, matrice_score=cosine_sim, nombre=5)
    movie_details = get_movie_details(utilisateur)  # Fetch details for the searched movie

    # Determine if movie details were found
    movie_exists = movie_details is not None
    # Determine if recommendations are empty
    recommendations_empty = len(recommandations) == 0 or recommandations[0][
        'titre'] == 'Sorry ! No similar movie found.'

    return render_template('recommendation.html',
                           recommandations=recommandations,
                           last_query=utilisateur,
                           movie_details=movie_details,
                           movie_exists=movie_exists,
                           recommendations_empty=recommendations_empty)

@app.route('/movie/<title>')
def movie_detail(title):
    """
    Renders the movie details page for a specific movie title.
    """
    title_decoded = unquote(title)
    details = get_movie_details(title_decoded)
    return render_template('movie_details.html', details=details, error=None if details else "Movie details not found")


if __name__ == '__main__':
    app.run(debug=True)