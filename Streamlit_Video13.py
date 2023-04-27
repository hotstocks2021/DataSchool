import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      * How do I change the data type of a pandas Series?
Video 13 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=V0AWyzVMf54&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=13
## Pandas Doc String handling: 
https://pandas.pydata.org/pandas-docs/version/0.22/api.html
## Set the display options
:red[pd.set_option('expand_frame_repr', False)]
\n:red[pd.set_option('display.max_colwidth', None)]

## Example 1: 
\n:green[**drinks = pd.read_csv("http://bit.ly/drinksbycountry")**]
\nprint(drinks.head())
"""
)
drinks = pd.read_csv("http://bit.ly/drinksbycountry")
st.table(drinks.head())
st.write("print(drinks.dtypes)")
st.table(drinks.dtypes)


st.markdown("""
## Example 2:
- Convert integer to float
\n:green[drinks.beer_servings = drinks.beer_servings:red[.astype(float)]]
\nst.table(drinks.dtypes)
""")
drinks.beer_servings = drinks.beer_servings.astype(float)
st.table(drinks.dtypes)

st.markdown("""
## Example 3:
- Change the data type as you read a DataFrame
\n:green[drinks = pd.read_csv("http://bit.ly/drinksbycountry", :red[dtype={'beer_servings':float}])]
\nst.table(drinks.dtypes)
""")
drinks = pd.read_csv("http://bit.ly/drinksbycountry", dtype={'beer_servings': float})
st.table(drinks.dtypes)

st.markdown("""
## Example 4:
- Convert a string object to float
\n:green[orders = pd.read_table("http://bit.ly/chiporders")]
\nprint(orders.head())
""")
orders = pd.read_table("http://bit.ly/chiporders")
st.table(orders.head())
st.write("print(orders.dtypes)")
st.table(orders.dtypes)
st.write("\nChanging a string object to float:")
st.write("\norders.item_price = orders.item_price:red[.str.replace(\"$\", \"\").astype(float)]")
orders.item_price = orders.item_price.str.replace("$", "").astype(float)
st.write("print(orders.dtypes)")
st.table(orders.dtypes)

st.markdown("""
## Example 5:
- Convert Boolean to 0s and 1s
\n:green[orders.item_name = orders.item_name:red[.str.contains("Chicken").astype(int)]]
\nprint(orders.item_name.head())
""")
orders.item_name = orders.item_name.str.contains("Chicken").astype(int)
st.table(orders.item_name.head())
