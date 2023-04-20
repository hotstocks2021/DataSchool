import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
## How do I sort a pandas DataFrame or a Series?
Video 7 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=zY4doF6xSxY&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=7

## Set the display options
:red[pd.set_option('expand_frame_repr', False)]
\n:red[pd.set_option('display.max_colwidth', None)]

## Example 1: Display the UFO DataFrame
\n:green[**movies = pd.read_csv("http://bit.ly/imdbratings")**]
\nprint(movies.head())
"""
)
movies = pd.read_csv("http://bit.ly/imdbratings")
st.table(movies.head())
st.write("print(movies.shape)")
st.write(str(movies.shape))

st.markdown("""
## Example 2: sort by column
\n:green[**movies.title.sort_values()**]
\n:green[**movies["title"].sort_values()**]
\n:green[**movies["title"].sort_values(ascending=False)**]
\nprint(movies.head())
""")
st.table(movies.head())
st.write(":red[Note]: Below three lines will return the same results")
st.write("print(movies.title.sort_values())")
st.write("print(movies[\"title\"].sort_values()))")
st.write("print(movies[\"title\"].sort_values(ascending=True)))")
st.table(movies["title"].sort_values(ascending=True).head())

st.markdown("""
## Example 3: sort by multiple columns
\n:green[**movies.sort_values(["content_rating", "duration"])**]
\nprint(movies.sort_values(["content_rating", "duration"]))
""")
st.table(movies.sort_values(["content_rating", "duration"]).head())

st.write(":green[movies.sort_values([\"content_rating\", \"duration\"], ascending=False))]")
st.write("print(movies.sort_values([\"content_rating\", \"duration\"], ascending=False))")
st.table(movies.sort_values(["content_rating", "duration"], ascending=False).head())

