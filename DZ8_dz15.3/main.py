# ТГ бот регистрации

import telebot, buttons as bt
from geopy import Nominatim

bot = telebot.TeleBot("6643297345:AAH2Dprar4RgV7PQ4rYd0skrGPdl7cj01m0")

geo = Nominatim(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id,f"Добро пожаловать, Начало регистрации. Введите имя.")
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    name = message.text
    user_id = message.from_user.id
    bot.send_message(user_id,"Имя получено, отправьте номер", reply_markup=bt.num_bt())
    bot.register_next_step_handler(message, get_num, name)


def get_num(message, name):
    user_id = message.from_user.id
    if message.contact:
        num = message.contact.phone_number
        bot.send_message(user_id,"Номер получен, отправьте локацию", reply_markup=bt.loc_bt())
        bot.register_next_step_handler(message, get_loc, name, num)
    else:
        bot.send_message(user_id, "Отправьте по кнопке.", reply_markup=bt.num_bt())
        bot.register_next_step_handler(message, get_num, name)

def get_loc(message):
    user_id = message.from_user.id
    if message.location:
        loc = str(geo.reverse(f"{message.location.latitude}.{message.location.longitude}"))
        bot.send_message(user_id,"Регистрация успешна", reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(user_id, "Отправьте по кнопке.", reply_markup=bt.loc_bt())
        bot.register_next_step_handler(message, get_loc, name, num)

bot.polling(non_stop=True)