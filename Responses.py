# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 18:59:40 2022

@author: danie
"""

import requests
import urllib.request
import urllib.parse
from datetime import datetime
import matplotlib.pyplot as plt
import available_cities

def city_weather(city):
  
    url= "https://api.openweathermap.org/data/2.5/forecast?q={city name}&units=metric&appid={API key}"
    api_key = '3886d5996f84c5b9a5c953b027fc2306'
      
    # city= urllib.parse.quote(input("Introduce la ciudad: "))
    city=urllib.parse.quote(city)
    url2= url.replace("{city name}", city).replace("{API key}", api_key)
    # print(url2)
      
    data= requests.get(url2)
    js = data.json()
      
    fechas=[]
    temperatura=[]
    for item in js["list"]:
      temperatura.append(item["main"]["feels_like"])
      fechas.append(item["dt_txt"])
      
      
    ts2 = [datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in fechas]
    fig= plt.figure(figsize=(12, 4))
    plt.grid()
      
    plt.plot(ts2, temperatura, color="blue");
    plt.savefig("temperatura.png")
      
    files = {'photo': open('temperatura.png', 'rb')}  
    url= 'https://api.telegram.org/bot5894955616:AAG_4S2XLv9Wx4BhGTC3uykjXWnzwigggj4/sendPhoto?chat_id=-1001822743230'
    url_caption = url + '&caption=' + 'El tiempo en ' + str(city)
    resp= requests.get(url_caption, files = files)
      
    # print(resp.status_code)
    # print(resp.text)

  
def sample_responses (input_text):

    user_message = str(input_text)
    user_message= user_message.replace("/", "")
    
    cities=available_cities.check_city()
    
    if user_message in cities:
        city_weather(city=user_message)
        # mensaje= "Aquí tienes el tiempo en " + str(user_message)
        # return mensaje

    elif user_message not in cities:
        return "City not found, please try another one"
    
    if user_message in ("time", "time?"):
        new = datetime.now()
        date_time= now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)
    
    # print("llegué")
    return "I don't understand you"