# -*- coding: utf-8 -*-
"""
Created on Sun Sep 4  13:45:46 2016

@author: hinnc
"""

import pandas as pd
import gmplot


url = ('http://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=' +
'2010-01-01&endtime=2016-01-01&minmagnitude=5.0')

# read_table(): the first parameter, filepath_or_buffer, could be a URL. Valid URL schemes include http, ftp, s3 and file.
earthquake = pd.read_table(url, sep = '|', header = 0)

# Determine the initial frame of the map
gmap = gmplot.GoogleMapPlotter(0, 0, 2)

gmap.heatmap(earthquake['Latitude'], earthquake['Longitude'], opacity = 0.8)

gmap.draw("earthquake.html")
