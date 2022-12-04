# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 18:59:40 2022

@author: danie
"""

from datetime import datetime

def sample_responses (input_text):
    user_message = str(input_text).lower()

    if user_message == "hello":
        return "Hey, how is it going"
    
    if user_message in ("hello", "hi", "sup"):
        return "Hey, how is it going"
    
    if user_message in ("who are you", "who are you?"):
        return "I am ABC bot"
    
    if user_message in ("time", "time?"):
        new = datetime.now()
        date_time= now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)
    
    print("llegué")
    # return "I don't understand you"