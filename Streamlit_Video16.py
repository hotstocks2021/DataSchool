import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      * How do I handle missing values in pandas?
Video 16 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=fCMrO_VzeL8&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=17
## Pandas Doc String handling: 
https://pandas.pydata.org/pandas-docs/version/0.22/api.html
## Set the display options
:red[pd.set_option('expand_frame_repr', False)]
\n:red[pd.set_option('display.max_colwidth', None)]

## Example 1: 
\n:green[**ufo = pd.read_csv("http://bit.ly/uforeports")**]
\nprint(ufo.:red[tail()])
"""
)
ufo = pd.read_csv("http://bit.ly/uforeports")
st.table(ufo.tail())
st.write(":red[Note: NaN (not a number) or <NA>]")

st.markdown("""
## Example 2:
- Use isnull() and notnull method to detect the missing values
\n:green[ufo.:red[isnull()].tail()]
\nprint(ufo.:red[isnull()].tail())
""")
st.table(ufo.isnull().tail())
st.write(":green[ufo.:red[notnull()].tail()]")
st.write("print(ufo.:red[notnull()].tail())")
st.table(ufo.notnull().tail())

st.markdown("""
## Example 3:
- Use isnull() method to find out the total number of missing values
- :red[Note]: True is equal to 1 and False is equal to 0
\n:green[(ufo.isnull().:red[sum()]]
\nprint(ufo.isnull().:red[sum()])
""")
st.table(ufo.isnull().sum(axis=0))
st.write("Note: method sum is doing :red[axis=0 by default]")

st.markdown("""
## Example 4:
- Use isnull() method to find the missing values from a Dataset
\n:green[ufo:red[[ufo.City.isnull()]]]
\nprint(ufo[ufo.City.isnull()])
""")
st.table(ufo[ufo.City.isnull()])
st.write("print(ufo[ufo.City.isnull() :red[&] ufo[\"Shape Reported\"].isnull()])")
st.table(ufo[ufo.City.isnull() & ufo["Shape Reported"].isnull()])

st.markdown("""
## Example 5:
- Use dropna(how="any") method to drop all rows that have missing values
\nprint(ufo.shape)
""")
st.write(ufo.shape)
st.write("print(ufo.:red[dropna(how=\"any\")].shape)")
st.write("Note: :red[how='any'] means drop row when its column contain N/A")
st.write(ufo.dropna(how="any").shape)
st.write("print(ufo.:red[dropna(how=\"all\")].shape)")
st.write("Note: :red[how='all'] means drop row when all of its column contain N/A")
st.write(ufo.dropna(how="all").shape)
st.write("print(ufo.dropna(:red[subset=[\"City\", \"Shape Reported\"]], how=\"any\").shape)")
st.write("Note: :red[subset=[\"City\", \"Shape Reported\"]] means drop row when either one of those columns contain N/A")
st.write(ufo.dropna(subset=["City", "Shape Reported"], how="any").shape)
st.write("print(ufo.dropna(:red[subset=[\"City\", \"Shape Reported\"]], how=\"all\").shape)")
st.write("Note: :red[subset=[\"City\", \"Shape Reported\"]] means drop row when both of those columns contain N/A")
st.write(ufo.dropna(subset=["City", "Shape Reported"], how="all").shape)

st.markdown("""
## Example 6:
- The value_counts() method of Series is to find how many times each values occur
\n:green[ufo["Shape Reported"].:red[value_counts()]]
\nprint(ufo["Shape Reported"].value_counts())
""")
st.table(ufo["Shape Reported"].value_counts())
st.write("ufo[\"Shape Reported\"].value_counts(:red[dropna=\"False\"])")
st.write("Note: :red[dropna=\"False\"] will include N/A")
st.table(ufo["Shape Reported"].value_counts(dropna=False))

st.markdown("""
## Example 7:
- The fillna() method of Series can be used to replace N/A with something more meaningful
\n:green[ufo["Shape Reported"].:red[fillna(value="VARIOUS", inplace=True)]]
\nprint(ufo["Shape Reported"].value_counts(dropna=False))
""")
ufo["Shape Reported"].fillna(value="VARIOUS", inplace=True)
st.write("Note: VARIOUS was 333; N/A = 2644 + 333 = :red[2977]")
st.table(ufo["Shape Reported"].value_counts(dropna=False))
