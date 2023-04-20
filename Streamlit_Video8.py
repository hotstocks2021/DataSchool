import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
## How do I filter rows of a pandas DataFrame by column value?
Video 8 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=2AFGPdNn4FM&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=8

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
## Example 2: filter rows
\n:green[booleans = []]
\n:green[for length in movies.duration:]
\n:green[_____if length >= 200:]
\n:green[__________booleans.append(True)]
\n:green[_____else:]
\n:green[__________booleans.append(False)]
\nprint(booleans[0:5])
""")

booleans = []
for length in movies.duration:
    if length >= 200:
        booleans.append(True)
    else:
        booleans.append(False)

st.write(str(booleans[0:5]))

st.write("print(len(booleans))")
st.write(str(len(booleans)))

st.write("print(movies[booleans].sort_values(\"duration\", ascending=False))")
st.table(movies[booleans].sort_values("duration", ascending=False))

st.markdown("""
## Example 3: filter rows
\n:green[**booleans = movies.duration >= 200**]
\nprint(movies[booleans].sort_values("duration", ascending=False)))
""")
booleans = movies.duration >= 200
st.table(movies[booleans].sort_values("duration", ascending=False))

st.markdown("""
## Example 4: filter rows
\nprint(:green[movies[movies.duration >= 200].sort_values("duration", ascending=False))])
""")
st.table(movies[movies.duration >= 200].sort_values("duration", ascending=False))





