# Video 26
#https://www.youtube.com/watch?v=ht5buXUMqkQ&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=26
# Date: 2023-05-12
# Title:
#       How do I find and remove duplicate rows in pandas?
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
# read a dataset of movie reviewers (modifying the default parameter values for read_table)
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols, index_col="user_id")
print(users.head())
print("\nShape:")
print(users.shape)
print("\nTypes:")
print(users.dtypes)

print("\nExample 2:")
# find the duplicated of the Series
print(users.zip_code.duplicated().sum())

print("\nExample 3:")
# find the duplicated of the DataFrame
print(users.duplicated().sum())

print("\nExample 4:")
# print out of the duplicates
print(users.loc[users.zip_code == "55414", : ])
print()
print(users.loc[users.duplicated(), : ])

print("\nExample 5:")
# print out of the duplicates of the first occurrence
print(users.loc[users.zip_code == "55414", : ])
print()
print(users.loc[users.duplicated(keep="first"), : ])

print("\nExample 6:")
# print out of the duplicates of the last occurrence
print(users.loc[users.zip_code == "55414", : ])
print()
print(users.loc[users.duplicated(keep="last"), : ])

print("\nExample 7:")
# print out all the duplicates
print(users.loc[users.zip_code == "55414", : ])
print()
print(users.loc[users.duplicated(keep=False), : ].sort_values(by=["age"]))

print("\nExample 8:")
# drop the duplicates by occurrence first
print("\nShape of dataset:")
print(users.shape)
print("\nNumber of duplicates:")
print(users.duplicated().sum())
print("\nShape of dataset after dropping duplicates:")
print(users.drop_duplicates(keep="first").shape)

print("\nExample 9:")
# drop the duplicates by "age" and "zip_code"
print("\nShape of dataset:")
print(users.shape)
print("\nNumber of duplicates by \"age\" and \"zip_code\":")
print(users.duplicated(subset=["age", "zip_code"]).sum())
print("\nShape of dataset after dropping duplicates by \"age\" and \"zip_code\":")
print(users.drop_duplicates(subset=["age", "zip_code"]).shape)

