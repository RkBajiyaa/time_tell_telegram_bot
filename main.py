import telebot
import constants as api_key
bot = telebot.TeleBot(api_key.API_KEY)
from datetime import datetime

print("bot Started!!!")

@bot.message_handler(commands=['start','hello', 'help me'])
def send_welcome(message):
    bot.reply_to(message, "Howdyy!!!")

@bot.message_handler(commands=['hi'])
def hi_reply(message):
    bot.reply_to(message, "Hello! how are you?")

@bot.message_handler(commands=['time','time?'])
def time_tell(message):
    now=datetime.now()
    date_time = str(now.strftime("%d/%m/%y, %H:%M:%S"))
    bot.reply_to(message, date_time)

@bot.message_handler(func=lambda message: True)
def anything(message):
    bot.reply_to(message, "I don't understand")

# print(date_time)
bot.infinity_polling()
