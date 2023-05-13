import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      How do I avoid a SettingWithCopyWarning in pandas?
Note: 


Video 27 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=4R4WsDJ-KVc&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=27
## Pandas Doc :red[String] handling: 
https://pandas.pydata.org/pandas-docs/version/0.22/api.html

## Pandas Doc :red[Datetime Properties] handling: 
https://pandas.pydata.org/pandas-docs/version/0.22/api.html#datetimelike-properties

## Set the display options
:red[pd.set_option('expand_frame_repr', False)]
\n:red[pd.set_option('display.max_colwidth', None)]

## Example 1: 
\n:movies[**users = pd.read_table('http://bit.ly/imdbratings')**]
\nprint(movies.:red[head()])
"""
)
movies = pd.read_csv('http://bit.ly/imdbratings')
st.table(movies.head())
st.write("print(ufo.:red[shape])")
st.write(str(movies.shape))
st.write("print(ufo.:red[dtypes])")
st.table(movies.dtypes)

st.markdown("""
## Example 2:
- find the :red[sum] of null content_rating
\nprint(movies.:red[content_rating.isnull().sum()])
""")
st.write(str(movies.content_rating.isnull().sum()))
st.write("- print out the rows where content_rating :red[is null]")
st.write("movies[:red[movies.content_rating.isnull()]]")
st.table(movies[movies.content_rating.isnull()])
st.write("- print out the rows where content_rating is :red[\"NOT RATED\"]")
st.write("movies[:red[movies.content_rating == \"NOT RATED\"]].head()")
st.table(movies[movies.content_rating == "NOT RATED"].head())


st.markdown("""
## Example 3:
- replace all the content_rating equal to "NOT RATED" with NaN
""")
import numpy as np
st.write(":red[Warning]: below line will produce a :red[SettingWithCopyWarning]")
st.write("movies[:red[movies.content_rating == \"NOT RATED\"]].:red[content_rating = np.nan]")
movies[movies.content_rating == "NOT RATED"].content_rating = np.nan
st.markdown(""":red[
\Video27.py:46: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead]
""")
st.write("\n")
st.write(":red[**Note**]: the line from above is a two operations, get and set. Pandas can't guarantee the get operating "
         "is a :red[copy] or :red[view] of the dataset; therefore it throw an :red[warning].")
st.write("- movies[movies.content_rating == \"NOT RATED\"] : This is :red[get]")
st.write("- .content_rating = np.nan : This is :red[set]")


st.markdown("""
## Example 4:
- use loc instead for the above example because loc turns a two operations into a single set operation
""")
st.write("movies.:red[loc][movies.content_rating == \"NOT RATED\", \"content_rating\"] = np.nan")
movies.loc[movies.content_rating == "NOT RATED", "content_rating"] = np.nan
st.write("print(movies.content_rating.isnull().sum())")
st.write(str(movies.content_rating.isnull().sum()))
st.write("- the sum of content_rating.isnull().sum() is not 68")

st.markdown("""
## Example 5:
- create a new DataFrame with the top movies of rating with 9 or above
""")
st.write(":red[**Note**]: be sure to use the method :red[copy()] to prevent from confusion of :red[copy] or :red[view] of the original DataFrame")
st.write("top_movies = movies.loc[movies.star_rating >= 9, : ].:red[copy()]")
top_movies = movies.loc[movies.star_rating >= 9, : ].copy()
st.write("\n")
st.write("- updating row 0 and column duration from 142 to :red[150]")
st.write("top_movies.loc[0 , \"duration\"] = 150")
top_movies.loc[0 , "duration"] = 150
st.table(top_movies)

st.write("- the original DataFrame of movies stays the same")
st.table(movies.loc[movies.star_rating >= 9, : ])

# st.markdown("""
# ## Example 6:
# - print out of the duplicates of the :red[last] occurrence
# """)
# st.write("print(users.loc[:red[users.zip_code == \"55414\"], : ])")
# st.table(users.loc[users.zip_code == "55414", : ])
# st.write("print(users.loc[:red[users.duplicated(keep=\"last\")], : ])")
# st.table(users.loc[users.duplicated(keep="last"), : ])
#
# st.markdown("""
# ## Example 7:
# - print out of the duplicates of the :red[last] occurrence
# """)
# st.write("print(users.loc[:red[users.zip_code == \"55414\"], : ])")
# st.table(users.loc[users.zip_code == "55414", : ])
# st.write("print(users.loc[:red[users.duplicated(keep=False), : ]]:red[.sort_values(by=[\"age\"])])")
# st.table(users.loc[users.duplicated(keep=False), : ].sort_values(by=["age"]))
#
# st.markdown("""
# ## Example 8:
# - drop the duplicates by occurrence first
# """)
# st.write("print(ufo.:red[shape])")
# st.write(str(users.shape))
# st.write("print(users.:red[duplicated().sum()])")
# st.write(str(users.duplicated().sum()))
# st.write("print(users.:red[drop_duplicates(keep=\"first\").shape])")
# st.write(str(users.drop_duplicates(keep="first").shape))
#
# st.markdown("""
# ## Example 9:
# - drop the duplicates by :red["age"] and :red["zip_code"]
# """)
# st.write("print(ufo.:red[shape])")
# st.write(str(users.shape))
# st.write("print(users.:red[duplicated(subset=[\"age\", \"zip_code\"]).sum()])")
# # print(users.duplicated(subset=["age", "zip_code"]).sum())
# st.write(str(users.duplicated(subset=["age", "zip_code"]).sum()))
# st.write("print(users.:red[drop_duplicates(keep=\"first\").shape])")
# st.write(str(users.drop_duplicates(subset=["age", "zip_code"]).shape))
#
