import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

# pd.set_option('expand_frame_repr', False)
# pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      How do I merge DataFrames in pandas?
Video 32 of Data analysis in Python with Pandas by Data School
\n:red[Note:] 
-      Selecting a Function
-      Joining (Merging) DataFrames
-      What if ...?
-      Four Types of Joins

\n https://www.youtube.com/watch?v=iYWKfUOtGaw&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=32
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
"""
)

st.markdown("""
## :red[Part 1: Selecting a Function]
Taken from Merging DataFrames with pandas (DataCamp course):

- df1.append(df2): stacking vertically
- pd.concat([df1, df2]):
  - stacking many horizontally or vertically
  - simple inner/outer joins on Indexes
- df1.join(df2): inner/outer/left/right joins on Indexes
- pd.merge(df1, df2): many joins on multiple columns
"""
)

st.markdown("""
## :red[Part 2: Joining (Merging) DataFrames]
Using the MovieLens 100k data, let's create two DataFrames:

- :red[movies:] shows information about movies, namely a unique :red[movie_id] and its :red[title]
- :red[ratings]: shows the :red[rating] that a particular :red[user_id] gave to a particular :red[movie_id] at a particular :red[timestamp]
"""
)

st.markdown("""
## Example 1: 
- create a :red[movies] DataFrame by importing data from the :red[u.item] file
"""
)
st.write(":red[movie_cols] = [:red[\"movie_id\", \"title\"]]")
movie_cols = ["movie_id", "title"]
st.write(":red[movies] = pd.read_table:red[(\"./data/u.item\", sep=\"|\", header=None, names=movie_cols, usecols=[0, 1])]")
movies = pd.read_table("./data/u.item", sep="|", header=None, names=movie_cols, usecols=[0, 1])
st.write("movies.:red[head()]")
st.table(movies.head())
st.write("movies.:red[shape]")
st.write(movies.shape)
st.write("movies.:red[nunique()]")
st.table(movies.nunique())

st.markdown("""
## Example 2:
- create a :red[rating] DataFrame by importing data from the :red[u.item] file
"""
)
st.write(":red[rating_cols] = [:red[\"user_id\", \"movie_id\", \"rating\", \"timestamp\"]]")
rating_cols = ["user_id", "movie_id", "rating", "timestamp"]
st.write(":red[ratings] = pd.read_table:red[(\"./data/u.data\", sep=\"\\t\", header=None, names=rating_cols)]")
ratings = pd.read_table("./data/u.data", sep="\t", header=None, names=rating_cols)
st.write("ratings.:red[head()]")
st.table(ratings.head())
st.write("ratings.:red[shape]")
st.write(ratings.shape)
st.write("ratings.:red[nunique()]")
st.table(ratings.nunique())
st.write("ratings.:red[loc[ratings.movie_id == 1 , : ].head()]")
st.table(ratings.loc[ratings.movie_id == 1, :].head())

st.markdown("""
## Example 3:
- :red[merging] the DataFrame :red[movies] and :red[ratings] together
"""
)
st.write("movies.:red[columns]")
st.write(str(movies.columns))
st.write("ratings.:red[columns]")
st.write(str(ratings.columns))
st.write(":red[movie_ratings] = pd.:red[merge(movies, ratings)]")
movie_ratings = pd.merge(movies, ratings)
st.write("movie_ratings.:red[columns]")
st.write(str(movie_ratings.columns))
st.write(":red[Note:] the order of the new DataFrame :red[movie_ratings] goes by the order from the two merged DataFrames")
st.write("movie_ratings.:red[head()]")
st.table(movie_ratings.head())

st.markdown("""
Here's what just happened:

- Pandas noticed that movies and ratings had one column in common, namely :red[movie_id]. This is the "key" on which the DataFrames will be joined.
- The first :red[movie_id]. in movies is 1. Thus, Pandas looked through every row in the ratings DataFrame, searching for a movie_id of 1. Every time it found such a row, it recorded the :red[user_id], :red[rating], and :red[timestamp] listed in that row. In this case, it found 452 matching rows.
- The second :red[movie_id]. in movies is 2. Again, Pandas did a search of ratings and found 131 matching rows.
- This process was repeated for all of the remaining rows in movies.

At the end of the process, the movie_ratings DataFrame is created, which contains the two columns from movies (:red[movie_id]. and :red[title]) and the three other colums from ratings (:red[user_id], rating, and :red[timestamp] ).

- :red[movie_id]. 1 and its :red[title] are listed 452 times, next to the :red[user_id], :red[rating], and :red[timestamp]  for each of the 452 matching ratings.
- :red[movie_id]. 2 and its :red[title] are listed 131 times, next to the :red[user_id], :red[rating], and :red[timestamp]  for each of the 131 matching ratings.
- And so on, for every movie in the dataset.
"""
)

st.write("movies.:red[shape]")
st.write(movies.shape)
st.write("ratings.:red[shape]")
st.write(ratings.shape)
st.write("movie_ratings.:red[shape]")
st.write(movie_ratings.shape)

st.markdown("""
Notice the shapes of the three DataFrames:

