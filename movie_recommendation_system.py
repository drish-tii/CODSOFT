import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample movie data
movies = pd.DataFrame({
    'title': ['The Matrix', 'John Wick', 'The Dark Knight', 'Inception', 'Interstellar', 'The Avengers', 'The Godfather', 'Pulp Fiction'],
    'genres': ['Sci-Fi', 'Action', 'Action', 'Sci-Fi', 'Sci-Fi', 'Action', 'Crime', 'Crime']
})

# Create a TF-IDF Vectorizer for the genres
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies['genres'])

# Compute cosine similarity between movies based on genres
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Create a mapping of movie titles to indices
indices = pd.Series(movies.index, index=movies['title']).to_dict()

def get_recommendations(title, cosine_sim=cosine_sim):
    """ Get recommendations for a given movie title. """
    idx = indices.get(title)
    if idx is None:
        return []  # Movie title not found in the dataset
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:5]  # Get top 4 similar items, excluding the item itself
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices]

def recommend_movies_based_on_user_likes(user_likes):
    """ Recommend movies based on a list of user liked movies. """
    recommendations = set()
    for movie in user_likes:
        if movie in indices:
            recommendations.update(get_recommendations(movie))
        else:
            print(f"Movie '{movie}' not found in the dataset.")
    return recommendations

def main():
    print("Welcome to the Movie Recommendation System!")
    
    # Get user's liked movies as input
    user_input = input("Enter your liked movies (separated by commas): ")
    user_likes = [movie.strip() for movie in user_input.split(',')]
    
    # Get recommendations
    recommendations = recommend_movies_based_on_user_likes(user_likes)
    
    if recommendations:
        print("\nRecommended movies based on your preferences:")
        for movie in recommendations:
            print(movie)
    else:
        print("No recommendations found. Please check if the movie titles are correct and try again.")

if __name__ == "__main__":
    main()
