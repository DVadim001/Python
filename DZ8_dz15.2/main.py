# ТГ бот простое приветствие

import telebot

TOKEN = "6846209665:AAFRg29rxion_63-cDeKvxyX9iK_ejiJTFw"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Здравствуйте!")


@bot.message_handler(commands=["help"])
def help(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_"
                              "%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")


bot.polling(non_stop=True)
