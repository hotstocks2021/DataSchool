import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      * When should I use a "groupby" in pandas?
Video 14 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=qy0fDqoMJx8&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=14
## Pandas Doc String handling: 
https://pandas.pydata.org/pandas-docs/version/0.22/api.html
## Set the display options
:red[pd.set_option('expand_frame_repr', False)]
\n:red[pd.set_option('display.max_colwidth', None)]

## Example 1: 
\n:green[**drinks = pd.read_csv("http://bit.ly/drinksbycountry")**]
\nprint(drinks.:red[head()])
"""
)
drinks = pd.read_csv("http://bit.ly/drinksbycountry")
st.table(drinks.head())
st.write("print(drinks.:red[dtypes])")
st.table(drinks.dtypes)
st.write("print(drinks.beer_servings.:red[mean()])")
st.write(drinks.beer_servings.mean())

# Use groupby
print(drinks.groupby("continent").beer_servings.mean())

st.markdown("""
## Example 2:
- Use groupby
\n:green[drinks.:red[groupby("continent")].beer_servings.mean()]
\nprint(drinks.:red[groupby("continent")].beer_servings.mean()))
""")
st.table(drinks.groupby("continent").beer_servings.mean())

st.markdown("""
## Example 3:
- Use groupby with aggregations of math calculation
\n:green[drinks.groupby("continent").beer_servings.:red[agg(["count", "max", "min", "mean"])]]
\nprint(drinks.groupby("continent").beer_servings.agg(["count", "max", "min", "mean"]))
""")
st.table(drinks.groupby("continent").beer_servings.agg(["count", "max", "min", "mean"]))
