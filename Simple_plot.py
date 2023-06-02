import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as cx


def generate_one_figure(name, path):
    gdf = gpd.GeoDataFrame.from_file(path)
    gdf.to_crs(4328, inplace=True)
    gdf.plot(column='value', cmap='OrRd', figsize=(60, 60), legend=True)
    plt.savefig(name + '.png')
    plt.clf


city_list = ['Chicago__crime', 'San', 'NYC']
b_list = [150, 300, 500, 1000, 1500, 2000, 3000, 5000]
base_path = '/Users/patrick/Desktop/output/'
for city in city_list:
    for i in b_list:
        layer_name = city + '_b' + str(i)
        path = base_path + layer_name + '.shp'
        print(path)
        generate_one_figure(layer_name + '_kdv', path)
