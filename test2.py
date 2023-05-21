import geopandas as gpd
import osmnx as ox
import momepy as mm
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# from colorspacious import cspace_converter

gdf = gpd.read_file('/Users/patrick/Desktop/hkbu-college/doc/year3/sem1/econ3105/pythonProject3/output_test1.shp')
gdf.plot('value', cmap='OrRd',legend=True)

plt.show()
print('')
