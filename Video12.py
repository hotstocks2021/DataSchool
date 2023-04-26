# Video 12
# https://www.youtube.com/watch?v=bofaC0IckHo&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=12
# Date: 2023-04-26
# Title:
#       * How do I use string methods in pandas?
# Note:
#       * https://pandas.pydata.org/pandas-docs/version/0.22/api.html
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
orders = pd.read_table("http://bit.ly/chiporders")
print(orders.head())
print(orders.shape)

print("\nExample 2:")
# Convert string in a Series to upper case
print(orders.item_name.str.upper().head())

print("\nExample 3:")
# Search for string in a Series
print(orders.item_name.str.contains("Chicken").head())

print("\nExample 4:")
# Filter by string in a Series
print(orders[orders.item_name.str.contains("Chicken")].head())

print("\nExample 5:")
# Chain together string methods to remove "[" and "]"
orders.choice_description = orders.choice_description.str.replace("[", "").str.replace("]", "")
print(orders.head())

print("\nExample 6:")
orders = pd.read_table("http://bit.ly/chiporders")
print("Original DataFame:")
print(orders.head())
# Using Regex on string method to remove "[" and "]"
orders.choice_description = orders.choice_description.str.replace("[\[\]]", "")
print("\nModified DataFame:")
print(orders.head())