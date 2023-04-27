# Video 13
# https://www.youtube.com/watch?v=V0AWyzVMf54&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=13
# Date: 2023-04-26
# Title:
#       * How do I change the data type of a pandas Series?
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
pd.set_option('expand_frame_repr', False)
# pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

print("Example 1:")
drinks = pd.read_csv("http://bit.ly/drinksbycountry")
print(drinks.head())
print(drinks.dtypes)

print("\nExample 2:")
# Convert integer to float
drinks.beer_servings = drinks.beer_servings.astype(float)
print(drinks.dtypes)

print("\nExample 3:")
# Change the data type as your read a DataFrame
drinks = pd.read_csv("http://bit.ly/drinksbycountry", dtype={'beer_servings':float})
print(drinks.dtypes)

print("\nExample 4:")
# Convert a string object to float
orders = pd.read_table("http://bit.ly/chiporders")
print(orders.head())
print(orders.dtypes)
print("\nChanging a string object to float:")
orders.item_price = orders.item_price.str.replace("$", "").astype(float)
print(orders.dtypes)

print("\nExample 5:")
# Convert Boolean to 0s and 1s
orders.item_name = orders.item_name.str.contains("Chicken").astype(int)
print(orders.item_name.head())
