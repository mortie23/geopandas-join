#!/usr/bin/python3
import pandas as pd
import geopandas

# for plots
df = pd.read_csv("dummy.csv")
gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.X, df.Y))

gdf.set_crs(epsg=4283, inplace=True)

# print(gdf.head())
filename = 'RA_2016_AUST'
dirpath = '/mnt/c/data/geodata/'

# only need to run once
#myshpfile = geopandas.read_file(dirpath+filename+'/'+filename+'.shp')
#myshpfile.to_file('./'+filename+'.json', driver='GeoJSON')
#print('Converted '+filename)

# for jupyter only
#world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
#base = world.plot(color='white', edgecolor='black')
#gdf.plot(ax=base, color='red')
# plt.show()

RA_AREAS = geopandas.read_file(dirpath + filename + '/' + filename + '.shp')
RA_join = geopandas.sjoin(gdf, RA_AREAS, how='inner')

print(RA_join)

# curl -O https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tar.xz
