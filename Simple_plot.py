import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as cx

gdf = gpd.GeoDataFrame.from_file('/Users/patrick/Desktop/output/Chicago__crime_b150.shp')
gdf.to_crs(3857, inplace=True)
ax = gdf.plot(column='value', scheme='quantiles', cmap='OrRd', k=8, figsize=(80, 80), legend=True)
plt.savefig('test_fig')
