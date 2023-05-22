import geopandas as gpd
import osmnx as ox
import momepy as mm
import matplotlib.pyplot as plt
import numpy as np
import contextily as cx
import matplotlib as mpl
import matplotlib.pyplot as plt
# from colorspacious import cspace_converter
import mplleaflet
import tilemapbase
gdf = gpd.read_file('/Users/patrick/Desktop/hkbu-college/doc/year3/sem1/econ3105/pythonProject3/output_test1.shp')
print(gdf.crs)
gdf.to_crs(3857, inplace=True)
tilemapbase.start_logging()
tilemapbase.init(create=True)

ax = gdf.plot('value', cmap='OrRd', legend=True)
cx.add_basemap(ax)
print('done')
plt.show()

# plt.plot(gdf)
print(gdf.crs)
print(gdf.info())
mplleaflet.show()

print('')
