import pandas as pd

df = pd.read_csv('/Users/patrick/Desktop/hkbu-college/doc/year3/sem1/econ3105/pythonProject3/dataset/NYC_Collisions_clean.csv', sep=' ', header=None,
                 names=['x', 'y'])
print(df.info())
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
df = df[~((df < (Q1 - 2 * IQR)) | (df > (Q3 + 2 * IQR))).any(axis=1)]
print(df.info())

df.to_csv('/Users/patrick/Desktop/hkbu-college/doc/year3/sem1/econ3105/pythonProject3/dataset/NYC_Collisions_clean.csv', sep=' ', header=None, index=False)
