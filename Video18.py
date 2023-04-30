# Video 18
# https://www.youtube.com/watch?v=15q-is8P_H4&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=18
# Date: 2023-04-30
# Title:
#       * What do I need to know about the pandas index? (Part 2)
# Note: The reason we need index
#       1: identification
#       2: selection
#       3: alignment

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
print("\nIndex:")
print(drinks.index)
print("\nColumns:")
print(drinks.columns)
print("\nShape:")
print(drinks.shape)
print("\nContinent:")
print(drinks.continent.head())


print("\nExample 2:")
# set the Country as the index for the dataset
drinks.set_index("country", inplace=True)
print(drinks.head())
# display the dataset head() and we will see the country as the index instead of numbers like example 1
print()
print(drinks.continent.head())

print("\nExample 3:")
# the result of drinks.continent.value_counts() is a Series
print(drinks.continent.value_counts())
print(drinks.continent.value_counts().index)
print(drinks.continent.value_counts().values)
print("from the Series, find the index Africa")
print(drinks.continent.value_counts()["Africa"])


print("\nExample 4:")
# sort by Series
print(drinks.continent.value_counts().sort_values())
# sort by Series index
print()
print(drinks.continent.value_counts().sort_index())

print("\nExample 5:")
# use index for alignment
people = pd.Series([3000000, 85000], index=["Albania", "Andorra"], name="population")
print(people.head())
print()
print(drinks.beer_servings.head())
print()
print((drinks.beer_servings * people).head())

print("\nExample 6:")
# add a Series to an existing DataFrame
drinks = pd.concat([drinks, people], axis=1)
print(drinks.head())