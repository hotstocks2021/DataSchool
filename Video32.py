# Video 32
# https://www.youtube.com/watch?v=iYWKfUOtGaw&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=32
# Date: 2023-05-17
# Title:
#       How do I merge DataFrames in pandas?
# Note:
#       Selecting a Function
#       Joining (Merging) DataFrames
#       What if ...?
#       Four Types of Joins

import os
import sys

try:
    import pandas as pd
except ImportError as e:
    os.system("pip install pandas")
    import pandas as pd

# Set the display options
pd.set_option('expand_frame_repr', False)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', None)

print()
print("Example 1:")
# create a movies DataFrame by importing data from the u.item file
movie_cols = ["movie_id", "title"]
movies = pd.read_table("./data/u.item", sep="|", header=None, names=movie_cols, usecols=[0, 1])
print(movies.head())
print()
print(movies.shape)
print()
print(movies.nunique())

print("\nExample 2:")
# create a rating DataFrame by importing data from the u.item file
rating_cols = ["user_id", "movie_id", "rating", "timestamp"]
ratings = pd.read_table("./data/u.data", sep="\t", header=None, names=rating_cols)
print(ratings.head())
print()
print(ratings.shape)
print()
print(ratings.movie_id.nunique())
print()
print(ratings.loc[ratings.movie_id == 1, :].head())

print("\nExample 3:")
# merging the DataFrame movies and ratings together
print(movies.columns)
print()
print(ratings.columns)
print()
movie_ratings = pd.merge(movies, ratings)
print(movie_ratings.columns)
print()
print(movie_ratings.head())
print()
print(movies.shape)
print()
print(ratings.shape)
print()
print(movie_ratings.shape)

print("\nExample 4:")
# What if the columns you want to join on don't have the same name?
movies.columns = ["m_id", "title"]
print(movies.columns)
print()
print(ratings.columns)
df = pd.merge(movies, ratings, left_on="m_id", right_on="movie_id")
print(df.columns)
print()
print(df.head())

print("\nExample 5:")
# join on one index
print(movies.head())
print()
movies = movies.set_index("m_id")
print(movies.head())
print()
print(movies.shape)
print()
print(ratings.shape)
df = pd.merge(movies, ratings, left_index=True, right_on="movie_id")
print(df.head())
print(df.shape)

print("\nExample 6:")
# join on two indexes
print(movies.head())
print()
ratings = ratings.set_index("movie_id")
print(ratings.head())
print()
df = pd.merge(movies, ratings, left_index=True, right_index=True)
print(df.head())

print("\nExample 7:")
# Example DataFrames A and B
A = pd.DataFrame({'color': ['green', 'yellow', 'red'], 'num':[1, 2, 3]})
print(A)

print()
B = pd.DataFrame({'color': ['green', 'yellow', 'pink'], 'size':['S', 'M', 'L']})
print(B)

print()
# inner join: only include observations found in both A and B
df = pd.merge(A, B, how="inner")
print(df)

print()
# outer join: include observations found in either A and B
df = pd.merge(A, B, how="outer")
print(df)

print()
# left join: include all observations found in A:
df = pd.merge(A, B, how="left")
print(df)

print()
# right join: include all observations found in B:
df = pd.merge(A, B, how="right")
print(df)