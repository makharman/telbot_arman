import telebot
from env import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['info'])
def info(massage):
    bot.send_message(massage.chat.id, "Info about bot")
    
bot.polling()