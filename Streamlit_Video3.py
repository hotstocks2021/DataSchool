import os
import sys
import streamlit as st
import pandas as pd

#st. set_page_config(layout="wide")
st.markdown("""
## How do I select a Pandas Series from a DataFrame?
Video 3 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=zxqjeyKP2Tk&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=3

## Set the display options
:red[pd.set_option('expand_frame_repr',False)]
\n:red[pd.set_option('display.max_colwidth', None)]

## Example 1 read commas separated table using :red[read_table]
\n:green[**ufo = pd.read_table("http://bit.ly/uforeports", :red[sep=","])**]
\nprint(ufo.head())
"""
)
ufo = pd.read_table("http://bit.ly/uforeports", sep=",")
st.table(ufo.head())

st.markdown("""
## Example 2 read commas separated table using :red[read_csv]
\n:green[**ufo = pd.read_csv("http://bit.ly/uforeports")**]
\nprint(ufo.head())
""")
ufo = pd.read_table("http://bit.ly/uforeports", sep=",")
st.table(ufo.head())

st.markdown("""
## Example 3 :red[select a Series from a DataFrame]
\n:green[**ufo["City"].head()**]
""")
st.write("print(ufo[\"City\"].head())")
st.table(ufo["City"].head())

st.write("print(type(ufo[\"City\"]))")
data_type = type(ufo["City"])
data_type = str(data_type)
st.write(data_type)

st.markdown("""
## Example 4 :red[Alternative way of example 3]
\n:green[**ufo.City.head()**]
\n:red[Note]: This method will not work with column name that has white space in between. IE: :red["Colors Reported"].
""")
st.write("print(ufo.City.head())")
st.table(ufo.City.head())

st.write("print(type(ufo.City))")
data_type = type(ufo.City)
data_type = str(data_type)
st.write(data_type)

st.markdown("""
## Example 5 :red[Create a new Series]
\n:green[**ufo.City.head() + ", " + ufo.State.head()**]
""")
st.write("print(ufo.City.head() + ", " + ufo.State.head())")
data = ufo.City.head() + ", " + ufo.State.head()
data_type = str(data)
st.table(ufo.City.head() + ", " + ufo.State.head())

st.markdown("""
## Example 6 :red[Create a new Series and assign a name]
\n:green[**ufo["Location"] = ufo.City.head() + ", " + ufo.State.head()**]
""")
ufo["Location"] = ufo.City.head() + ", " + ufo.State.head()
st.write("print(ufo.head())")
st.table(ufo.head())
