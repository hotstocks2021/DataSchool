# Video 28
# https://www.youtube.com/watch?v=yiO43TQ4xvc&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=28
# Date: 2023-05-14
# Title:
#       How do I change display options in pandas?
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
# pd.set_option('display.max_colwidth', None)

print("Example 1:")
# read a dataset of movie reviewers (modifying the default parameter values for read_table)
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
print(drinks)
# print(drinks.head())
print("\nShape:")
print(drinks.shape)
print("\nTypes:")
print(drinks.dtypes)

print("\nExample 2:")
# find the default display.max_rows
print(pd.get_option("display.max_rows"))

print("\nExample 3:")
# set the display.max_rows
pd.set_option("display.max_rows", None)
print(pd.get_option("display.max_rows"))
print(drinks)

print("\nExample 4:")
# reset the display.max_rows
pd.reset_option("display.max_rows")
print(pd.get_option("display.max_rows"))

print("\nExample 5:")
# get the default display.max_columns
print(pd.get_option("display.max_columns"))
# get the default display.max_colwidth
print(pd.get_option("display.max_colwidth"))

print("\nExample 6:")
# set the display.max_columns to None
pd.set_option("display.max_columns", None)
print(pd.get_option("display.max_columns"))
# set the display.max_colwidth to None
pd.set_option("display.max_colwidth", None)
print(pd.get_option("display.max_colwidth"))
print(drinks.head())

print("\nExample 7:")
train = pd.read_csv('http://bit.ly/kaggletrain')
print(train.head())
print()
# get the default display.precision
print(pd.get_option("display.precision"))
# set the display.precision to 2
pd.set_option("display.precision", 2)
print(pd.get_option("display.precision"))
print(train.head())

print("\nExample 8:")
# get and set the display.float_format
drinks["x"] = drinks.wine_servings * 1000
drinks["y"] = drinks.total_litres_of_pure_alcohol * 1000
print(pd.get_option("display.float_format"))
print(drinks.head())
print()
pd.set_option("display.float_format", "{:,}".format)
print(pd.get_option("display.float_format"))
print(drinks.head())
print()
print(drinks.dtypes)
print("Note: display.float_format only applys to float64 datatype and not int64 datatype; therefore, X column didn't work.")

print("\nExample 9:")
# get the descriptions of the Pandas functions without connecting to the Internet
print(pd.describe_option())

print("\nExample 10:")
# search for function inside the describe_option()
print(pd.describe_option("rows"))

print("\nExample 10:")
# reset all the get and set options
print(pd.reset_option("all"))