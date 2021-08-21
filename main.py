import movie_recommendation
import flight_prec
import streamlit as st
PAGES = {
    "Flight Price Predictor": flight_prec,
    "Movie Recommender System": movie_recommendation
}
st.sidebar.title('AI Enabled Prediction')
selection = st.sidebar.radio("Select Anyone", list(PAGES.keys()))
page = PAGES[selection]
page.main()