from telebot import types


def sum_usd():
    # Создание пространства
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создание кнопок
    sum = types.KeyboardButton("Sum")
    usd = types.KeyboardButton("USD")
    # Добавление кнопок в пространство
    kb.add(sum, usd)
    return kb