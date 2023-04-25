# Video 9
# https://www.youtube.com/watch?v=YPItfQ87qjM&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=9
# Date: 2023-04-25
# Title: How do I apply multiple filter criteria to a pandas DataFrame?
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
print(movies.shape)

print("\nExample 2:")
# filter one column of the DataFrame
print(movies[movies.duration >= 200].sort_values("duration"))

print("\nExample 3:")
# filter two columns of the DataFrame
print(movies[(movies.duration >= 200) & (movies.genre == "Drama")].sort_values("duration", ascending=False))

print("\nExample 4:")
# filter the columns of the DataFrame by using "isin"
print(movies[(movies.duration >= 200) & (movies.genre.isin(["Drama", "Crime", "Action"]))].sort_values("duration", ascending=False))
