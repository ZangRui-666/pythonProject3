from pynkdv.PyNKDV import *
import pandas as pd
import numpy as np
import scipy.stats as stats


setPath(['/Users/patrick/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/ProcessX',
         '/Users/patrick/opt/anaconda3/envs/pynkdv/share/qgis/python',
         '/Users/patrick/Library/Application Support/QGIS/QGIS3/profiles/default/python',
         '/Users/patrick/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins',
         '/Users/patrick/opt/anaconda3/envs/pynkdv/share/qgis/python/plugins',
         '/Users/patrick/opt/anaconda3/envs/pynkdv/share/qgis/python/plugins',
         '/Users/patrick/opt/anaconda3/envs/pynkdv/share/qgis/python', '/Users/patrick',
         '/Users/patrick/opt/anaconda3/envs/pynkdv/lib/python39.zip',
         '/Users/patrick/opt/anaconda3/envs/pynkdv/lib/python3.9',
         '/Users/patrick/opt/anaconda3/envs/pynkdv/lib/python3.9/lib-dynload',
         '/Users/patrick/opt/anaconda3/envs/pynkdv/lib/python3.9/site-packages',
         '/Users/patrick/Library/Application Support/QGIS/QGIS3/profiles/default/python'])

df = pd.read_csv('/Users/patrick/Desktop/fypProject/dataset/Gainesville_Crime_Responses.csv', sep=' ', header=None,
                 names=['x', 'y'])
print(df.info())
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
df = df[~((df < (Q1 - 2 * IQR)) | (df > (Q3 + 2 * IQR))).any(axis=1)]
print(df.info())

# df = pd.read_csv('/Users/patrick/Desktop/fypProject/Datasets_Yun/San_Francisco_clean.csv', sep=' ', header=None,
#                  names=['x', 'y'])
# df = df[(np.abs(stats.zscore(df)) < 4).all(axis=1)]
# print(df.info())
#
df.to_csv('/Users/patrick/Desktop/fypProject/dataset/Gainesville_Crime_Responses.csv', sep=' ', header=None, index=False)
map_data = map_road_network('/Users/patrick/Desktop/fypProject/dataset/Gainesville_Crime_Responses.csv')

# model = PyNKDV(map_data, bandwidth=500, lixel_size=20, num_threads=8)
# results = model.compute()
# output(results, 'output_test1')
