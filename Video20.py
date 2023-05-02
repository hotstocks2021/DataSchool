# Video 20
# https://www.youtube.com/watch?v=XaCSdr7pPmY&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=20
# Date: 2023-05-02
# Title:
#       When should I use the "inplace" parameter in pandas?
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

print("\nExample 2:")
# use the drop() method to drop one of the column from a dataset
ufo.drop("City", axis=1, inplace=True)
print(ufo.head())

print("\nExample 3:")
# use assignment statement is the same as inplace=True
ufo = ufo.set_index("Time")
print(ufo.head())
