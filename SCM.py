import pandas as pd
import streamlit as st

#print ("Hello world!")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    #st.subheader("Preview of Data")
    st.dataframe(df.head())