# Video 23
# https://www.youtube.com/watch?v=oH3wYKvwpJ8&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=23
# Date: 2023-05-11
# Title:
#       More of your pandas questions answered!
# Note:
#       How to use the sample method

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

print("\nExample 2:")
# get three sample rows
print(ufo.sample(n=3))

print("\nExample 3:")
# get three same sample rows
print(ufo.sample(n=3, random_state=50))

print("\nExample 4:")
# get a faction of rows
print(ufo.sample(frac=0.0001, random_state=50))

print("\nExample 5:")
# get the remaining rows of the faction from the above example
train = ufo.sample(frac=0.0001, random_state=50)
print(ufo.shape)
print(train.shape)
test = ufo.loc[~ufo.index.isin(train.index), : ]
print(test.shape)