# Video 27
#https://www.youtube.com/watch?v=4R4WsDJ-KVc&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=27
# Date: 2023-05-13
# Title:
#       How do I avoid a SettingWithCopyWarning in pandas?
# Note:
#

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
pd.set_option('display.max_colwidth', None)

print("Example 1:")
# read a dataset of movie reviewers (modifying the default parameter values for read_table)
movies = pd.read_csv('http://bit.ly/imdbratings')
print(movies.head())
print("\nShape:")
print(movies.shape)
print("\nTypes:")
print(movies.dtypes)

print("\nExample 2:")
# find the sum of null content_rating
print(movies.content_rating.isnull().sum())
print()
# print out the rows where content_rating is null
print(movies[movies.content_rating.isnull()])
print()
# print out the rows where content_rating is "NOT RATED"
print(movies[movies.content_rating == "NOT RATED"])

print("\nExample 3:")
# replace all the content_rating equal to "NOT RATED" with NaN
import numpy as np
# below line will produce a SettingWithCopyWarning"
# movies[movies.content_rating == "NOT RATED"].content_rating = np.nan
# the total isnull is still equals to 3:
print(movies.content_rating.isnull().sum())

print("\nExample 4:")
# use loc instead for the above example because loc turns a two operations into a single set operation
movies.loc[movies.content_rating == "NOT RATED", "content_rating"] = np.nan
print(movies.content_rating.isnull().sum())

print("\nExample 5:")
# create a new DataFrame with the top movies of rating with 9 or above
top_movies = movies.loc[movies.star_rating >= 9, : ].copy()
top_movies.loc[0, "duration"] = 150
print(top_movies)
print()
# the original DataFrame of movies stay the same
print(movies.head())

# print("\nExample 6:")
# # change a cell from a DataFrame using loc but still getting the :red[SettingWithCopyWarning]
# top_movies.loc[0, "duration"] = 150
# print(top_movies)

# print("\nExample 7:")
# # print out all the duplicates
# print(users.loc[users.zip_code == "55414", : ])
# print()
# print(users.loc[users.duplicated(keep=False), : ].sort_values(by=["age"]))
#
# print("\nExample 8:")
# # drop the duplicates by occurrence first
# print("\nShape of dataset:")
# print(users.shape)
# print("\nNumber of duplicates:")
# print(users.duplicated().sum())
# print("\nShape of dataset after dropping duplicates:")
# print(users.drop_duplicates(keep="first").shape)
#
# print("\nExample 9:")
# # drop the duplicates by "age" and "zip_code"
# print("\nShape of dataset:")
# print(users.shape)
# print("\nNumber of duplicates by \"age\" and \"zip_code\":")
# print(users.duplicated(subset=["age", "zip_code"]).sum())
# print("\nShape of dataset after dropping duplicates by \"age\" and \"zip_code\":")
# print(users.drop_duplicates(subset=["age", "zip_code"]).shape)
#
