import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      * What do I need to know about the pandas index? (Part 1)
- Note: The reason we need index:
-      1: identification
-       2: selection
-       3: alignment
Video 17 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=OYZNk7Z9s6I&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=17
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
st.write("print(drinks.:red[index])")
st.write(str(drinks.index))
st.write("print(drinks.:red[columns])")
st.write(str(drinks.columns))
st.write("print(drinks.:red[shape])")
st.write(str(drinks.shape))

st.markdown("""
## Example 2:
- the index for South America rows do not change from the Dataset
\n:green[drinks[drinks.:red[continent == "South America"]]
\nprint(drinks[drinks.continent == "South America"])
""")
st.table(drinks[drinks.continent == "South America"])

st.markdown("""
## Example 3:
- use :red[loc] to select row 23 for beer servings
\n:green[drinks.:red[loc[23, 'beer_servings']]
\nprint(drinks.loc[23, 'beer_servings'])
""")
st.write(drinks.loc[23, 'beer_servings'])

st.markdown("""
## Example 4:
- by setting the index as something that is meaningful, we can use it to do data selection from a DataFrame
\n:green[drinks.:red[set_index("country", inplace=True)]]
\nprint(drinks.:red[loc["Brazil", "beer_servings"]])
""")
drinks.set_index("country", inplace=True)
st.write(drinks.loc["Brazil", "beer_servings"])

st.markdown("""
## Example 5:
- the name of the index can be removed
\n:green[drinks.:red[index.name = None]]
\nprint(drinks.head())
""")
drinks.index.name = None
st.table(drinks.head())

st.markdown("""
## Example 6:
- reset the index
\n:green[drinks.:red[index.name = "country"]]
\n:green[drinks.:red[reset_index(inplace=True)]]
\nprint(drinks.head())
""")
drinks.index.name = "country"
drinks.reset_index(inplace=True)
st.table(drinks.head())

st.markdown("""
## Example 7:
- the result of the method describe() is a DataFrame
\nprint(drinks.:red[describe()])
""")
st.table(drinks.describe())
st.write("\nThe 25% of beer_serving:")
st.write("print(drinks.describe():red[.loc[\"25%\", \"beer_servings\"]])")
st.write(drinks.describe().loc["25%", "beer_servings"])
