import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      How do I find and remove duplicate rows in pandas?
Note: 


Video 26 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=ht5buXUMqkQ&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=26
## Pandas Doc :red[String] handling: 
https://pandas.pydata.org/pandas-docs/version/0.22/api.html

## Pandas Doc :red[Datetime Properties] handling: 
https://pandas.pydata.org/pandas-docs/version/0.22/api.html#datetimelike-properties

## Set the display options
:red[pd.set_option('expand_frame_repr', False)]
\n:red[pd.set_option('display.max_colwidth', None)]

## Example 1: 
\n:green[**user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']**]
\n:green[**users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols, index_col="user_id")**]
\nprint(ufo.:red[head()])
"""
)
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols, index_col="user_id")
st.table(users.head())
st.write("print(ufo.:red[shape])")
st.write(str(users.shape))
st.write("print(ufo.:red[dtypes])")
st.table(users.dtypes)

st.markdown("""
## Example 2:
- find the duplicated of the Series
\nprint(users.zip_code.duplicated().sum())
""")
st.write(users.zip_code.duplicated().sum())

st.markdown("""
## Example 3:
- find the duplicated of the DataFrame
\nprint(users.duplicated().sum())
""")
st.write(users.duplicated().sum())

st.markdown("""
## Example 4:
- print out of the duplicates
\nprint(users.loc[:red[users.duplicated()], : ])
""")
st.table(users.loc[users.zip_code == "55414", : ])
st.table(users.loc[users.duplicated(), : ])

st.markdown("""
## Example 5:
- print out of the duplicates of the :red[first] occurrence
""")
st.write("print(users.loc[:red[users.zip_code == \"55414\"], : ])")
st.table(users.loc[users.zip_code == "55414", : ])
st.write("print(users.loc[:red[users.duplicated(keep=\"first\")], : ])")
st.table(users.loc[users.duplicated(keep="first"), : ])

st.markdown("""
## Example 6:
- print out of the duplicates of the :red[last] occurrence
""")
st.write("print(users.loc[:red[users.zip_code == \"55414\"], : ])")
st.table(users.loc[users.zip_code == "55414", : ])
st.write("print(users.loc[:red[users.duplicated(keep=\"last\")], : ])")
st.table(users.loc[users.duplicated(keep="last"), : ])

st.markdown("""
## Example 7:
- print out of the duplicates of the :red[last] occurrence
""")
st.write("print(users.loc[:red[users.zip_code == \"55414\"], : ])")
st.table(users.loc[users.zip_code == "55414", : ])
st.write("print(users.loc[:red[users.duplicated(keep=False), : ]]:red[.sort_values(by=[\"age\"])])")
st.table(users.loc[users.duplicated(keep=False), : ].sort_values(by=["age"]))

st.markdown("""
## Example 8:
- drop the duplicates by occurrence first
""")
st.write("print(ufo.:red[shape])")
st.write(str(users.shape))
st.write("print(users.:red[duplicated().sum()])")
st.write(str(users.duplicated().sum()))
st.write("print(users.:red[drop_duplicates(keep=\"first\").shape])")
st.write(str(users.drop_duplicates(keep="first").shape))

st.markdown("""
## Example 9:
- drop the duplicates by :red["age"] and :red["zip_code"]
""")
st.write("print(ufo.:red[shape])")
st.write(str(users.shape))
st.write("print(users.:red[duplicated(subset=[\"age\", \"zip_code\"]).sum()])")
# print(users.duplicated(subset=["age", "zip_code"]).sum())
st.write(str(users.duplicated(subset=["age", "zip_code"]).sum()))
st.write("print(users.:red[drop_duplicates(keep=\"first\").shape])")
st.write(str(users.drop_duplicates(subset=["age", "zip_code"]).shape))

