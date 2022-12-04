# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 18:59:40 2022

@author: danie
"""

#A ESTE MÓDULO VENGO CUANDO RECIBO UN MENSAJE EN EL BOT DEL TELEGRAM. 
#ANALIZO SI ES UNA CIUDAD EN LA LISTA DE CIUDADES DISPONIBLES. DE SER ASÍ, LLAMARÉ A LA FUNCIÓN city_weather
# PARA QUE ME GENERE LA GRÁFICA Y LA ENVÍE COMO MENSAJE DE VUELTA AL CHAT DE TELEGRAM. 

import requests
import urllib.request
import urllib.parse
from datetime import datetime
import matplotlib.pyplot as plt
import available_cities
import Constants

def city_weather(city):
  
    url= "https://api.openweathermap.org/data/2.5/forecast?q={city name}&units=metric&appid={API key}"
    api_key = '3886d5996f84c5b9a5c953b027fc2306'
      
    # city= urllib.parse.quote(input("Introduce la ciudad: "))
    city_uncoded=urllib.parse.quote(city)
    url2= url.replace("{city name}", city_uncoded).replace("{API key}", api_key)
      
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
    plt.ylabel("ºC")
    titulo_grafico= "Pronóstico temperatura en " + str(city)
    plt.title(titulo_grafico)
      
    plt.plot(ts2, temperatura, color="blue");
    plt.savefig("temperatura.png")
      
    files = {'photo': open('temperatura.png', 'rb')}  

    url= 'https://api.telegram.org/bot' + Constants.API_KEY + '/sendPhoto?chat_id=' + Constants.chat_id

    url_caption = url + '&caption=' + 'El tiempo en ' + str(city)
    resp= requests.get(url_caption, files = files)
      
    # print(resp.status_code)
    # print(resp.text)


def chequear_respuesta (input_text):

    user_message = str(input_text)
    user_message= user_message.replace("/", "")
    
    cities=available_cities.check_city()
    
    if user_message in cities:
        # user_message= urllib.parse.quote(user_message) #aquí traduzco el nombre de la ciudad a código que entiende la máquina
        city_weather(city=user_message)
        # mensaje= "Aquí tienes el tiempo en " + str(user_message)

    elif user_message not in cities:
        return "City not found, please try another one"

    else:
        return "I don't understand you"
    
    return "Listo, dime otra ciudad de la que quieras conocer el pronóstico del tiempo o escribe /perro"