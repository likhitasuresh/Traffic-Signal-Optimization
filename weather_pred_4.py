# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 20:14:33 2019

@author: Likhita Suresh
"""
from geopy.geocoders import Nominatim
from datetime import datetime,timedelta
import sys, requests
import numpy

DARK_SKY_API_KEY = "7d24336217bfc27f8c4e7c8c3c578e1b"
option_list = "exclude=currently,minutely,alerts&amp;units=si"

l1 = 'Los Angeles'
d1 = '2019-06-3'
d2 = '2019-06-3'


location = Nominatim().geocode(l1, language='en_US', timeout=30)
d_from_date = datetime.strptime(d1 , '%Y-%m-%d')
d_to_date = datetime.strptime(d2 , '%Y-%m-%d')


delta = d_to_date - d_from_date
latitude = str(location.latitude)
longitude = str(location.longitude)


for i in range(delta.days+1):
  new_date = (d_from_date + timedelta(days=i)).strftime('%Y-%m-%d')
  search_date = new_date+"T00:00:00"
  response = requests.get("https://api.darksky.net/forecast/"+DARK_SKY_API_KEY+"/"+latitude+","+longitude+","+search_date+"?"+option_list)
  json_res = response.json()
  unit_type = '°C'
bar=[]

bar.append([])


for q in range(6,23):
    bar[0].append(str(datetime.fromtimestamp(json_res['hourly']['data'][q]['time'])))
    
bar.append([])   
for q in range(6,23):
    bar[1].append(str(datetime.weekday(datetime.fromtimestamp(json_res['hourly']['data'][q]['time']))))
bar.append([])    
for q in range(6,23):
    bar[2].append(str(json_res['hourly']['data'][q]['apparentTemperature']))
bar.append([])    
for q in range(6,23):
    bar[3].append(str(json_res['hourly']['data'][q]['icon']))
a = numpy.empty([17,4])
for i in range(0,17):
    a[i][0]=i+6
    a[i][1]=bar[1][0]    
    a[i][2]=bar[2][i] 
    encode={
            'clear-day': 0 ,
              'clear-night':1,
              'rain':2,
              'wind':3,
              'fog':4,
              'cloudy':5,
              'partly-cloudy-day':6,
              'partly-cloudy-night':7,
              'snow':8,
              'sleet':9
             }
   
    a[i][3]=encode.get(bar[3][i], "")