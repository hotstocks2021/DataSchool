import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      * How do I use string methods in pandas?
Video 12 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=bofaC0IckHo&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=12
## Pandas Doc String handling: 
https://pandas.pydata.org/pandas-docs/version/0.22/api.html
## Set the display options
:red[pd.set_option('expand_frame_repr', False)]
\n:red[pd.set_option('display.max_colwidth', None)]

## Example 1: 
\n:green[**orders = pd.read_table("http://bit.ly/chiporders")**]
\nprint(drinks.head())
"""
)
orders = pd.read_table("http://bit.ly/chiporders")
st.table(orders.head())
st.write("print(drinks.shape)")
st.write(str(orders.shape))

print(orders.item_name.str.upper().head())

st.markdown("""
## Example 2:
- Convert the string in a Series to upper case
\n:green[orders.item_name:red[.str.upper()].head()]
\nprint(orders.item_name:red[.str.upper()].head())
""")
st.write(orders.item_name.str.upper().head())

st.markdown("""
## Example 3:
- Search for string in a Series
\n:green[orders.item_name:red[.contains("Chicken")].head()]
\nprint(orders.item_name:red[.contains("Chicken")].head())
""")
st.table(orders.item_name.str.contains("Chicken").head())

st.markdown("""
## Example 4:
- Filter by string in a Series
\n:green[orders[orders.item_name:red[.contains("Chicken")].head()]]
\nprint(orders[orders.item_name:red[.contains("Chicken"")].head()]]
""")
st.table(orders[orders.item_name.str.contains("Chicken")].head())

print("\nExample 5:")
# Chain together string methods to remove "[" and "]"
print(orders.choice_description.str.replace("[", "").replace("]", "").head())

st.markdown("""
## Example 5:
- Chain together string methods to remove "[" and "]"
\n:green[orders.choice_description = orders.choice_description:red[.str.replace("[", "").replace("]", "")]]
\nprint(orders.head())
""")
orders.choice_description = orders.choice_description.str.replace("[", "").str.replace("]", "")
st.table(orders.head())

st.markdown("""
## Example 6:
- Using Regex on string method to remove "[" and "]"
\n:green[orders = pd.read_table("http://bit.ly/chiporders")]
\nprint(orders.head())
\n:green[Original DataFrame:]
""")
orders = pd.read_table("http://bit.ly/chiporders")
st.table(orders.head())

st.write("orders.choice_description = orders.choice_description.str.replace(:red[\"[\\\[\\\]]\", \"\"])")
st.write("orders.head()")
st.write(":red[Modified DataFrame:]")
orders.choice_description = orders.choice_description.str.replace("[\[\]]", "")
st.table(orders.head())