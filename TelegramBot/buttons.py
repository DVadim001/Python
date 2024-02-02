from telebot import types

# Создаём пространство для кнопок
kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

# Создаём сами кнопки
wiki = types.KeyboardButton("Википедия")
translate = types.KeyboardButton("Переводчик")

# Добавляем кнопки в пространство
kb.add(wiki, translate)
