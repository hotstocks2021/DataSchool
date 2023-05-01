import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      * How do I select multiple rows and columns from a pandas DataFrame?
Note: 
- :red[loc] is for selecting rows and filtering columns by :red[LABEL], index and column names. (inclusive on both side)
- :red[iloc] is for selecting rows and filtering columns by :red[INTEGER] position (exclusive on the right side)

Video 19 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=xvpNA7bC8cs&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=19
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
- use loc to display row 0 and all columns; the result will be a pandas Series
\n:green[ufo.:red[loc[0, : ]]]
\nprint(ufo.loc[0, :])
""")
st.table(ufo.loc[0, : ])

st.markdown("""
## Example 3:
- use loc to display row 0, 1, and 2 and all columns; the result will be a pandas DataFrame
\n:green[ufo.:red[loc[[0, 1, 2], :]]]
\nprint(ufo.loc[[0, 1, 2], :])
""")
st.table(ufo.loc[[0, 1, 2], :])
st.write("ufo.:red[loc[0:2, : ]]")
st.table(ufo.loc[0:2, : ])

st.markdown("""
## Example 4:
- use loc to display all rows and column "City"; the result will be a pandas Series
\n:green[ufo.:red[loc[:,"City"].head()]]
\nprint(ufo.loc[:,"City"].head())
""")
st.table(ufo.loc[:,"City"].head())

st.markdown("""
## Example 5:
- use loc to display all rows and column "City" and "State"; the result will be a pandas DataFrame
\n:green[ufo.:red[loc[:,["City", "State"]].head()]]
\nprint(ufo.loc[:,["City", "State"]].head())
""")
st.table(ufo.loc[:,["City", "State"]].head())
st.write("ufo.:red[loc[:, \"City\":\"State\"]].head()")
st.table(ufo.loc[:, "City":"State"].head())

st.markdown("""
## Example 6:
- use loc to display all the city = Oakland rows and all columns; the result will be a pandas DataFrame
\n:green[ufo.:red[loc[ufo.City == "Oakland", : ].head()]]
\nprint(ufo.loc[ufo.City == "Oakland", : ].head())
""")
st.table(ufo.loc[ufo.City == "Oakland", : ].head())

st.markdown("""
## Example 7:
- use iloc to display all rows and columns in position 0 and 3; the result will be a pandas DataFrame
\n:green[ufo.:red[iloc[:, [0, 3]].head()]]
\nprint(ufo.iloc[:, [0, 3]].head())
""")
st.table(ufo.iloc[:, [0, 3]].head())
st.write("ufo.:red[iloc[:, 0:4].head()]")
st.write("print(ufo.iloc[:, 0:4].head())")
st.table(ufo.iloc[:, 0:4].head())