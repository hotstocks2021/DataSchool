import os
import sys
import streamlit as st
import pandas as pd

st.write("Home [link](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

pd.set_option('expand_frame_repr',False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
## How do I rename columns in a pandas DataFrame?
Video 5 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=0uBirYFhizE&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=5

## Set the display options
:red[pd.set_option('expand_frame_repr',False)]
\n:red[pd.set_option('display.max_colwidth', None)]

## Example 1: Display the UFO DataFrame
\n:green[**ufo = pd.read_csv("http://bit.ly/uforeports")**]
\n
\nprint(ufo.head())
"""
)
ufo = pd.read_csv("http://bit.ly/uforeports")
st.table(ufo.head())

st.markdown("""
## Example 2: Display the columns attributes
\n:green[**ufo.columns**]
\nprint(ufo.columns)
""")
st.write(str(ufo.columns))

st.markdown("""
## Example 3: Rename a column
\n:green[**ufo.rename(columns={"Colors Reported":"Colors_Reported", "Shape Reported":"Shape_Reported"}, inplace=True)**]
\nprint(ufo.head())
""")
ufo.rename(columns={"Colors Reported":"Colors_Reported", "Shape Reported":"Shape_Reported"}, inplace=True)
st.table(ufo.head())

st.markdown("""
## Example 4: Replace all column names
\n:green[**ufo_cols = ["city", "colors reports", "shape reported", "state", "time"]**]
\n:green[**ufo.columns = ufo_cols**]
\nprint(ufo.head())
""")
ufo_cols = ["city", "colors reports", "shape reported", "state", "time"]
ufo.columns = ufo_cols
st.table(ufo.head())

st.markdown("""
## Example 5: Rename a column while reading the DataFrame
\n:green[**ufo_cols = ["City", "Colors_Reported", "Shape_Reported", "State", "Time"]**]
\n:green[**ufo = pd.read_csv("http://bit.ly/uforeports", names=ufo_cols, header=0)**]
\n:red[Note]: "header=0" means row zero is a header
\nprint(ufo.head())
""")
ufo_cols = ["City", "Colors_Reported", "Shape_Reported", "State", "Time"]
ufo = pd.read_csv("http://bit.ly/uforeports", names=ufo_cols, header=0)
# "header=0" means row zero is a header
st.table(ufo.head())

st.markdown("""
## Example 6: Replace all columns' whitespace with underscore
\n:green[**ufo = pd.read_csv("http://bit.ly/uforeports")**]
\n:green[**ufo.columns = ufo.columns.str.replace(" ", "_")**]
\nprint(ufo.head())
""")
ufo = pd.read_csv("http://bit.ly/uforeports")
ufo.columns = ufo.columns.str.replace(" ", "_")
st.table(ufo.head())
