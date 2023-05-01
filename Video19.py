# Video 19
# https://www.youtube.com/watch?v=xvpNA7bC8cs&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=19
# Date: 2023-05-01
# Title:
#       * How do I select multiple rows and columns from a pandas DataFrame?
# Note:
#       loc is for selecting rows and filtering columns by LABEL (inclusive on both side)
#       iloc is for selecting rows and filtering columns by INTEGER position (exclusive on the right side)
#       ix is for selecting rows and filtering columns by LABEL and POSITION. Note: ix has been deprecated

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
# use loc to display row 0 and all columns; the result will be a pandas Series
print(ufo.loc[0, :])

print("\nExample 3:")
# use loc to display row 0, 1, and 2 and all columns; the result will be a pandas DataFrame
print(ufo.loc[[0, 1, 2], :])
print()
print(ufo.loc[0:2, :])

print("\nExample 4:")
# use loc to display all rows and column "City"; the result will be a pandas Series
print(ufo.loc[:,"City"].head())

print("\nExample 5:")
# use loc to display all rows and column "City" and "State"; the result will be a pandas DataFrame
print(ufo.loc[:,["City", "State"]].head())
print()
print(ufo.loc[:,"City":"State"].head())

print("\nExample 6:")
# use loc to display all the city = Oakland rows and all columns; the result will be a pandas DataFrame
print(ufo.loc[ufo.City == "Oakland", : ].head())

print("\nExample 7:")
# use iloc to display all rows and columns in position 0 and 3; the result will be a pandas DataFrame
print(ufo.iloc[:, [0, 3]].head())
print()
print(ufo.iloc[:, 0:4].head())

