# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 18:57:08 2022

@author: danie
"""
import Constants as keys
from telegram.ext import *
import Responses as R
import json
from telegram import Update

print("Bot started... ")


from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests

import urllib.request
import urllib.parse

from datetime import datetime
import matplotlib.pyplot as plt



def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    # print(url)
    return url
# def echo(update: Update, context: CallbackContext):
# 	update.message.reply_photo(photo=url)

def tiempo(bot, update): 
    # c_id = '-1001822743230'   
    # filename = 'C:/Users/danie/Documents/Python_project/temperatura.png'  
    files = {'photo': open('foto.jpg', 'rb')}  
    resp= requests.get('https://api.telegram.org/bot5894955616:AAG_4S2XLv9Wx4BhGTC3uykjXWnzwigggj4/sendPhoto?chat_id=-1001822743230', files = files)

    print(resp.status_code)
    print(resp.text)

def send_photo_from_URL(update:Update,context:CallbackContext):
  chat_id='-1001822743230'
  url_photo= 'https://images.unsplash.com/photo-1587691592099-24045742c181?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1746&q=80'

  context.bot.send_photo(chat_id=chat_id, photo=url_photo)

def perro(bot, update):
    url = get_url()
    url_chat= 'https://api.telegram.org/bot5894955616:AAG_4S2XLv9Wx4BhGTC3uykjXWnzwigggj4/sendPhoto'
    parameters = {
        "chat_id": '-1001822743230',
        "photo": url}
    resp= requests.get(url_chat, data = parameters)
    print(resp.text)

def start_command(update, context):
    update.message.reply_text("Type something random to get started!")
    
def help_command(update, context):
    update.message.reply_text("if you need help you should ask Google!")

def handle_message(update, context):
    text = str(update.message.text)
    # print(text)
    response = R.sample_responses(text)
    
    update.message.reply_text(response)
    
def error(update, context):
    print("Update", {update}, "causes error", {context.error})
    
def main():
    updater= Updater(keys.API_KEY, use_context=True)
    dp= updater.dispatcher
    
    dp.add_handler(CommandHandler("tiempo", tiempo))
    dp.add_handler(CommandHandler("perro", perro))
    dp.add_handler(CommandHandler("url", send_photo_from_URL))
    # dp.add_handler(CommandHandler("Madrid", city_weather))
    
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()
    
main()

    