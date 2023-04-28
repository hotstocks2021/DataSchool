# Video 16
# https://www.youtube.com/watch?v=fCMrO_VzeL8&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=17
# Date: 2023-04-27
# Title:
#       * How do I handle missing values in pandas?
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
ufo = pd.read_csv("http://bit.ly/uforeports")
print(ufo.tail())

print("\nExample 2:")
# Use isnull() method to detect the missing values
print(ufo.isnull().tail())
print("\n")
print(ufo.notnull().tail())

print("\nExample 3:")
# Use isnull() method to find out the total number of missing values
print(ufo.isnull().sum())

print("\nExample 4:")
# Use isnull() method to find the missing values from a Dataset
print(ufo[ufo.City.isnull()])

print("\nExample 5:")
# Use dropna(how="any") method to drop all rows that have missing values
print(ufo.shape)
print(ufo.dropna(how="any").shape)
print(ufo.dropna(how="all").shape)
print(ufo.dropna(subset=["City", "Shape Reported"], how="any").shape)

print("\nExample 6:")
# The value_counts() method of Series is to find the number of uniqueness
print(ufo["Shape Reported"].value_counts(dropna=False))

print("\nExample 7:")
# The fillna() method of Series can be used to replace N/A with something more meaningful
ufo["Shape Reported"].fillna(value="VARIOUS", inplace=True)
print(ufo["Shape Reported"].value_counts(dropna=False))

# print("\nExample 8:")
# # Describe method
# print(movies.duration.describe())