import time

from pynkdv.PyNKDV import *
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

time_start = time.time()
# map_data = map_road_network('/Users/patrick/Desktop/hkbu-college/doc/year3/sem1/econ3105/pythonProject3/dataset/NYC_Collisions_clean.csv')
model = PyNKDV(['simplified_Chicago_crimes_from_2001_to_present_clean.gpkg', 'graph_output_Chicago_crimes_from_2001_to_present_clean'], bandwidth=3000, lixel_size=20, num_threads=8)
results = model.compute()
print(time.time() - time_start)
output(results, 'output/Chicago__crime_b3000')
print(time.time() - time_start)