import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

# pd.set_option('expand_frame_repr', False)
# pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      How do I create a pandas DataFrame from another object?
Note: 


Video 29 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=-Ov1N1_FbP8&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=29
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
- manually create a DataFrame with index, column names and values by using dictionary
"""
)
df = pd.DataFrame({"id": [100, 101, 102], "color": ["red", "blue", "red"]}, columns=["id", "color"], index=["a", "b", "c"])
st.write(":green[df = pd.DataFrame(:red[{\"id\": [100, 101, 102], \"color\": [\"red\", \"blue\", \"red\"]}, columns=[\"id\", \"color\"], index=[\"a\", \"b\", \"c\"]])]")
st.write("print(:red[df])")
st.table(df)

st.markdown("""
## Example 2: 
- manually create a DataFrame with index, column names and values by using list of list
"""
)
df2 = pd.DataFrame([[100, "red"], [101, "blue"], [102, "red"]], columns=["id", "color"], index=["a", "b", "c"])
st.write(":green[df2 = pd.DataFrame(:red[[[100, \"red\"], [101, \"blue\"], [102, \"red\"]], columns=[\"id\", \"color\"], index=[\"a\", \"b\", \"c\"]])]")
st.write("print(:red[df2])")
st.table(df2)

st.markdown("""
## Example 3: 
- manually create a DataFrame with index, column names and values by using numpy rand() method to generate data
"""
)
import numpy as np
st.write(":green[import :red[numpy] as :red[np]]")
arr = np.random.rand(4, 2)
st.write(":green[:red[arr] = np.random.:red[rand(4, 2)]]")
df3 = pd.DataFrame(arr, columns=["id", "color"], index=["a", "b", "c", "d"])
st.write(":green[df3 = pd.DataFrame(:red[arr, columns=[\"id\", \"color\"], index=[\"a\", \"b\", \"c\", \"d\"]])]")
st.write("print(:red[df3])")
st.table(df3)

st.markdown("""
## Example 4: 
- manually create a DataFrame with index, column names and values by using numpy arange() and numpy randint()
"""
)
import numpy as np
st.write(":green[import :red[numpy] as :red[np]]")
arr = np.random.rand(4, 2)
st.write(":green[:red[arr] = np.random.:red[rand(4, 2)]]")
df4 = pd.DataFrame({"student" : np.arange(100, 110, 1), "test" : np.random.randint(60, 101, 10)}).set_index(("student"))
st.write(":green[df4 = pd.DataFrame(:red[{\"student\" : np.arange(100, 110, 1), \"test\" : np.random.randint(60, 101, 10)}).set_index((\"student\")])]")
st.write(":red[**Note:**]")
st.write("""
- :red[arange()] = array range;
   -  1st number = starting
   -  2nd number = ending
   -  3rd number step
""")
st.write("""
- :red[randint()] = random integer;
   -  1st number = minimum of 60
   -  2nd number = maximum of 100 because is exclusive
   -  3rd number = generate x number of the above
""")
st.write("""
- :red[set_index()] = set a column to be the index
""")
st.write("print(:red[df4])")
st.table(df4)

st.markdown("""
## Example 5: 
- manually create a Series and attach it to a DataFrame
"""
)
s = pd.Series(["round", "square"], index=["c", "b"], name="shape")
st.write(":green[s = pd.Series(:red[[\"round\", \"square\"], index=[\"c\", \"b\"], name=\"shape\"])]")
st.write("""
- :red[name=shape]
   -  the column name for the Series
""")
st.write("print(:red[s])")
st.table(s)
st.write("print(:red[df])")
st.table(df)
df5 = pd.concat([df, s], axis=1)
st.write(":green[df5 = pd.:red[concat([df, s], axis=1)]]")
st.write("""
- :red[concat] 
   -  :red[concatenate] DataFrame :red[df] with Series :red[s] together
   -  :red[axis=1] = match by index
""")
st.write("print(:red[df5])")
st.table(df5)
st.write(":red[**Note:**] index :red[a] doesn't have value from Series :red[s]; therefor, it displays :red[<NA>]")
