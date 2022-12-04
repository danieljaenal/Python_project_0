# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 12:55:41 2022

@author: danie
"""
import requests
import json

  
def check_city():
    url = "https://api.openaq.org/v1/cities?limit=3000&offset=0&sort=asc&order_by=city"
    
    headers = {"accept": "application/json"}
    
    response = requests.get(url, headers=headers)
    
    js = response.json()
    cities=[]
    for item in js["results"]:
      cities.append(item["city"])
    
    return cities
    

# print(response.text)

# url = "https://api.openaq.org/v1/cities"

# pais = "ES"
# datos= requests.get(url, params={"country": pais})

# js = datos.json()

# for item in js["results"]:
#   city = item["name"]
#   print(city)