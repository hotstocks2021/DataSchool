import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
## How do I apply multiple filter criteria to a pandas DataFrame?
Video 9 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=YPItfQ87qjM&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=9

## Set the display options
:red[pd.set_option('expand_frame_repr', False)]
\n:red[pd.set_option('display.max_colwidth', None)]

## Example 1: Display the movies DataFrame
\n:green[**movies = pd.read_csv("http://bit.ly/imdbratings")**]
\nprint(movies.head())
"""
)
movies = pd.read_csv("http://bit.ly/imdbratings")
st.table(movies.head())
st.write("print(movies.shape)")
st.write(str(movies.shape))

st.markdown("""
## Example 2: filter one column of the DataFrame
\n:green[movies[movies.duration >= 200].sort_values("duration")]
\nprint(movies[movies.duration >= 200].sort_values("duration"))
""")
st.table(movies[movies.duration >= 200].sort_values("duration", ascending=False))

st.markdown("""
## Example 3: filter two columns of the DataFrame
\n:green[movies[(movies.duration >= 200) & (movies.genre == "Drama")]]
\nprint(movies[(movies.duration >= 200) & (movies.genre == "Drama")].sort_values("duration", ascending=False))
""")
st.table(movies[(movies.duration >= 200) & (movies.genre == "Drama")].sort_values("duration", ascending=False))

st.markdown("""
## Example 4: filter the columns of the DataFrame by using :red[isin()]
\n:green[movies.genre.:red[isin(["Drama", "Crime", "Action"]]]
\nprint(movies[(movies.duration >= 200) & (movies.genre.isin(["Drama", "Crime", "Action"]))].sort_values("duration", ascending=False))
""")
st.table(movies[(movies.duration >= 200) & (movies.genre.isin(["Drama", "Crime", "Action"]))].sort_values("duration", ascending=False))





