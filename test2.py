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
# gdf = gpd.read_file('/Users/patrick/Desktop/hkbu-college/doc/year3/sem1/econ3105/pythonProject3/output_test1.shp')
gdf = gpd.GeoDataFrame.from_file('/Users/patrick/Desktop/hkbu-college/doc/year3/sem1/econ3105/pythonProject3/output_test1.shp')

print(gdf.crs)
# gdf.to_crs(3857, inplace=True)
gdf.to_crs(4326, inplace=True)

#ax = gdf.plot('value', cmap='OrRd', scheme='equal_interval', legend=True, alpha=1, linewidth=1.5)
# alpha scheme cmap
# ax = gdf.plot(column='value', scheme='quantiles', cmap='OrRd', figsize=(200, 200),legend=True, linewidth=1.5)
m = gdf.explore(column='value', cmap='OrRd')
m.save('test_active_map')
#ax = gdf.plot(column='value', cmap='OrRd')

# plt.savefig('test_fig')
# mplleaflet.show(fig=ax.figure, crs=gdf.crs, path='sgmap.html')
# mplleaflet.show(fig=ax.figure, crs=gdf.crs, path='sgmap1.html')


# cx.add_basemap(ax)
print('done')
# plt.savefig('test_fig')
plt.show()

# plt.plot(gdf)
print(gdf.crs)
print(gdf.info())
#mplleaflet.show()

print('')
