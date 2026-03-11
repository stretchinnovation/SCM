import pandas as pd
import streamlit as st

#print ("Hello world!")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file:
    # Read the whole file as raw text
    with open("your_file.csv", "r") as f:
        lines = [line.strip().split(",") for line in f.readlines()]

    # Extract headers
    header1 = lines[0]   # row 1
    header2 = lines[2]   # row 3

    # Extract data
    # Row 2 belongs to header1
    data1 = [lines[1]]
    # All rows after row 3 belong to header2
    data2 = lines[3:]

    # Build DataFrames
    df1 = pd.DataFrame(data1, columns=header1)
    df2 = pd.DataFrame(data2, columns=header2)

    st.dataframe(df1.head())
    st.dataframe(df2.head())