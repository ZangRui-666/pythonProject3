# from pynkdv.PyNKDV import *
import pandas as pd


def handle(path, df):
    new_df = pd.read_csv(path, sep=',')
    df2 = new_df.loc[:, ['Longitude', 'Latitude']]
    df3 = df2.dropna(axis=0, how='any')
    df5 = df3.loc[: ,['Longitude', 'Latitude']] # make sure the order
    df6 = pd.concat([df, df5], sort=False)
    print(df6.info())
    return df6


df = pd.read_csv('/Users/patrick/Desktop/Cheshire/2020-04/2020-04-cheshire-street.csv')
df2 = df.loc[:, ['Longitude', 'Latitude']]
df3 = df2.dropna(axis=0, how='any')
df5 = df3.loc[:, ['Longitude', 'Latitude']]  # make sure the order
df = df5
print(df.info())
for i in range(5, 13):
    if i < 10:
        name = '2020-0' + str(i)
    else:
        name = '2020-' + str(i)
    path = '/Users/patrick/Desktop/Cheshire/' + name + '/' + name+'-cheshire-street.csv'
    csv_path = "dataset/" + name + '-cheshire-street.csv'
    print(path)
    print(csv_path)
    df = handle(path, df)

for i in range(1, 13):
    if i < 10:
        name = '2021-0' + str(i)
    else:
        name = '2021-' + str(i)
    path = '/Users/patrick/Desktop/Cheshire/' + name + '/' + name+'-cheshire-street.csv'
    csv_path = "dataset/" + name + '-cheshire-street.csv'
    print(path)
    print(csv_path)
    df = handle(path, df)

for i in range(1, 13):
    if i < 10:
        name = '2022-0' + str(i)
    else:
        name = '2022-' + str(i)
    path = '/Users/patrick/Desktop/Cheshire/' + name + '/' + name+'-cheshire-street.csv'
    csv_path = "dataset/" + name + '-cheshire-street.csv'
    print(path)
    print(csv_path)
    df = handle(path, df)

for i in range(1, 4):
    if i < 10:
        name = '2023-0' + str(i)
    else:
        name = '2023-' + str(i)
    path = '/Users/patrick/Desktop/Cheshire/' + name + '/' + name+'-cheshire-street.csv'
    csv_path = "dataset/" + name + '-cheshire-street.csv'
    print(path)
    print(csv_path)
    df = handle(path, df)

df.to_csv('dataset/' + 'total' + '-cheshire-street.csv', header=None, index=None, sep=' ')