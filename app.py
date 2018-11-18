import pandas as pd
import matplotlib.pyplot as plt
import time
import datetime as datetime
import calendar

abbr_to_num = {name: num for num,
               name in enumerate(calendar.month_abbr) if num}

df = pd.read_csv('data.csv', skipinitialspace=True)
df['Wins'] = df['Wins'].apply(pd.to_numeric, errors='coerce')
df['DD'] = df['DD'].apply(pd.to_numeric, errors='coerce')
df['YYYY'] = df['YYYY'].apply(pd.to_numeric, errors='coerce')

# Get only drafts with at least 1 winner
winsDf = df[df['Wins'] > 0]

# Build date from DD, MMM, YYYY fields
dateWins = []
for row in winsDf.iterrows():
    year = int(row[1]['YYYY'])
    month = int(abbr_to_num[row[1]['MMM']])
    day = int(row[1]['DD'])

    dt = datetime.datetime(year=year,
                           month=month, day=day)

    dateWins.append(dt)

    #print("DT: " + str(dt))

winDates = pd.DataFrame(dateWins)

print("NewDF: " + str(winDates))
# print(pd.Series(winsDf['Wins']))
# print(winsDf['Wins'])

winsSeries = pd.Series(winsDf['Wins'])

# print(winsDf)
# plt.plot(pd.Series(winsDf['Wins']))
# plt.show(block=False)
# input('press here')

# Working plot example
# time = [0, 1, 2, 6]
# position = [0, 100, 200, 300]
plt.plot(winDates, winsDf['Wins'])
plt.xlabel('Dates')
plt.ylabel('Number of Winners')
plt.show()

# print('wins axis: ' + str(s))
# TODO: Get all entries where someone win

# Iterate through every row in dataframe
# for index, row in df.iterrows():
# print('data: ' + str(row))
