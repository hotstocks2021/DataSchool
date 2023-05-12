# Video 25
# https://www.youtube.com/watch?v=yCgJGsg0Xa4&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=25
# Date: 2023-05-12
# Title:
#       How do I work with dates and times in pandas?
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
pd.set_option('display.max_colwidth', None)

print("Example 1:")
ufo = pd.read_csv("http://bit.ly/uforeports")
print(ufo.head())
print("\nShape:")
print(ufo.shape)
print("\nTypes:")
print(ufo.dtypes)

print("\nExample 2:")
# convert the time column to pandas time
ufo["Time"] = pd.to_datetime(ufo.Time)
print(ufo.head())
print("\nTypes:")
print(ufo.dtypes)

print("\nExample 3:")
# get the hour out of pandas time series
print(ufo.Time.dt.hour.head())

print("\nExample 4:")
# get the dayofweek out of pandas time series
print(ufo.Time.dt.dayofweek.head())

print("\nExample 5:")
# get the dayofyear out of pandas time series
print(ufo.Time.dt.dayofyear.head())

print("\nExample 6:")
# convert a manually entered date to a timestamp
ts = pd.to_datetime("1/1/1999")
print(ts)

print("\nExample 7:")
# use a timestamp to compare with a dataset
print(ufo.loc[ufo.Time >= ts, :].head())

print("\nExample 8:")
# find the latest in a time series
print(ufo.Time.max())

print("\nExample 9:")
# find the max and min methods to do math in a time series
print(ufo.Time.max() - ufo.Time.min())

print("\nExample 10:")
# find out how many report sightings in a year
ufo["Year"] = ufo.Time.dt.year
print(ufo.head())
year_data = ufo.Year.value_counts().sort_index()
print(year_data)

print("\nExample 11:")
# plot the report sightings in a year
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(year_data.index.values)
ypoints = np.array(year_data.values)

plt.plot(xpoints, ypoints)
plt.show()