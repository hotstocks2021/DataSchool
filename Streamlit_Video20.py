import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      When should I use the "inplace" parameter in pandas?
Note: 


Video 20 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=XaCSdr7pPmY&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=20
## Pandas Doc String handling: 
https://pandas.pydata.org/pandas-docs/version/0.22/api.html
## Set the display options
:red[pd.set_option('expand_frame_repr', False)]
\n:red[pd.set_option('display.max_colwidth', None)]

## Example 1: 
\n:green[**ufo = pd.read_csv("http://bit.ly/uforeports")**]
\nprint(drinks.:red[head()])
"""
)
ufo = pd.read_csv("http://bit.ly/uforeports")
st.table(ufo.head())
st.write("print(ufo.:red[shape])")
st.write(str(ufo.shape))

st.markdown("""
## Example 2:
- use the drop() method to drop one of the column from a dataset
\n:green[ufo.:red[drop("City", axis=1, inplace=True)]]
\nprint(ufo.head())
""")
st.table(ufo.head())

st.markdown("""
## Example 3:
- use assignment statement is the same as inplace=True
\n:green[ufo = ufo.set_index("Time")]
\nprint(ufo.head())
""")
ufo = ufo.set_index("Time")
st.table(ufo.head())
