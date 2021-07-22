"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
from sklearn.preprocessing import MultiLabelBinarizer

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    html_template = """
    <div style="background-color:white;padding:10px;border-radius:20px;margin:5px;">
    <h1 style="color:black;text-align:center; text-shadow:2px 2px #ff0000">EDSA Movie Recommendation Challenge</h1>
    <h3 style="color:black;text-decoration:underline">EVERYTHING is Recommended.</h3>
    <h3 style="color:black;">TEAM ZM6_UNSUPERVISED LEARNING</h3>
    </div>
    """

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Home","Recommender System","Solution Overview","Exploratory Data Analysis","Contact us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    

    if page_selection == "Exploratory Data Analysis":
        st.title("Exploratory Data Analysis")
        st.write("Exploratory Data Analysis (EDA) is an important step in the Data Science Process.")
        st.write("EDA consists of comprehensively examining the dataset before using the dataset in training a model.")
        st.write("The core of EDA involves identifying key relationships that exist between features in the dataset and how these features interact to alter the target variable")
        st.write("EDA includes performing analysis using a myriad of statistical and data visualisation techniques.") 
        
        if st.checkbox("Genres"):
            st.subheader("Top Genres")
            st.image('resources/imgs/common_genres.png',use_column_width=True)
        
        if st.checkbox("Movies"):
            st.subheader("Popular Movies")
            st.image('resources/imgs/most_watched.png',use_column_width=True)

        if st.checkbox("Ratings"):
            st.subheader("Number of Ratings")
            st.image('resources/imgs/ratings.png',use_column_width=True)

        if st.checkbox("Directors"):
            st.subheader("Movies per Director")
            st.image('resources/imgs/directors.png',use_column_width=True)

    if page_selection == "Home":
        st.markdown(html_template.format('royalblue','white'), unsafe_allow_html=True)
        st.image('resources/imgs/movies.jpg',use_column_width=True) 

    if page_selection == "Contact us":
        st.header("Contact us")
        st.subheader("Let`s start a conversation")
        st.write("Address: 19 Amershoff, Braamfontein")
        st.write("Contacts: +27710258594")
        st.write("E-mail: unsupervised@explore.net")

        


    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
