import telebot


TOKEN = '7536764664:AAFmUa7bvHjL_rlQapj2y4G4usn_tX_5UWc'  
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)