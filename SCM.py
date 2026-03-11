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
    data2 = lines[3:6]    # rows after row 3 belong to header2

    # Build DataFrames
    df1 = pd.DataFrame(data1, columns=header1)
    df2 = pd.DataFrame(data2, columns=header2)

    # Retrieve specific fields from df1
   

    #st.subheader("Dataset from Header Row 1")
    st.write(df1)

    # Specify which columns you want to show
    columns_to_show = ["Place", "Surname", "Firstname", "Number", "Team", "Performance"]

    st.subheader("Final Women U19 10000m Walk")
    
    # Create a Styler with transparent backgrounds
    styled = (
        df2[columns_to_show]
        .style
        .hide(axis="index")  # hide index
        .set_table_styles(
            [
                {"selector": "th", "props": [
                    ("font-family", "Poppins"),
                    ("font-weight", "bold"),
                    ("background-color", "#00000000"),
                    ("text-transform", "uppercase")
                ]},
                {"selector": "td", "props": [
                    ("font-family", "Poppins"),
                    ("text-align", "center"),
                    ("text-transform", "uppercase"),
                    ("background-color", "#00000000")
                ]},
                {"selector": "tr:nth-child(even)", "props": [("background-color", "#00000000")]},
                {"selector": "tr:nth-child(odd)", "props": [("background-color", "#00000000")]}
            ]
        )
    )

    # Load Poppins font globally
    st.markdown(
        """
        <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
        """,
        unsafe_allow_html=True
    )

    # Render styled table
    st.markdown(styled.to_html(), unsafe_allow_html=True)