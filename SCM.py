import streamlit as st
import pandas as pd

#st.title("CSV Splitter")

# Upload CSV file
uploaded_file = st.file_uploader("", type="csv")

if uploaded_file is not None:
    # Read raw lines from the uploaded file
    lines = [line.decode("utf-8").strip().split(",") for line in uploaded_file.readlines()]

    # Extract headers
    header1 = lines[0]   # row 1
    header2 = lines[2]   # row 3

    # Extract data
    data1 = [lines[1]]   # row 2 belongs to header1
    data2 = lines[3:]    # rows after row 3 belong to header2

    # Build DataFrames
    df1 = pd.DataFrame(data1, columns=header1)
    df2 = pd.DataFrame(data2, columns=header2)

    # Retrieve specific fields from df1
    #item = str(df1.at[0, "Item"])

    #st.subheader("Dataset from Header Row 1")
    st.write(df1)

    st.subheader("My Item Header")
    st.write(df2)