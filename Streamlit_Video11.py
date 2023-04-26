import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      * How do I use the "axis" parameter in pandas?
Video 11 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=PtO3t6ynH-8&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=11

## Set the display options
:red[pd.set_option('expand_frame_repr', False)]
\n:red[pd.set_option('display.max_colwidth', None)]

## Example 1: 
\n:green[**drinks = pd.read_csv("http://bit.ly/drinksbycountry")**]
\nprint(drinks.head())
"""
)
drinks = pd.read_csv("http://bit.ly/drinksbycountry")
st.table(drinks.head())
st.write("print(drinks.shape)")
st.write(str(drinks.shape))

st.markdown("""
## Example 2: 
- drop one of the columns using axis=1
- axis=1 is for Columns
\n:green[drinks.drop("continent", :red[axis=1]).head()]
\nprint(drinks.drop("continent", axis=1).head())
""")
st.write(drinks.drop("continent", axis=1).head())

st.markdown("""
## Example 3: 
- drop one of the rows using axis=0
- axis=0 is for Rows
\n:green[drinks.drop(2, :red[axis=0]).head()]
\nprint(drinks.drop(2, axis=0).head())
""")
st.write(drinks.drop(2, axis=0).head())

st.markdown("""
## Example 4: 
- get the :red[mean] of the columns
- :red[axis=0 is set by default]
- :red[axis=0] is the same as :red[axis="index"]
- :red[numeric_only=True will silence a deprecated warning]
\n:green[drinks.mean(:red[numeric_only=True, axis=0])]
\nprint(drinks.mean(numeric_only=True, axis=0))
""")
st.write(drinks.mean(numeric_only=True, axis=0))
st.write("print(drinks.mean(numeric_only=True, :red[axis=\"index\"]))")
st.table(drinks.mean(numeric_only=True, axis="index"))

st.markdown("""
## Example 5: 
- get the mean of the rows
- :red[axis=1] is the same as :red[axis="columns"]
- :red[numeric_only=True will silence a deprecated warning]
\n:green[drinks.mean(:red[numeric_only=True, axis=0])]
\nprint(drinks.mean(numeric_only=True, axis=1).head())
""")
st.write(drinks.mean(numeric_only=True, axis=1).head())
st.write("print(drinks.mean(numeric_only=True, :red[axis=\"columns\"]))")
st.table(drinks.mean(numeric_only=True, axis="columns").head())
