from  telegram.ext import Updater,CommandHandler
from Adafruit_IO import Client, Feed,Data
import requests #gets data from cloud
import os
name = os.getenv("name")
key = os.getenv("key") 
aio = Client(name,key)
# Create a data item with value 10 in the 'Test' feed.
def on(bot,update):
    chat_id=update.message.chat_id
    bot.send_message(chat_id,'Led on')
    data = Data(value=1)
    aio.create_data('okay', data)
def off(bot,update):
    chat_id=update.message.chat_id
    bot.send_message(chat_id,'Led off')
    data = Data(value=0)
    aio.create_data('okay', data)
u=Updater('1278640635:AAF8kPkUfeebEL32W_kIpIm0zL9XqpUy6YU')
dp=u.dispatcher
d=dp.add_handler(CommandHandler('on',on))
k=dp.add_handler(CommandHandler('off',off))
u.start_polling()
u.idle()
