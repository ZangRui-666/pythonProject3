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


model = PyNKDV(['simplified_Seattle_crash_Collisions.gpkg', 'graph_output_Seattle_crash_Collisions'])
results = model.compute()
print('last')
output(results, 'test6_output')