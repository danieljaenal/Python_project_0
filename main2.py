# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 19:15:09 2022

@author: danie
"""


import Constants as keys
from telegram.ext import *
import Responses as R
import json


print("Bot started... ")


from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

# def main():
#     updater = Updater('5894955616:AAG_4S2XLv9Wx4BhGTC3uykjXWnzwigggj4', use_context= True)
#     dp = updater.dispatcher
#     dp.add_handler(CommandHandler('bop',bop))
#     updater.start_polling()
#     updater.idle()

# if __name__ == '__main__':
#     main()


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def start_command(update, context):
    update.message.reply_text("Type something random to get started!")
    
def help_command(update, context):
    update.message.reply_text("if you need help you should ask Google!")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    
    update.message.reply_text(response)
    
def error(update, context):
    print(f"Update {update} causes error {context.error}")
    
def main():
    updater= Updater(keys.API_KEY, use_context=True)
    dp= updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("start", help_command))
    
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()
    
main()