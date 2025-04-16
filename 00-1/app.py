# app.py
import streamlit as st
import pickle
import pandas as pd

# Load model
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = list(enumerate(similarity[movie_index]))
    sorted_movies = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]
    
    recommended_movies = []
    for i in sorted_movies:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox("Select a movie you like", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.subheader("You might also like:")
    for movie in recommendations:
        st.write("👉", movie)
