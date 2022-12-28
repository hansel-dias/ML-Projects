from urllib import request
import streamlit as st
import pickle
import pandas as pd 
import requests

st.title('Movie Recommendation System')
API_KEY = "526bf60f6c879bf801a9b40523520d26"

# path = r"C:\Users\hanse\OneDrive\Desktop\ML Projects\Movie Recommendation system\archive\movies_dict.pkl"
path = "movies_dict.pkl"
SIMILARITY_PATH  = "similarity.pkl"
# SIMILARITY_PATH  = r"C:\Users\hanse\OneDrive\Desktop\ML Projects\Movie Recommendation system\archive\similarity.pkl"
movies_dict = pickle.load(open(path,'rb')) 
movies = pd.DataFrame(movies_dict)
movies_list = movies['title'].values
print(movies_list)

movie_selected = st.selectbox(
    'Select Your Favourite Movie from the list below',
    (movies_list))
cs = pickle.load(open(SIMILARITY_PATH,'rb'))



def fetch_poster(id):
       TMDB_URL = f"https://api.themoviedb.org/3/movie/{id}?api_key={API_KEY}&language=en-US"
       # TMDB_URL = f"https://api.themoviedb.org/3/movie"

       response = requests.get(url=TMDB_URL)
       data = response.json()
       poster = data['poster_path']
       poster_path = f"https://image.tmdb.org/t/p/w500/{poster}"
       return poster_path



def recommend(movie):
       ind = movies[movies['title'] == movie].index[0] # get index of movie 
       distances = cs[ind] # calculate vector distance between them
       movies_list = sorted(enumerate(distances),reverse=True,key=lambda x:x[1])[1:6] # get a sorted list starting from movies with less distances and recommend first five
       
       recommended_movies = []
       recommended_movies_posters = []

       for i in movies_list:
             id = movies.iloc[i[0]].movie_id

             recommended_movies.append(movies.iloc[i[0]].title)
             recommended_movies_posters.append(fetch_poster(id))
       #       st.text(movies.iloc[i[0]].title)
       #       st.image(url=fetch_poster(id=id))
       #       print(movies.iloc[i[0]].title)
       return recommended_movies,recommended_movies_posters

if st.button('Recommend'):
       title,posters = recommend(movie_selected)
       
       col1, col2, col3,col4, col5 = st.columns(5)
       with col1:
              st.text(title[0])
              st.image(posters[0])

       with col2:
              st.text(title[1])
              st.image(posters[1])

       with col3:
              st.text(title[2])
              st.image(posters[2])

       with col4:
              st.text(title[3])
              st.image(posters[3])

       with col5:
              st.text(title[4])
              st.image(posters[4])
              


# st.write('You selected:', movie_selected)