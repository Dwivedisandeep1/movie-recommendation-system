import streamlit as st
import pickle
import pandas as pd
import requests



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

movies_dict =  pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('https://drive.google.com/file/d/1BdF6Yr4Vii2brSMnjhd86eT7tE5USaI4/view?usp=sharing','rb'))

st.title('Movie Recommender system')
selected_movie_name = st.selectbox('How would you like to be contacted?',movies['title'].values)

if st.button ('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
