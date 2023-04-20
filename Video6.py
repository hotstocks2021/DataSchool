# Video 6
# https://www.youtube.com/watch?v=gnUKkS964WQ&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=6
# Date: 2023-04-19
# Title: How do I remove columns from a pandas DataFrame?
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
ufo = pd.read_csv("http://bit.ly/uforeports")
print(ufo.head())
print(ufo.shape)

print("\nExample 2:")
# remove a column, a string is needed
# axis=0 is for the row access
# axis=1 is for the column access
ufo.drop("Colors Reported", axis=1, inplace=True)
print(ufo.head())

print("\nExample 3:")
# drop multiple columns, need a list of string to that
ufo = pd.read_csv("http://bit.ly/uforeports")
ufo.drop(["Colors Reported", "Shape Reported"], axis=1, inplace=True)
print(ufo.head())

print("\nExample 4:")
# drop rows from a DataFrame, need to use the index (label)
ufo = pd.read_csv("http://bit.ly/uforeports")
ufo.drop([0, 1], axis=0, inplace=True)
print(ufo.head())
