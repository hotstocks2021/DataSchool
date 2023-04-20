# https://www.youtube.com/watch?v=5_QXMwezPJE&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=2
# Date: 2023-04-15

import os
import sys

try:
    import pandas as pd
except ImportError as e:
    os.system("pip install pandas")
    import pandas as pd

# Set the display options
pd.set_option('expand_frame_repr',False)
pd.set_option('display.max_colwidth', None)

print("\nMovie Users Table:")
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
# user_cols = ['user_id', 'age', 'gender', 'occupation']
movieusers = pd.read_table("http://bit.ly/movieusers", sep="|", header=None, names=user_cols, skiprows=None)

#Pandas read table documentation:
#https://pandas.pydata.org/docs/reference/api/pandas.read_table.html

#sep = seperated by |
#header = header of the table
#names = use as the column names
#skiprows = specify the number of rows to skip

print(movieusers.head())





