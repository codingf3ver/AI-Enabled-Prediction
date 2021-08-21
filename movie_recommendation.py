import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import time

def main():

    html_temp = """
            <div style="background-color:purple;padding:10px">
            <h2 style="color:black;text-align:center;">Welcome to Movie Recommendation System </h2>
            </div>
            """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Reading file .....
    df = pd.read_csv(
        "/Users/quantum/Desktop/recomender/Recommender_Data/movie_dataset.csv")

    # Selecting features ...
    com_features = ['keywords', 'cast', 'genres', 'director']

    # Filling NaN Values
    for f in com_features:
        df[f] = df[f].fillna('')

    # Combining All features into a single column
    def com_features(r):
        try:
            return r['keywords'] + " " + r['cast'] + " " + r['genres'] + " " + r['director']
        except:
            print("Unwanted Data:", r)

    df['Com_features'] = df.apply(com_features, axis=1)

    # Creating count vectorizer for combined column
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df['Com_features'])

    # Finding cosine similarity for combined column
    cosine_similar = cosine_similarity(count_matrix)

    # Getting input text from the user
    movie_input = st.text_input("Enter a movie title: ", 'Avatar')

    # Finding Index of movie from title column

    def get_index_from_title(title):
        return df[df.title == title]["index"].values[0]

    movie_index = get_index_from_title(movie_input)
    similar_movies = list(enumerate(cosine_similar[movie_index]))

    # Getting  a list of similar movies in descending order of similarity score
    sorted_similar_movies = sorted(
        similar_movies, key=lambda x: x[1], reverse=True)

    # Now printing titles of first 10 movies
    def get_title_from_index(index):
        return df[df.index == index]["title"].values[0]

    for movie in sorted_similar_movies[1:30]:
        st.write(get_title_from_index(movie[0]))

    html = """
            <div style="background-color:purple;padding:3px">
            <h3 style="color:black;text-align:center;">@Copyright Md Tausif </h3>
            </div>
            """
    st.markdown(html, unsafe_allow_html=True)
    time.sleep(2)
    st.balloons()


if __name__ == '__main__':
    main()
