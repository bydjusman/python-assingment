import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load CSV
df = pd.read_csv("tmdb_5000_movies.csv")

# Fill NaNs and combine columns
df['overview'] = df['overview'].fillna('')
df['tags'] = df['genres'] + " " + df['keywords'] + " " + df['overview']
df['tags'] = df['tags'].str.replace("[^\w\s]", "", regex=True).str.lower()

# Vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(df['tags'].values.astype('U'))

# Similarity
similarity = cosine_similarity(vectors)

# Save required stuff
pickle.dump(df[['title']], open('movies.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("✅ Model saved: movies.pkl & similarity.pkl")
