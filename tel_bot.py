# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 23:58:59 2019

@author: Mohammad Amin Roohi
"""


from __future__ import print_function

from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import telegram



#SCOPES = 'https://www.googleapis.com/auth/drive'
#store = file.Storage('storage.json')
#creds = store.get()
#if not creds or creds.invalid:
   # flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
   # creds = tools.run_flow(flow, store)

#DRIVE = discovery.build('drive', 'v2', http=creds.authorize(Http()),cache_discovery=False)



updater = Updater(token='1012021563:AAH4J0iP6xzrR49euuxxSGC-Br_dz6yvjb0', use_context=True)
dispatcher = updater.dispatcher
dispatcher1 = updater.dispatcher
dispatcher2 = updater.dispatcher
dispatcher3 = updater.dispatcher




logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


custom_keyboard = [['Send an Image', 'Send the Name of Image']]


def start(update, context):
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Thank you for helping WikiZob, You are now an environment lover!!!" , reply_markup=reply_markup)
    


    
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def act(update, context):
    text=update.message.text
    
    if text == 'Send an Image':
        context.bot.send_message(chat_id=update.effective_chat.id, text="I am waiting to receive your image!")
        image_handler = MessageHandler(Filters.photo, image)
        dispatcher2.add_handler(image_handler)

    
    if text == 'Send the Name of Image':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please tell me the name of picture you just sent!")
        
            
        
    


def text(update , context):  
    f_id = update.message.photo[-1].file_id  
    file_image = context.bot.getFile(f_id)
    print ("file_id: " + str(update.message.photo[-1].file_id))
    file_image.download('C:/Users/Mohammad Amin Roohi/Desktop/bot.jpg')
    context.bot.send_message(chat_id=update.effective_chat.id, text="I got your image, Thanks!!!")



def image(update , context):  
    f_id = update.message.photo[-1].file_id  
    file_image = context.bot.getFile(f_id)
    print ("file_id: " + str(update.message.photo[-1].file_id))
    file_image.download('C:/Users/Mohammad Amin Roohi/Desktop/bot.jpg')
    context.bot.send_message(chat_id=update.effective_chat.id, text="I got your image, Thanks. Now, you should tell me name of this...")
    
    
    
def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu    
    



#  FILES = ((update.message.photo[-1].file_name, False),(update.message.photo[-1].file_name, True))
 # for filename, convert in FILES:
#     metadata = {'title': update.message.photo[-1].file_name}
   #  DRIVE.files().insert(convert=convert, body=metadata,media_body=filename, fields='mimeType,exportLinks').execute()
     #if res:
      #   print('Uploaded "%s" (%s)' % (filename, res['mimeType']))
         # silentremove(filename) #if u want to remove upladed file from local 
         #update.message.reply_text("Uploaded!")
       #  context.bot.send_message(chat_id=update.effective_chat.id, text= 'Uploaded!')




start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)



#echo_handler = MessageHandler(Filters.text, echo)
#dispatcher1.add_handler(echo_handler)




#file = MessageHandler(Filters.photo, file_handler)
#dispatcher3.add_handler(file)

act_handler = MessageHandler(Filters.text, act)
dispatcher3.add_handler(act_handler)


updater.start_polling()













