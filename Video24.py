# Video 24
# https://www.youtube.com/watch?v=0s_1IsROgDc&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=24
# Date: 2023-05-11
# Title:
#       How do I work with dates and times in pandas?
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
train = pd.read_csv("http://bit.ly/kaggletrain")
print(train.head())
print("\nShape:")
print(train.shape)

print("\nExample 2:")
# add a column to a Dataset using the existing data
train["Sex_male"] = train.Sex.map({"female":0, "male":1})
print(train.head())

print("\nExample 3:")
# using the get_dummies method to add column using existing data
train = pd.read_csv("http://bit.ly/kaggletrain")
train["Sex_male"] = pd.get_dummies(train.Sex, prefix="Sex").iloc[:,1:]
print(train.head())

print("\nExample 4:")
# using the get_dummies method to add columns using existing data
train = pd.read_csv("http://bit.ly/kaggletrain")
train["Embarked_C"] = pd.get_dummies(train.Embarked, prefix="Embarked").iloc[:,:1]
train["Embarked_Q"] = pd.get_dummies(train.Embarked, prefix="Embarked").iloc[:,1:2]
train["Embarked_S"] = pd.get_dummies(train.Embarked, prefix="Embarked").iloc[:,2:]
print(train)

print("\nExample 5:")
# an easier way of doing example 4
train = pd.read_csv("http://bit.ly/kaggletrain")
embarked_dummies = pd.get_dummies(train.Embarked, prefix="Embarked").iloc[:,:]
train = pd.concat([train, embarked_dummies], axis=1)
print(train)

print("\nExample 6:")
# the easiest way of doing example 4
train = pd.read_csv("http://bit.ly/kaggletrain")
train = pd.get_dummies(train, columns=["Sex", "Embarked"])
print(train)