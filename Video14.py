# Video 14
# https://www.youtube.com/watch?v=qy0fDqoMJx8&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=14
# Date: 2023-04-27
# Title:
#       * When should I use a "groupby" in pandas?
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
print()
print(drinks.dtypes)
print()
print(drinks.beer_servings.mean())

print("\nExample 2:")
# Use groupby
print(drinks.groupby("continent").beer_servings.mean())

print("\nExample 3:")
# Use groupby with aggregations of math calculation
print(drinks.groupby("continent").beer_servings.agg(["count", "max", "min", "mean"]))

# print("\nExample 4:")
# import matplotlib
# print(drinks.groupby("continent").mean(numeric_only=True).plot(kind="bar"))