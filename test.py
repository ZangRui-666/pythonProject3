from pynkdv.PyNKDV import *

setPath(['/Users/patrick/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/ProcessX', '/Users/patrick/opt/anaconda3/envs/pynkdv/share/qgis/python', '/Users/patrick/Library/Application Support/QGIS/QGIS3/profiles/default/python', '/Users/patrick/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins', '/Users/patrick/opt/anaconda3/envs/pynkdv/share/qgis/python/plugins', '/Users/patrick/opt/anaconda3/envs/pynkdv/share/qgis/python/plugins', '/Users/patrick/opt/anaconda3/envs/pynkdv/share/qgis/python', '/Users/patrick', '/Users/patrick/opt/anaconda3/envs/pynkdv/lib/python39.zip', '/Users/patrick/opt/anaconda3/envs/pynkdv/lib/python3.9', '/Users/patrick/opt/anaconda3/envs/pynkdv/lib/python3.9/lib-dynload', '/Users/patrick/opt/anaconda3/envs/pynkdv/lib/python3.9/site-packages', '/Users/patrick/Library/Application Support/QGIS/QGIS3/profiles/default/python'])
map_data = map_road_network('/Users/patrick/Desktop/fypProject/Datasets_Yun/San_Francisco_clean.csv')
model = PyNKDV(map_data, bandwidth=1000, lixel_size=20, num_threads=8)
results = model.compute()
output(results, 'output_test1')
