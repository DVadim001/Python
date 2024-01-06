from telebot import types

def num_bt():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    num = types.KeyboardButton("Отправить номер", request_contact=True)
    kb.add(num)
    return kb


def loc_bt():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    loc = types.KeyboardButton("Отправить локацию", request_location=True)
    kb.add(loc)
    return kb