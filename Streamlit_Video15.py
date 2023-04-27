import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      * How do I explore a pandas Series?
Video 15 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=QTVTq8SPzxM&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=15
## Pandas Doc String handling: 
https://pandas.pydata.org/pandas-docs/version/0.22/api.html
## Set the display options
:red[pd.set_option('expand_frame_repr', False)]
\n:red[pd.set_option('display.max_colwidth', None)]

## Example 1: 
\n:green[**drinks = pd.read_csv("http://bit.ly/drinksbycountry")**]
\nprint(drinks.:red[head()])
"""
)
movies = pd.read_csv("http://bit.ly/imdbratings")
st.table(movies.head())
st.write("print(movies.:red[dtypes])")
st.table(movies.dtypes)
st.write("print(movies.genre.:red[describe()])")
st.table(movies.genre.describe())

st.markdown("""
## Example 2:
- Use the value_count() method
\n:green[movies.genre.:red[value_counts()]]
\nprint(movies.genre.value_counts())
""")
st.table(movies.genre.value_counts())

st.markdown("""
## Example 3:
- Use the value_count() method and convert it to percentage
\n:green[movies.genre.value_counts(:red[normalize=True])]
\nprint(movies.genre.value_counts(normalize=True))
""")
st.table(movies.genre.value_counts(normalize=True))

st.markdown("""
## Example 4:
- The result of the method value_counts() is a Series; therefore, you can use the Series methods.
---
\n:green[type(movies.genre.value_counts())]
\nprint(:red[type](movies.genre.value_counts()))
""")
st.write(str(type(movies.genre.value_counts())))
st.markdown("""---""")
st.write("\nprint(movies.genre.value_counts():red[.head()])")
st.table(movies.genre.value_counts().head())

st.markdown("""
## Example 5:
- The unique() method of Series
\n:green[movies.genre.:red[unique()]]
\nprint(movies.genre.unique())
""")
st.table(movies.genre.unique())

st.markdown("""
## Example 6:
- The nunique() method of Series is to find the number of uniqueness
\n:green[movies.genre.:red[nunique()]]
\nprint(movies.genre.nunique())
""")
st.write(movies.genre.nunique())

st.markdown("""
## Example 7:
- Crosstab method
\n:green[:red[pd.crosstab](movies.genre, movies.content_rating)]
\nprint(pd.crosstab(movies.genre, movies.content_rating))
""")
st.table(pd.crosstab(movies.genre, movies.content_rating))

st.markdown("""
## Example 8:
- Describe method
\n:green[movies.duration.:red[describe()]]
\nprint(movies.duration.describe())
""")
st.table(movies.duration.describe())
