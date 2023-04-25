import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      * Read only specific columns from a DataFrame
##      * Read only specific rows from a DataFrame
##      * Iterate DataFrame
##      * Select only numeric columns from a DataFrame
Video 10 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=B-r9VuK80dk&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=10

## Set the display options
:red[pd.set_option('expand_frame_repr', False)]
\n:red[pd.set_option('display.max_colwidth', None)]

## Example 1: display the UFO DataFrame
\n:green[**ufo = pd.read_csv("http://bit.ly/uforeports")**]
\nprint(ufo.head())
"""
)
ufo = pd.read_csv("http://bit.ly/uforeports")
st.table(ufo.head())
st.write("print(ufo.shape)")
st.write(str(ufo.shape))

st.markdown("""
## Example 2: read only the "City" and "State" from a DataFrame
\n:green[ufo = pd.read_csv("http://bit.ly/uforeports", :red[usecols=["City", "State"]])]
\nReference by indexes; the results are the same as above
\n:green[ufo = pd.read_csv("http://bit.ly/uforeports", :red[usecols=[0, 3]])]
\nprint(movies.head())
""")
ufo = pd.read_csv("http://bit.ly/uforeports", usecols=[0, 3])
st.table(ufo.head())
st.write("print(ufo.shape)")
st.write(str(ufo.shape))

st.markdown("""
## Example 3: take only the first 3 rows of a DataFrame
\n:green[ufo = pd.read_csv("http://bit.ly/uforeports", :red[nrows=3])]
\nprint(movies.head())
""")
ufo = pd.read_csv("http://bit.ly/uforeports", nrows=3)
st.table(ufo.head())
st.write("print(ufo.shape)")
st.write(str(ufo.shape))

st.markdown("""
## Example 4: how to iterate a DataFrame
\nNote: :red["index"] must be included inside the FOR loop, printing of it is optional
\n:green[for index, row in ufo.iterrows():]
\n:green[_____print(row.City, row.State)]
""")
for index, row in ufo.iterrows():
    st.write(row.City, row.State)

st.markdown("""
## Example 5: select only numeric columns from a DataFrame
\n:green[drinks = pd.read_csv("http://bit.ly/drinksbycountry")]
\nprint(drinks.dtypes)
""")
drinks = pd.read_csv("http://bit.ly/drinksbycountry")
st.write(drinks.dtypes)

st.write("\nselect only numeric columns from a DataFrame")
st.write("\nimport numpy as np")
import numpy as np
st.write(":green[drinks.select_dtypes(:red[include=[np.number]]).dtypes]")
st.write(drinks.select_dtypes(include=[np.number]).dtypes)

st.write(":green[drinks.select_dtypes(include=[np.number]).head()]")
st.table(drinks.select_dtypes(include=[np.number]).head())
