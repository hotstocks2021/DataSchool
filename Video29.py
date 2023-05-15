# Video 29
# https://www.youtube.com/watch?v=-Ov1N1_FbP8&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=29
# Date: 2023-05-15
# Title:
#       How do I create a pandas DataFrame from another object?
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
# pd.set_option('display.max_colwidth', None)

print("Example 1:")
# manually create a DataFrame with index, column names and values by using dictionary
df = pd.DataFrame({"id": [100, 101, 102], "color": ["red", "blue", "red"]}, columns=["id", "color"], index=["a", "b", "c"])
print(df)

print("\nExample 2:")
# manually create a DataFrame with index, column names and values by using list of list
df2 = pd.DataFrame([[100, "red"], [101, "blue"], [102, "red"]], columns=["id", "color"], index=["a", "b", "c"])
print(df2)

print("\nExample 3:")
# manually create a DataFrame with index, column names and values by using numpy rand() method to generate data
import numpy as np
arr = np.random.rand(4, 2)
df3 = pd.DataFrame(arr, columns=["id", "color"], index=["a", "b", "c", "d"])
print(df3)

print("\nExample 4:")
# manually create a DataFrame with index, column names and values by using numpy arange() and numpy randint()
import numpy as np
arr = np.random.rand(4, 2)
df4 = pd.DataFrame({"student" : np.arange(100, 110, 1), "test" : np.random.randint(60, 101, 10)}).set_index(("student"))
print(df4)

print("\nExample 5:")
# manually create a Series and attach it to a DataFrame
s = pd.Series(["round", "square"], index=["c", "b"], name="shape")
print(s)
print()
print(df)

print()
df5 = pd.concat([df, s], axis=1)
print(df5)




