# https://www.youtube.com/watch?v=0uBirYFhizE&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=5
# Date: 2023-04-18
# Title: How do I rename columns in a pandas DataFrame?
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
pd.set_option('expand_frame_repr',False)
# pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

print("\nUFO Report:")
print("Example 1:")
ufo = pd.read_csv("http://bit.ly/uforeports")
print(ufo.head())

print("\nExample 2:")
# display the columns attributes
print(ufo.columns)

print("\nExample 3:")
# rename a column
ufo.rename(columns={"Colors Reported":"Colors_Reported", "Shape Reported":"Shape_Reported"}, inplace=True)
print(ufo.head())
    
print("\nExample 4:")
# replace all column names
ufo_cols = ["city", "colors reports", "shape reported", "state", "time"]
ufo.columns = ufo_cols
print(ufo.head())

print("\nExample 5:")
# rename a column while reading the DataFrame
ufo_cols = ["City", "Colors_Reported", "Shape_Reported", "State", "Time"]
ufo = pd.read_csv("http://bit.ly/uforeports", names=ufo_cols, header=0)
# "header=0" means row zero is a header
print(ufo.head())

print("\nExample 6:")
# replace all columns' whitespace with something
ufo = pd.read_csv("http://bit.ly/uforeports")
print(ufo.head())
ufo.columns = ufo.columns.str.replace(" ", "_")
print(ufo.head())
