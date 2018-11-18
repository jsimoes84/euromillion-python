import pandas as pd

# read csv into a dataframe
dataset = pd.read_csv(
    "/Users/admin/learn-python-euromillons/data.csv", skiprows=0)

# Dataset type is dataframe
print(type(dataset))
# print(dataset['Jackpot'].dtypes)

headers = list(dataset.columns.values)

numbersList = list(dataset)

print(numbersList)

s = pd.Series(dataset)

print(s)
