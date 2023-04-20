# Video 7
# https://www.youtube.com/watch?v=zY4doF6xSxY&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=7
# Date: 2023-04-19
# Title: How do I sort a pandas DataFrame or a Series?
# Note:
#       DataFrame = rows and columns
#       Series = column

import os
import sys

try:
    import pandas as pd
except ImportError as e:
    os.system("pip install pandas")
    import pandas as pd

# Set the display options
pd.set_option('expand_frame_repr',False)
# pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

print("Example 1:")
movies = pd.read_csv("http://bit.ly/imdbratings")
print(movies.head())
print(movies.shape)

print("\nExample 2:")
# sort by column
print(movies.title.sort_values())
print(movies["title"].sort_values())
print(movies["title"].sort_values(ascending=False))

print("\nExample 3:")
# sort by multiple columns
print(movies.sort_values(["content_rating", "duration"]))
print(movies.sort_values(["content_rating", "duration"], ascending=False))


