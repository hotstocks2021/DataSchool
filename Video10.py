# Video 10
# https://www.youtube.com/watch?v=B-r9VuK80dk&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=10
# Date: 2023-04-25
# Title:
#       * Read only specific columns from a DataFrame
#       * Read only specific rows from a DataFrame
#       * Iterate DataFrame
#       * Select only numeric columns from a DataFrame
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
print(ufo.head())
print(ufo.shape)

print("\nExample 2:")
# read only the "City" and "State" from a DataFrame
ufo = pd.read_csv("http://bit.ly/uforeports", usecols=["City", "State"])
# Reference by indexes
ufo = pd.read_csv("http://bit.ly/uforeports", usecols=[0, 3])
print(ufo.head())
print(ufo.shape)

print("\nExample 3:")
# take only the first 3 rows of a DataFrame
ufo = pd.read_csv("http://bit.ly/uforeports", nrows=3)
print(ufo.head())
print(ufo.shape)

print("\nExample 4:")
# how to iterate a DataFrame
# Note: "index" must be included inside the FOR loop; print of it is optional
for index, row in ufo.iterrows():
    print(row.City, row.State)

print("\nExample 5:")
# select only numeric columns from a DataFrame
drinks = pd.read_csv("http://bit.ly/drinksbycountry")
print(drinks.dtypes)

print("\nselect only numeric columns from a DataFrame")
import numpy as np
print(drinks.select_dtypes(include=[np.number]).dtypes)
