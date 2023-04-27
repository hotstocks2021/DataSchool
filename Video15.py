# Video 15
# https://www.youtube.com/watch?v=QTVTq8SPzxM&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=15
# Date: 2023-04-27
# Title:
#       * How do I explore a pandas Series?
# Note:
#
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
movies = pd.read_csv("http://bit.ly/imdbratings")
print(movies.head())
print()
print(movies.dtypes)
print()
print(movies.genre.describe())

print("\nExample 2:")
# Use the value_count() method
print(movies.genre.value_counts())

print("\nExample 3:")
# Use the value_count() method and convert it to percentage
print(movies.genre.value_counts(normalize=True))

print("\nExample 4:")
# The result of the method value_counts() is a Series; therefore, you can use the Series methods.
print(type(movies.genre.value_counts(normalize=True)))
print(movies.genre.value_counts().head())

print("\nExample 5:")
# The unique() method of Series
print(movies.genre.unique())

print("\nExample 6:")
# The nunique() method of Series is to find the number of uniqueness
print(movies.genre.nunique())

print("\nExample 7:")
# Crosstab method
print(pd.crosstab(movies.genre, movies.content_rating))

print("\nExample 8:")
# Describe method
print(movies.duration.describe())