# ТГ бот конвертер

import  telebot

bot = telebot.TeleBot("6801993152:AAFKksnzFYxVMsDZrzCcpEKvgGrOFLq3OQE")

@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id,"Здравствуйте.")

@bot.message_handler(content_types=["text"])
def text_message(message):
    user_id = message.from_user.id



bot.polling(non_stop=True)