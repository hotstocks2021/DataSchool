import os
import sys
import streamlit as st
import pandas as pd

st.write("Home [link](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

#st. set_page_config(layout="wide")
st.markdown("""
## How do I read a tabular data file into pandas?
Video 2 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=5_QXMwezPJE&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=2

## Set the display options
:red[pd.set_option('expand_frame_repr',False)]
\n:red[pd.set_option('display.max_colwidth', None)]

## Example 1 without using read table options
\n:green[**movieusers = pd.read_table("http://bit.ly/movieusers")**]
"""
)

movieusers = pd.read_table("http://bit.ly/movieusers")
st.table(movieusers.head())

st.markdown("""
## Example 2 using read table options
print("\nMovie Users Table:")
\n:red[user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']]
\n:green[**movieusers = pd.read_table("http://bit.ly/movieusers", sep="|", header=None, names=user_cols, skiprows=None)**]

#Pandas read table documentation:
#https://pandas.pydata.org/docs/reference/api/pandas.read_table.html

\n:red[#sep = seperated by |]
\n:red[#header = header of the table]
\n:red[#names = use as the column names]
\n:red[#skiprows = specify the number of rows to skip]

print(movieusers.head())
""")

print("\nMovie Users Table:")
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
# user_cols = ['user_id', 'age', 'gender', 'occupation']
movieusers = pd.read_table("http://bit.ly/movieusers", sep="|", header=None, names=user_cols, skiprows=None)

st.table(movieusers.head())
