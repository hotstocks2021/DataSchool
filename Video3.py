# https://www.youtube.com/watch?v=zxqjeyKP2Tk&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=3
# Date: 2023-04-17
# Title: How do I select a Pandas Series from a DataFrame?
# Note: There are two basic object types in Pandas that hold data
#           1: DataFame: Table of rows and columns. Each of those columns are known as Pandas series.
#                        You can have a series that are not part of the data frame.

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

print("\nUFO sighting report table:")
print("Example 1:")
ufo = pd.read_table("http://bit.ly/uforeports", sep=",")
print(ufo.head())

print("\nUFO sighting report table:")
print("Example 2:")
ufo = pd.read_csv("http://bit.ly/uforeports")
print(ufo.head())
# Get the type of a variable
print(type(ufo))

print("\nExample 3:")
print(ufo["City"].head())
data_type = type(ufo["City"])
print(data_type)

print("\nExample 4:")
# Alternative way of example 3
print(ufo.City.head())
# This method will not work with column name that has white space in between. IE: "Colors Reported".
print(type(ufo.City))

print("\nExample 5:")
# Create a new Series
print(ufo.City.head() + ", " + ufo.State.head())

print("\nExample 6:")
# Create a new Series and assign a name
ufo["Location"] = ufo.City.head() + ", " + ufo.State.head()
print(ufo.head())