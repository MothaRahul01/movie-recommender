import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------
movies_path = r"replace this path"  # update if needed
ratings_path = r"replace this path"  # update if needed

# Load movies dataset
movies = pd.read_csv(
    movies_path,
    sep='|',
    encoding='latin-1',
    header=None,
    usecols=[0, 1, 2],
    names=['movieId', 'title', 'genres']
)

ratings = pd.read_csv(
    ratings_path,
    sep='\t',
    header=None,
    names=['userId', 'movieId', 'rating', 'timestamp']
)

print("Movies dataset:\n", movies.head(), "\n")
print("Ratings dataset:\n", ratings.head(), "\n")

# -------------------------------
movies['genres'] = movies['genres'].fillna('')
movies['features'] = movies['genres']

# -------------------------------
count = CountVectorizer(tokenizer=lambda x: x.split('|'))
count_matrix = count.fit_transform(movies['features'])
cosine_sim = cosine_similarity(count_matrix, count_matrix)
print("Cosine similarity matrix computed. Shape:", cosine_sim.shape)

# -------------------------------

def recommend_movies(title, cosine_sim=cosine_sim):
    # Case-insensitive partial match
    matches = movies[movies['title'].str.lower().str.contains(title.lower())]
    
    if matches.empty:
        return f"Movie '{title}' not found in the dataset."
    
    idx = matches.index[0]  # take first match
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # top 5 excluding itself
    
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].tolist()


if __name__ == "__main__":
    movie_input = input("Enter a movie you like: ")
    recommended_movies = recommend_movies(movie_input)
    
    print("\nTop 5 movie recommendations for you:")
    if isinstance(recommended_movies, list):
        for i, movie in enumerate(recommended_movies, 1):
            print(f"{i}. {movie}")
    else:
        print(recommended_movies)
