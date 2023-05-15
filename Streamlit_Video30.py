import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

# pd.set_option('expand_frame_repr', False)
# pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      How do I apply a function to a pandas Series or DataFrame?
Note: 
-   apply
-   map
-   applymap

Video 30 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=P_q0tkYqvSk&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=30
## Pandas Doc :red[String] handling: 
https://pandas.pydata.org/pandas-docs/version/0.22/api.html

## Pandas Doc :red[Datetime Properties] handling: 
https://pandas.pydata.org/pandas-docs/version/0.22/api.html#datetimelike-properties

## Pandas Doc :red[Options and Setting] :
- :red[get_option] 
\n   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_option.html
- :red[set_option]
\n   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.set_option.html
- :red[reset_option]
\n   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.reset_option.html
- :red[describe_option]
\n   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.describe_option.html

## Set the display options
:red[pd.set_option('expand_frame_repr', False)]
\n:red[pd.set_option('display.max_colwidth', None)]

## Example 1: 
\n:drinks[**users = pd.read_table('http://bit.ly/drinksbycountry')**]
\nprint(drinks.:red[head()])
"""
)
train = pd.read_csv('http://bit.ly/kaggletrain')
st.table(train.head())
st.write("print(train.:red[shape])")
st.write(str(train.shape))
st.write("print(train.:red[dtypes])")
st.table(train.dtypes)

st.markdown("""
## Example 2:
- create a new column by using the :red[map()] method with existing data
""")
train["Sex_num"] = train.Sex.map({"female":0, "male": 1})
st.write(":green[train:red[[\"Sex_num\"]] = train.Sex.:red[map({\"female\":0, \"male\": 1})]]")
st.write("train.loc[:red[0:4, [\"Sex\", \"Sex_num\"]]]")
st.table(train.loc[0:4, ["Sex", "Sex_num"]])

st.markdown("""
## Example 3:
- get the length of the Name length by using the apply() method with existing data
""")
train["Name_length"] = train.Name.apply(len)
st.write(":green[train:red[[\"Name_length\"]] = train.Name.:red[apply(len)]]")
st.write("train.loc[:red[0:4, [\"Name\", \"Name_length\"]]]")
st.table(train.loc[0:4, ["Name", "Name_length"]])
st.write(":red[Note]: :red[apply()] is to apply the method that is inside the apply's method")

st.markdown("""
## Example 4:
- get the last name of the people under column Name
""")
def get_element(my_list, position):
    return my_list[position]

st.write(":green[def get_element(my_list, position):]")
st.write("   -  :green[return my_list[position]]")
st.write("print(:red[train.Name.str.split(\",\").apply(get_element, position=0).head()])")
st.table(train.Name.str.split(",").apply(get_element, position=0).head())

st.write(":red[Note]: :red[get_element()] is to return the element :red[ZERO] from a list")

st.markdown("""
## Example 5:
- example 4 can be done by using :red[lambda]
""")

st.write("print(:red[train.Name.str.split(\",\").apply(lambda x: x[0]).head()])")
st.table(train.Name.str.split(",").apply(lambda x: x[0]).head())

st.write(":red[Note]: :red[lambda] is to return the element :red[ZERO] from a list")

st.markdown("""
## Example 6: 
\n:drinks[**users = pd.read_table('http://bit.ly/drinksbycountry')**]
\nprint(drinks.:red[head()])
"""
)
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
st.table(drinks.head())
st.write("print(train.:red[shape])")
st.write(str(drinks.shape))
st.write("print(train.:red[dtypes])")
st.table(drinks.dtypes)

st.write(":green[:red[drinks_subset] = drinks.:red[loc[:, \"beer_servings\":\"wine_servings\"]]]")
drinks_subset = drinks.loc[:, "beer_servings":"wine_servings"]
st.write("print(:red[drinks_subset.head()])")
st.table(drinks_subset.head())
st.write("- apply the :red[max] on the :red[drink_subset] DataFrame for :red[axis=0]")
st.write("print(drinks_subset.:red[apply(max, axis=0)])")
st.table(drinks_subset.apply(max, axis=0))

st.write(":red[Note]: :red[max] is to find the max values for :red[axis=0]")

st.markdown("""
## Example 7: 
"""
)
st.write("- apply the :red[max] on the :red[drink_subset] DataFrame for :red[axis=1]")
st.write("print(drinks_subset.:red[apply(max, axis=1)])")
st.table(drinks_subset.apply(max, axis=1).head())

st.write(":red[Note]: :red[max] is to find the max values for :red[axis=1]")

st.markdown("""
## Example 8: 
"""
)
st.write("- applymap is to overturn everything in a DataFrame")
st.write("print(drinks.loc[:, \"beer_servings\":\"wine_servings\"].:red[applymap(float).head()])")
st.table(drinks.loc[:, "beer_servings":"wine_servings"].applymap(float).head())

st.write(":red[Note]: :red[applymap] will be applied to :red[both axes]")