from pynkdv.PyNKDV import *
import pandas as pd


def handle(path, csv_path):
    df = pd.read_csv(path, sep=',')
    df2 = df.loc[:, ['Longitude', 'Latitude']]
    print(df2.info())
    df3 = df2.dropna(axis=0, how='any')
    df5 = df3.loc[: ,['Longitude', 'Latitude']] # make sure the order
    df5.to_csv(csv_path, sep=' ', index=False, header=False)
    setPath(['/Users/patrick/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/ProcessX', '/Users/patrick/opt/anaconda3/envs/pynkdv/share/qgis/python', '/Users/patrick/Library/Application Support/QGIS/QGIS3/profiles/default/python', '/Users/patrick/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins', '/Users/patrick/opt/anaconda3/envs/pynkdv/share/qgis/python/plugins', '/Users/patrick/opt/anaconda3/envs/pynkdv/share/qgis/python/plugins', '/Users/patrick/opt/anaconda3/envs/pynkdv/share/qgis/python', '/Users/patrick', '/Users/patrick/opt/anaconda3/envs/pynkdv/lib/python39.zip', '/Users/patrick/opt/anaconda3/envs/pynkdv/lib/python3.9', '/Users/patrick/opt/anaconda3/envs/pynkdv/lib/python3.9/lib-dynload', '/Users/patrick/opt/anaconda3/envs/pynkdv/lib/python3.9/site-packages', '/Users/patrick/Library/Application Support/QGIS/QGIS3/profiles/default/python'])
    map_data = map_road_network(csv_path)


for i in range(4, 13):
    if i < 10:
        name = '2020-0' + str(i)
    else:
        name = '2020-' + str(i)

    path = '/Users/patrick/Desktop/Cheshire/' + name + '/' + name+'-cheshire-street.csv'
    csv_path = "dataset/" + name + '-cheshire-street.csv'
    print(path)
    print(csv_path)
    handle(path, csv_path)


