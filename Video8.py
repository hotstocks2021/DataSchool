# Video 8
# https://www.youtube.com/watch?v=2AFGPdNn4FM&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=8
# Date: 2023-04-19
# Title: How do I filter rows of a pandas DataFrame by column value?
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
pd.set_option('expand_frame_repr',False)
# pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

print("Example 1:")
movies = pd.read_csv("http://bit.ly/imdbratings")
print(movies.head())
print(movies.shape)

print("\nExample 2:")
# filter rows
# this is the long way of filtering
booleans = []
for length in movies.duration:
    if length >= 200:
        booleans.append(True)
    else:
        booleans.append(False)

print(booleans[0:5])
print(len(booleans))
print(movies[booleans].sort_values("duration"))

print("\nExample 3:")
# filter rows
# this is the short way of filtering
booleans = movies.duration >= 200
print(movies[booleans].sort_values("duration"))

print("\nExample 4:")
# filter rows
# this is the shorter way of filtering
print(movies[movies.duration >= 200].sort_values("duration"))

