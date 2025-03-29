# Import necessary libraries
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


st.title("Welcome to My Python Project...1")


st.header("Project Overview")


st.write("This project is designed to demonstrate the capabilities of Python in data analysis and visualization.")

st.image("image.jpg", caption="Project Logo", width=200)


st.header("Features")


st.write("* Data Analysis")
st.write("* Data Visualization")
st.write("* Machine Learning")


st.header("Get Started")


if st.button("Explore Data"):
    st.write("Data exploration page")


with st.sidebar:
    st.header("Navigation")
    st.write("Select a page:")
    page = st.selectbox("Pages", ["Home", "Data", "Visualizations", "About"])
    if page == "Data":
        st.write("Data page")
    elif page == "Visualizations":
        st.write("Visualizations page")
    elif page == "About":
        st.write("About page")



st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px;
            font-size: 14px;
        }
    </style>
    <div class="footer">
        © 2023 My Python Project
    </div>
""", unsafe_allow_html=True)
