import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

# pd.set_option('expand_frame_repr', False)
# pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      How do I change display options in pandas?
Note: 


Video 28 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=yiO43TQ4xvc&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=28
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
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
st.table(drinks.head())
st.write("print(ufo.:red[shape])")
st.write(str(drinks.shape))
st.write("print(ufo.:red[dtypes])")
st.table(drinks.dtypes)

st.markdown("""
## Example 2:
- find the default display.max_rows
\nprint(pd.:red[get_option("display.max_rows")])
""")
st.write(str(pd.get_option("display.max_rows")))

st.markdown("""
## Example 3:
- set the display.max_rows
""")
st.write("pd.:red[set_option(\"display.max_rows\", None)]")
pd.set_option("display.max_rows", None)
st.write("print(pd.get_option(\"display.max_rows\"))")
st.write(str(pd.get_option("display.max_rows")))

st.markdown("""
## Example 4:
- reset the display.max_rows
""")
st.write("pd.:red[reset_option(\"display.max_rows\")]")
pd.reset_option("display.max_rows")
st.write("print(pd.get_option(\"display.max_rows\"))")
st.write(str(pd.get_option("display.max_rows")))

st.markdown("""
## Example 5:
""")
st.write("- get the default display.max_columns")
st.write("pd.:red[get_option(\"display.max_columns\")]")
st.write(str(pd.get_option("display.max_columns")))

st.write("- get the default display.max_colwidth")
st.write("pd.:red[get_option(\"display.max_colwidth\")]")
st.write(str(pd.get_option("display.max_colwidth")))

st.markdown("""
## Example 6:
""")
st.write("- set the default display.max_columns")
pd.set_option("display.max_columns", None)
st.write("pd.:red[set_option(\"display.max_columns\"), None]")
st.write(str(pd.get_option("display.max_columns")))

st.write("- set the default display.max_colwidth")
pd.set_option("display.max_colwidth", None)
st.write("pd.:red[set_option(\"display.max_colwidth\", None)]")
st.write(str(pd.get_option("display.max_colwidth")))

st.markdown("""
## Example 7:
\ntrain = pd.read_csv('http://bit.ly/kaggletrain')
""")
train = pd.read_csv('http://bit.ly/kaggletrain')
st.write("print(train.head())")
st.table(train.head())

st.write("- get the default display.precision")
st.write("pd.:red[get_option(\"display.precision\")]")
st.write(str(pd.get_option("display.precision")))

st.write("- set the default display.precision")
pd.set_option("display.precision", 2)
st.write("pd.:red[set_option(\"display.precision\", 2)]")
st.write(str(pd.get_option("display.precision")))

st.write("print(train.head())")
st.table(train.head())

st.write(":red[Note]: not all of the set and get options work in Streamlit")

st.markdown("""
## Example 8:
- :red[get] the display.float_format
""")
st.write(":green[drinks[\"wine_servings\"] = drinks.wine_servings * 100000]")
drinks["wine_servings"] = drinks.wine_servings * 100000
st.write(":green[drinks[\"total_litres_of_pure_alcohol\"] = drinks.total_litres_of_pure_alcohol * 100000]")
drinks["total_litres_of_pure_alcohol"] = drinks.total_litres_of_pure_alcohol * 100000
st.write(str(pd.get_option("display.float_format")))
st.write("drinks.:red[head()]")
st.table(drinks.head())

st.write("- :red[set] the display.float_format")
st.write(":green[pd.set_option(:red[\"display.float_format\", \"{ : , }\".format])]")
pd.set_option("display.float_format", "{:,}".format)
st.write("drinks.:red[head()]")
st.table(drinks.head())
st.table(drinks.dtypes)

st.write(":red[Note]: display.float_format only applys to float64 datatype and not int64 datatype; therefore, :red[wine_servings] column didn't work.")

st.markdown("""
## Example 9:
- get the descriptions of the Pandas functions without connecting to the Internet
""")
st.write("pd.:red[describe_option()]")

st.markdown("""
## Example 10:
- search for function inside the describe_option()
""")
st.write("pd.:red[describe_option(rows)]")

st.markdown("""
## Example 11:
- reset all the get and set options
""")
st.write("pd.:red[reset_option(\"all\")]")
st.write(":red[Note]: you will get a warning due to deprecated options.")
