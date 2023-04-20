# https://www.youtube.com/watch?v=hSrDViyKWVk&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=4
# Date: 2023-04-17
# Title: Why do some pandas commands end with parentheses (and others don't)?
# Note:
#       Parenthesis (action) - method
#    No parenthesis (attribute) - description of what something is.

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

print("\nIMDB data table:")
print("Example 1:")
movies = pd.read_csv("http://bit.ly/imdbratings")
print(movies.head())

print("\nExample 2:")
# As long as there's one numeric column, it will display numeric statistic value for all columns.
print(movies.describe())

print("\nExample 3:")
# Display the total rows and columns of a DataFrame
print(movies.shape)
    
print("\nExample 4:")
# Display the data type of all columns
print(movies.dtypes)

print("\nExample 5:")
# Display the type of a object
print(type(movies))

print("\nExample 6:")
# Display the description of a column type object
print(movies.describe(include=["object"]))
