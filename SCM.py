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

    # --- Build single string from df1 ---
    # Specify the order of fields you want
    df1.columns = df1.columns.str.strip()

    # Allocate each field into its own string variable
    round = str(df1.iloc[0]["Round"])
    heat = str(df1.iloc[0]["Heat"])
    gender = str(df1.iloc[0]["Gender"])
    age = (df1.iloc[0]["Age"]
    item = str(df1.iloc[0]["Item"])
    
    if round == "F":
        round = "FINAL"
    else: 
        round = "HEAT "+heat

    if age not in range(0-23):
        age = "SENIOR"
    else: 
        age = "U"+age

    # Now you can build your head string in any order you like
    head = f"{round} {gender} {age} {item}"

    # Display the string instead of the DataFrame
    st.subheader("Header Row 1 Data")
    st.write(head)

    # Specify which columns you want to show
    columns_to_show = ["Place", "Surname", "Firstname", "Number", "Team", "Performance"]

    # Load Poppins font globally
    st.markdown(
        """
        <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
        <style>
        .custom-subheader {
            font-family: 'Poppins', sans-serif;
            font-size: 1.5em;
            font-weight: 600;
            text-transform: uppercase;
            margin-top: 1em;
            margin-bottom: 0.5em;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Use custom styled subheader
    st.markdown('<div class="custom-subheader">Final Women U19 10000m Walk</div>', unsafe_allow_html=True)
    
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

        # Render styled table
    st.markdown(styled.to_html(), unsafe_allow_html=True)