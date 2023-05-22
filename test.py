from pynkdv.PyNKDV import *
import pandas as pd
setPath(['/Users/patrick/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/ProcessX', '/Users/patrick/opt/anaconda3/envs/pynkdv/share/qgis/python', '/Users/patrick/Library/Application Support/QGIS/QGIS3/profiles/default/python', '/Users/patrick/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins', '/Users/patrick/opt/anaconda3/envs/pynkdv/share/qgis/python/plugins', '/Users/patrick/opt/anaconda3/envs/pynkdv/share/qgis/python/plugins', '/Users/patrick/opt/anaconda3/envs/pynkdv/share/qgis/python', '/Users/patrick', '/Users/patrick/opt/anaconda3/envs/pynkdv/lib/python39.zip', '/Users/patrick/opt/anaconda3/envs/pynkdv/lib/python3.9', '/Users/patrick/opt/anaconda3/envs/pynkdv/lib/python3.9/lib-dynload', '/Users/patrick/opt/anaconda3/envs/pynkdv/lib/python3.9/site-packages', '/Users/patrick/Library/Application Support/QGIS/QGIS3/profiles/default/python'])

df1 = pd.read_csv('/Users/patrick/Desktop/fypProject/dataset/Gainesville_Crime_Responses.csv',sep=' ', header=None, names=['x','y'])
print(df1.info())
df2 = df1[(df1['x'] != 0.0) & (df1['y'] != 0.0)]
df2.to_csv('/Users/patrick/Desktop/fypProject/dataset/Gainesville_Crime_Responses.csv', sep=' ', header=None, index=False)
map_data = map_road_network('/Users/patrick/Desktop/fypProject/dataset/Gainesville_Crime_Responses.csv')

# model = PyNKDV(map_data, bandwidth=500, lixel_size=20, num_threads=8)
# results = model.compute()
# output(results, 'output_test1')
