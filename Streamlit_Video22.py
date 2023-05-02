import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      How do I use pandas with scikit-learn to create Kaggle submissions?
Note: 


Video 22 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=ylRlGCtAtiE&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=22
## Pandas Doc String handling: 
https://pandas.pydata.org/pandas-docs/version/0.22/api.html
## Set the display options
:red[pd.set_option('expand_frame_repr', False)]
\n:red[pd.set_option('display.max_colwidth', None)]

## Example 1: 
\n:green[**train = pd.read_csv("http://bit.ly/kaggletrain")**]
\nprint(drinks.:red[head()])
"""
)
train = pd.read_csv("http://bit.ly/kaggletrain")
st.table(train.head())
st.write("print(ufo.:red[shape])")
st.write(str(train.shape))

st.markdown("""
## Example 2:
- export dataset to a csv file
\n:green[train.:red[to_csv("train_dataset.csv")]]
""")

st.markdown("""
## Example 3:
- convert a dataset to a pickle file
\n:green[train.:red[to_pickle("train.pkl")]]
""")

st.markdown("""
## Example 4:
- convert a pickle file to a DataFrame
\n:green[train = :red[pd.read_pickle("train.pkl")]]
\nprint(train.head())
""")
st.write(train.head())


