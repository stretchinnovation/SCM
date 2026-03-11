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

    # Example: specify the fields you want, in order
    #fields = ["Round", "Gender", "Age", "Item"]  # replace with your actual column names

    # Extract values from the first row of df1 in that order
    #values = [str(df1.loc[0, field]) for field in fields]
    round = df1.loc[0, "Round"]
    gender = df1.loc[0, "Gender"]
    age = df1.loc[0, "Age"]
    item = df1.loc[0, "Item"]
    # Concatenate into a single string
    head = round+" "+gender+" "+age+" "+item
    #st.subheader("Dataset from Header Row 1")
    #st.write(df1)

    st.subheader(head)
    st.write(df2)