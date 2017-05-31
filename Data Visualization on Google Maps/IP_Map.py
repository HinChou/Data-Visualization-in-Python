# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 13:28:54 2016

@author: hinnc
"""

import pandas as pd
import json
import gmplot


# Data is from: https://raw.githubusercontent.com/luyishisi/IP_location_wordpress/master/date/all.html
# Using "with" clause, without writing "ip.close()" explicitly
with open('IP Data.txt') as ip:
  ip_data = ip.read()

ip_data = ip_data.replace('\'', '\"')
ip_data = ip_data.replace(';', '')

# Convert a large string to a list of dictionaries
ip_jdata = json.loads(ip_data)

ip_jdata = pd.DataFrame(ip_jdata)

# Determine the initial frame of the map
gmap = gmplot.GoogleMapPlotter(39.9390731, 116.1172613, 4)

gmap.heatmap(ip_jdata['lat'], ip_jdata['lng'], opacity = 0.8)

gmap.draw('ip_map.html')
