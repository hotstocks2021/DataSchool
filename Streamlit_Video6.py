import os
import sys
import streamlit as st
import pandas as pd

st.write("Home [link](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

pd.set_option('expand_frame_repr',False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
## How do I remove columns from a pandas DataFrame?
Video 6 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=gnUKkS964WQ&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=6

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
st.write("print(:red[ufo.shape])")
st.write(str(ufo.shape))

st.markdown("""
## Example 2: Remove a column, a string is needed
\n axis=0 is for the row access
\n axis=1 is for the column access
\n:green[**ufo.drop("Colors Reported", :red[axis=1], inplace=True)**]
\nprint(ufo.head())
""")
ufo.drop("Colors Reported", axis=1, inplace=True)
st.table(ufo.head())

st.markdown("""
## Example 3: Drop multiple columns, need a list of string to do that
\n ufo = pd.read_csv("http://bit.ly/uforeports")
\n:green[**ufo.drop(:red[["Colors Reported", "Shape Reported"]], axis=1, inplace=True)**]
\nprint(ufo.head())
""")
ufo = pd.read_csv("http://bit.ly/uforeports")
ufo.drop(["Colors Reported", "Shape Reported"], axis=1, inplace=True)
st.table(ufo.head())

st.markdown("""
## Example 4: Drop rows from a DataFrame, need to use the index (label)
\n ufo = pd.read_csv("http://bit.ly/uforeports")
\n:green[**ufo.drop([0, 1], axis=0, inplace=True)**]
\nprint(ufo.head())
""")
ufo = pd.read_csv("http://bit.ly/uforeports")
ufo.drop([0, 1], axis=0, inplace=True)
st.table(ufo.head())
