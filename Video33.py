# Video 33
# https://www.youtube.com/watch?v=-NbY7E9hKxk&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=33
# Date: 2023-05-17
# Title:
#       4 new time-saving tricks in pandas
# Note:


# Tanium@Mar@2023

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

print(pd.__version__)
print()

print("1. Create a datetime column from a DataFrame")

print("\nExample 1:")
# create an example DataFrame
df = pd.DataFrame([[12, 25, 2017, 10], [1, 15, 2018, 11]],  columns=['month', 'day', 'year', 'hour'])
print(df.head())
print()
print(df.shape)

print("\nExample 2:")
# create a datetime column from the entire DataFrame
df = pd.to_datetime(df)
print(df.head())

print("\nExample 3:")
# create a datetime column from a subset of columns
df = pd.DataFrame([[12, 25, 2017, 10], [1, 15, 2018, 11]],  columns=['month', 'day', 'year', 'hour'])
df = pd.to_datetime(df[['month', 'day', 'year']])
print(df.head())

print("\nExample 4:")
# overwrite the index
df = pd.DataFrame([[12, 25, 2017, 10], [1, 15, 2018, 11]],  columns=['month', 'day', 'year', 'hour'])
df.index = pd.to_datetime(df[['month', 'day', 'year']])
print(df.head())

print("\n2. Create a category column during file reading")

print("\nExample 5:")
# read the drinks dataset into a DataFrame and convert the 'continent' datatype to category
drinks = pd.read_csv('http://bit.ly/drinksbycountry', dtype={'continent':'category'})
print(drinks.head())
print()
print(drinks.dtypes)

print("\n3. Convert the data type of multiple columns at once")

print("\nExample 6:")
# read the drinks dataset into a DataFrame
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
print(drinks.dtypes)

print()
# convert the datatype from int to float
drinks = drinks.astype({'beer_servings':'float', 'spirit_servings':'float'})
print(drinks.dtypes)

print("\n4. Apply multiple aggregations on a Series or DataFrame")

print("\nExample 7:")
# example of a single aggregation function after a groupby
print(drinks.groupby('continent').beer_servings.mean())

print("\nExample 8:")
# multiple aggregation functions can be applied simultaneously
print(drinks.groupby('continent').beer_servings.agg(['mean', 'min', 'max']))

print("\nExample 9:")
# apply the same aggregations to a Series
print(drinks.beer_servings.agg(['mean', 'min', 'max']))

print("\nExample 10:")
# apply the same aggregations to a DataFrame
print(drinks.agg(['mean', 'min', 'max']))

print("\nExample 11:")
# DataFrame describe method provides similar functionality but is less flexible
print(drinks.describe())
