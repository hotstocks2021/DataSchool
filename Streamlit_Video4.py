import os
import sys
import streamlit as st
import pandas as pd

pd.set_option('expand_frame_repr',False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
## Why do some pandas commands end with parentheses (and others don't)?
Video 4 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=hSrDViyKWVk&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=4
\n   Parenthesis (action) = method
\n   No parenthesis (attribute) = description of what something is.

## Set the display options
:red[pd.set_option('expand_frame_repr',False)]
\n:red[pd.set_option('display.max_colwidth', None)]

## Example 1: Display the action Describe
\n:green[**movies = pd.read_csv("http://bit.ly/imdbratings")**]
\nprint(movies.head())
"""
)
movies = pd.read_csv("http://bit.ly/imdbratings")
st.table(movies.head())
st.write("movies.describe()")
st.write(":red[Note]: As long as there's one numeric column, it will display numeric statistic value for all columns.")
st.table(movies.describe())

st.markdown("""
## Example 2: Display the total rows and columns of a DataFrame
\n:green[**movies.shape**]
\nprint(movies.shape)
""")
st.write(str(movies.shape))

st.markdown("""
## Example 3: Display the data type of all columns
\n:green[**movies.dtypes**]
\nprint(movies.dtypes)
""")
st.table(movies.dtypes)

st.markdown("""
## Example 4: Display the type of a object
\n:green[**type(movies)**]
\nprint(type(movies))
""")
st.write(str(type(movies)))

st.markdown("""
## Example 5: Display the description of a column type object
\n:green[**movies.describe(include=["object"])**]
\nprint(movies.describe(include=["object"]))
""")
st.table(movies.describe(include=["object"]))