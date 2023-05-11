import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      More of your pandas questions answered!
Note: 
- How to use the sample method


Video 23 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=oH3wYKvwpJ8&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=23
## Pandas Doc String handling: 
https://pandas.pydata.org/pandas-docs/version/0.22/api.html
## Set the display options
:red[pd.set_option('expand_frame_repr', False)]
\n:red[pd.set_option('display.max_colwidth', None)]

## Example 1: 
\n:green[**ufo = pd.read_csv("http://bit.ly/uforeports")**]
\nprint(ufo.:red[head()])
"""
)
ufo = pd.read_csv("http://bit.ly/uforeports")
st.table(ufo.head())
st.write("print(ufo.:red[shape])")
st.write(str(ufo.shape))

st.markdown("""
## Example 2:
- get three same sample rows
\n:green[print(ufo.:red[sample(n=3))]]
""")
st.table(ufo.sample(n=3))

st.markdown("""
## Example 3:
- get three sample rows
\n:green[print(ufo.:red[sample(n=3, random_state=50))]]
""")
st.table(ufo.sample(n=3, random_state=50))

st.markdown("""
## Example 4:
- get a faction of rows
\n:green[print(ufo.:red[sample(frac=0.0001, random_state=50)])]
""")
st.table(ufo.sample(frac=0.0001, random_state=50))

st.markdown("""
## Example 5:
- get the remaining rows of the faction from the above example
\nprint(:green[ufo.:red[shape])]
""")
st.write(ufo.shape)
st.write(":green[train = ufo.sample(frac=0.0001, random_state=50))]")
train = ufo.sample(frac=0.0001, random_state=50)
st.write("print(:green[train.:red[shape])]")
st.write(train.shape)
test = ufo.loc[~ufo.index.isin(train.index), : ]
st.write(":green[test = ufo.loc[:red[~]ufo.index.isin(train.index), : ]]")
st.write("print(:green[test.:red[shape])]")
st.write(test.shape)