- There are 1682 rows in the movies DataFrame.
- There are 100000 rows in the ratings DataFrame.
- The :red[merge] function resulted in a movie_ratings DataFrame with 100000 rows, because every row from ratings matched a row from movies.
- The movie_ratings DataFrame has 5 columns, namely the 2 columns from movies, plus the 4 columns from ratings, minus the 1 column in common.
By default, the :red[merge] function joins the DataFrames using all column names that are in common (:red[movie_id], in this case). The documentation explains how you can override this behavior.
"""
)

st.markdown("""
## :red[Part 3: What if...?]
- What if the columns you want to join on don't have the same name?
"""
)

st.markdown("""
## Example 4:
"""
)
st.write("movies.columns = [:red[\"m_id\"], \"title\"]")
movies.columns = ["m_id", "title"]
st.write("movies.:red[columns]")
st.write(str(movies.columns))
st.write("ratings.:red[columns]")
st.write(str(ratings.columns))
st.write("df = pd.merge(movies, ratings, :red[left_on=\"m_id\"], :red[right_on=\"movie_id\"])")
df = pd.merge(movies, ratings, left_on="m_id", right_on="movie_id")
st.write(":red[Note:] since the above two DataFrames don't have index in common, using :red[left_on=] and :red[right_on=] are required")
st.write("df.:red[columns]")
st.write(str(df.columns))
st.write("df.:red[head()]")
st.write(df.head())

st.markdown("""
## Example 5:
- join on one index
"""
)
st.write("movies.:red[head()]")
st.write(movies.head())
st.write("movies = movies.set_index(\"m_id\")")
movies = movies.set_index("m_id")
st.write("movies.:red[head()]")
st.write(movies.head())

st.write(":red[df] = pd.:red[merge](:red[movies], :red[ratings], :red[left_index=True], :red[right_on=\"movie_id\"])")
df = pd.merge(movies, ratings, left_index=True, right_on="movie_id")
st.write("df.:red[columns]")
st.write(str(df.columns))
st.write("df.:red[head()]")
st.write(df.head())
st.write(":red[Note:] the :red[df] DataFrame :red[index] is using the index on the :red[right] DataFrame")

st.markdown("""
## Example 6:
- join on two indexes
"""
)
st.write("movies.:red[head()]")
st.write(movies.head())
st.write("ratings = ratings.set_index(\"m_id\")")
ratings = ratings.set_index("movie_id")
st.write("ratings.:red[head()]")
st.write(ratings.head())

st.write(":red[df] = pd.:red[merge](:red[movies], :red[ratings], :red[left_index=True], :red[right_index=True])")
df = pd.merge(movies, ratings, left_index=True, right_index=True)
st.write("df.:red[columns]")
st.write(str(df.columns))
st.write("df.:red[head()]")
st.write(df.head())
st.write(":red[Note:] the :red[df] DataFrame :red[index] is using the index on the :red[left] DataFrame. The index doesn't have to be unique.")

st.markdown("""
## :red[Part 4: Four Types of Joins]
There are actually four types of joins supported by the Pandas merge function. Here's how they are described by the documentation:

- :red[inner]: use intersection of keys from both frames, similar to a SQL inner join; preserve the order of the left keys
- :red[outer]: use union of keys from both frames, similar to a SQL full outer join; sort keys lexicographically
- :red[left]: use only keys from left frame, similar to a SQL left outer join; preserve key order
- :red[right]: use only keys from right frame, similar to a SQL right outer join; preserve key order

The default is the "inner join", which was used when creating the movie_ratings DataFrame.

It's easiest to understand the different types by looking at some simple examples from below:
"""
)

st.markdown("""
## Example 7:
- Example DataFrames :red[A] and :red[B]
"""
)
st.write(":red[A] = pd.DataFrame({\"color\": [\"green\", \"yellow\", \"red\"], \"num\":[1, 2, 3]})")
A = pd.DataFrame({'color': ['green', 'yellow', 'red'], 'num':[1, 2, 3]})
st.write("print(:red[A])")
st.table(A)

st.write(":red[B]  = pd.DataFrame({\"color\": [\"green\", \"yellow\", \"pink\"], \"size\":[\"S\", \"M\", \"L\"]})")
B = pd.DataFrame({'color': ['green', 'yellow', 'pink'], 'size':['S', 'M', 'L']})
st.write("print(:red[B])")
st.table(B)

st.write("- :red[**inner join**]: only include observations found in both A and B")
df = pd.merge(A, B, how="inner")
st.write("print(:red[df])")
st.table(df)

st.write("- :red[**outer join**]: include observations found in either A and B")
df = pd.merge(A, B, how="outer")
st.write("print(:red[df])")
st.table(df)

st.write("- :red[**left join**]: include all observations found in A")
df = pd.merge(A, B, how="left")
st.write("print(:red[df])")
st.table(df)

st.write("- :red[**right join**]: include all observations found in B")
df = pd.merge(A, B, how="right")
st.write("print(:red[df])")
st.table(df)