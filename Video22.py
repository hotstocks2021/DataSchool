# Video 22
# https://www.youtube.com/watch?v=ylRlGCtAtiE&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=22
# Date: 2023-05-02
# Title:
#       How do I use pandas with scikit-learn to create Kaggle submissions?
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
# create a new DataFrame by borrowing data from another dataset
feature_cols = ["Pclass", "Parch"]
print(train.head())
X = train.loc[:, feature_cols]
print(X.head())
print()
print(X.shape)
print()
y = train.Survived
print(y.head())
print()
print(y.shape)
print()
print("PassengerId 891:")
print(train[train.PassengerId == 891])
print("Ticket 17758:")
print(train[train.Ticket == 17758])

print("\nExample 3:")
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X, y)

test = pd.read_csv("http://bit.ly/kaggletest")
print(test.head())
test.to_csv("kaggletest.csv")
print()
print("PassengerId 1306:")
print(test[test.PassengerId == 1306])


X_new = test.loc[:, feature_cols]
print(X_new)
print()
print(X_new.shape)

new_pred_class = logreg.predict(X_new)
test.PassengerId
new_pred_class
predict_model = pd.DataFrame({"PassengerId":test.PassengerId, "Survived":new_pred_class}).set_index("PassengerId")
print(predict_model)

print("\nExample 4:")
# export DataFame to a csv file
pd.DataFrame({"PassengerId":test.PassengerId, "Survived":new_pred_class}).set_index("PassengerId").to_csv("sub.csv")

print("\nExample 5:")
# convert a DataFrame to a pickle file
train.to_pickle("train.pkl")
# convert a pickle file to a DataFrame
train2 = pd.read_pickle("train.pkl")
print(train2.head())