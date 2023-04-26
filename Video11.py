# Video 11
# https://www.youtube.com/watch?v=PtO3t6ynH-8&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=11
# Date: 2023-04-26
# Title:
#       * How do I use the "axis" parameter in pandas?
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
drinks = pd.read_csv("http://bit.ly/drinksbycountry")
print(drinks.head())
print(drinks.shape)

print("\nExample 2:")
# drop one of the columns using axis=1
print(drinks.drop("continent", axis=1).head())

print("\nExample 3:")
# drop one of the rows using axis=0
print(drinks.drop(2, axis=0).head())

print("\nExample 4:")
# get the mean of the columns
# axis=0 is set by default
# numeric_only=True will silence a deprecated warning
print(drinks.mean(numeric_only=True, axis=0))

print("\nExample 5:")
# get the mean of the rows
# numeric_only=True will silence a deprecated warning
print(drinks.mean(numeric_only=True, axis=1).head())