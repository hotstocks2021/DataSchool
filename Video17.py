# Video 17
# https://www.youtube.com/watch?v=OYZNk7Z9s6I&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=17
# Date: 2023-04-29
# Title:
#       * What do I need to know about the pandas index? (Part 1)
# Note: The reason we need index
#       1: identification
#       2: selection
#       3: alignment

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
print("\nIndex:")
print(drinks.index)
print("\nColumns:")
print(drinks.columns)
print("\nShape:")
print(drinks.shape)

print("\nExample 2:")
# the index for South America rows do not change from the Dataset
print(drinks[drinks.continent == "South America"])

print("\nExample 3:")
# use loc to select row 23 for beer servings
print(drinks.loc[23, 'beer_servings'])

print("\nExample 4:")
# by setting the index as seomthing that is meaningful, we can use it to do data selection from a DataFrame
print(drinks.head())
drinks.set_index("country", inplace=True)
print(drinks.loc["Brazil", "beer_servings"])
print(drinks.head())

print("\nExample 5:")
# the name of the index can be removed
drinks.index.name = None
print(drinks.head())

print("\nExample 6:")
# reset the index
drinks.index.name = "country"
drinks.reset_index(inplace=True)
print(drinks.head())

print("\nExample 7:")
# the result of the method describe() is a DataFrame
print(drinks.describe())
print("\nThe 25% of beer_serving:")
print(drinks.describe().loc["25%", "beer_servings"])