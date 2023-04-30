import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      * What do I need to know about the pandas index? (Part 2)
- Note: The reason we need index:
-       1: identification
-       2: selection
-       3: alignment
Video 18 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=15q-is8P_H4&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=18
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
st.write("print(drinks.:red[continent].head())")
st.table(drinks.continent.head())

st.markdown("""
## Example 2:
- set the Country column as the index of the dataset
\n:green[drinks.:red[set_index("country", inplace=True)]]
\nprint(drinks.head())
""")
drinks.set_index("country", inplace=True)
st.write("display the dataset head() and we will see the country as the index instead of numbers like :red[example 1]")
st.write("print(drinks.:red[continent].head())")
st.table(drinks.continent.head())

st.markdown("""
## Example 3:
- the result of drinks.continent.value_counts() is a Series
\n:green[drinks.:red[continent.value_counts()]]
\nprint(drinks.continent.value_counts())
""")
st.write(drinks.continent.value_counts())
st.write("Series has index and values as attribute:")
st.write("drinks.continent.value_counts().:red[index]")
st.write(str(drinks.continent.value_counts().index))
st.write("drinks.continent.value_counts().:red[values]")
st.write(str(drinks.continent.value_counts().values))
st.write("from the Series, find the index Africa")
st.write(drinks.continent.value_counts()["Africa"])

st.markdown("""
## Example 4:
- sort by Series
\n:green[drinks.continent.value_counts().:red[sort_values()]]
\nprint(drinks.continent.value_counts().sort_values())
""")
st.table(drinks.continent.value_counts().sort_values())
st.write("sort by Series index")
st.write("print(drinks.continent.value_counts().:red[sort_index()])")
st.table(drinks.continent.value_counts().sort_index())

st.markdown("""
## Example 5:
- use index for alignment
""")
people = pd.Series([3000000, 85000], index=["Albania", "Andorra"], name="population")
st.write(":green[people = pd.Series([3000000, 85000], index=[\"Albania\", \"Andorra\"], name=\"population\")]")
st.write("print(people.head())")
st.table(people.head())
st.write("print(drinks.beer_servings.head())")
st.table(drinks.beer_servings.head())
st.write(":red[use the drinks.beer_servings Series to do calculation on the people Series]")
st.write("print((:red[drinks.beer_servings * people]).head())")
st.table((drinks.beer_servings * people).head())

st.markdown("""
## Example 6:
- add a Series to an existing DataFrame
\n:green[drinks = :red[pd.concat([drinks, people], axis=1)]]
\nprint(drinks.head())
""")
drinks = pd.concat([drinks, people], axis=1)
st.table(drinks.head())
