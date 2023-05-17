# Video 31
# https://www.youtube.com/watch?v=tcRGa2soc-c&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=31
# Date: 2023-05-16
# Title:
#       How do I apply a function to a pandas Series or DataFrame?
# Note:
#       apply
#       map
#       applymap

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
stocks = pd.read_csv('http://bit.ly/smallstocks')
print(stocks)
print("\nShape:")
print(stocks.shape)
print("\nTypes:")
print(stocks.dtypes)
print("\nIndex:")
print(stocks.index)

print("\nExample 2:")
# group the DataFrame by stock symbols then find the mean
print(stocks.groupby("Symbol").Close.mean())

print("\nExample 3:")
# group the DataFrame by stock symbols and date then find the mean
print(stocks.groupby(["Symbol", "Date"]).Close.mean())
ser = stocks.groupby(["Symbol", "Date"]).Close.mean()
print()
# ser is a Series:
print(type(ser))
print()
# ser.index is a MultiIndex
print(ser.index)

print("\nExample 4:")
# multi index Series can be unstacked to a DataFrame
ser = ser.unstack()
print(ser)

print("\nExample 5:")
# example 4 can be done by using the pivot_table() method
df = stocks.pivot_table(values="Close", columns="Date", index="Symbol")
print(df)

print("\nExample 6:")
# create a multi index DataFrame
print(stocks)
print()
stocks.set_index(["Symbol", "Date"], inplace=True)
stocks.sort_index(inplace=True)
print(stocks)
print()
print(stocks.index)

print("\nExample 7:")
# use a tuple on multi index DataFrame
print(stocks.loc[("AAPL", "2016-10-03"), : ])

print("\nExample 8:")
# use a tuple and a list to select multiple indexes on multi index DataFrame
print(stocks.loc[(["AAPL", "MSFT"], "2016-10-03"), : ])

print("\nExample 9:")
# use an index and a tuple to select multiple indexes on multi index DataFrame
print(stocks.loc["AAPL", ("2016-10-03", "2016-10-05"), : ])

print("\nExample 10:")
# use an index and a tuple to select multiple indexes on multi index DataFrame
print(stocks.loc[slice(None), ("2016-10-03", "2016-10-05"), : ])

print("\nExample 11:")
# merge two DataFrames together
stocks = pd.read_csv('http://bit.ly/smallstocks')
print(stocks)

print("\nCreating a new Close DataFrame:")
close = pd.read_csv('http://bit.ly/smallstocks', usecols=[0, 1, 3], index_col=["Symbol", "Date"])
print(close)

print("\nCreating a new Volume DataFrame:")
volume = pd.read_csv('http://bit.ly/smallstocks', usecols=[0, 2, 3], index_col=["Symbol", "Date"])
print(volume)

print("\nMerging the two new DataFrames")
both = pd.merge(close, volume, left_index=True, right_index=True)
print(both)

print("\nExample 12:")
# reset multi indexes DataFrame
both.reset_index(inplace=True)
print(both)