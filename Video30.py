# Video 30
# https://www.youtube.com/watch?v=P_q0tkYqvSk&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=30
# Date: 2023-05-15
# Title:
#       How do I apply a function to a pandas Series or DataFrame?
# Note:
#       apply
#       map
#       applymap

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
# pd.set_option('display.max_colwidth', None)

print("Example 1:")
# read a dataset of movie reviewers (modifying the default parameter values for read_table)
train = pd.read_csv('http://bit.ly/kaggletrain')
print(train.head())
print("\nShape:")
print(train.shape)
print("\nTypes:")
print(train.dtypes)

print("\nExample 2:")
# create a new column by using the map() method with existing data
train["Sex_num"] = train.Sex.map({"female":0, "male": 1})
print(train.loc[0:4, ["Sex", "Sex_num"]])

print("\nExample 3:")
# get the length of the Name length by using the apply() method with existing data
train["Name_length"] = train.Name.apply(len)
print(train.loc[0:4, ["Name", "Name_length"]])

print("\nExample 4:")
# get the last name of the people under column Name
def get_element(my_list, position):
    return my_list[position]

print(train.Name.str.split(",").apply(get_element, position=0).head())

print("\nExample 5:")
# example 4 can be done by using lambda
print(train.Name.str.split(",").apply(lambda x: x[0]).head())

print("\nExample 6:")
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
print(drinks.head())
print("\nShape:")
print(drinks.shape)
print("\nTypes:")
print(drinks.dtypes)
print()
drinks_subset = drinks.loc[:, "beer_servings":"wine_servings"]
print(drinks_subset.head())
print()
# apply the max on the drink_subset DataFrame for axis=0
print(drinks_subset.apply(max, axis=0))

print("\nExample 7:")
# apply the max on the drink_subset DataFrame for axis=1
print(drinks_subset.apply(max, axis=1).head())

print("\nExample 8:")
# applymap is to overturn everything in a DataFrame
print(drinks.loc[:, "beer_servings":"wine_servings"].applymap(float).head())

# print("\nExample 9:")



