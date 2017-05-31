# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 01:40:58 2016

@author: Hin
"""

# Heatmap of Houses in San Francisco(SF)
import gmplot
import pandas as pd


data_sf = pd.read_csv('data_sf.csv')

# Determine the initial frame of the map
gmap = gmplot.GoogleMapPlotter(37.770771, -122.413081, 12)

gmap.heatmap(data_sf['lat'], data_sf['lon'], opacity = 0.8)

gmap.draw('mymap.html')
