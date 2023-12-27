import telebot
from telebot.types import ReplyKeyboardRemove
from buttons import kb

#создать объект бота
bot = telebot.TeleBot('6575299390:AAHsMK6PjueGwxPS64A1fbyqdwkjrS2nK_M')

# обработка команды start
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Привет! Добро пожаловать!", reply_markup=kb)


# # Обработка текстовых сообщений
# @bot.message_handler(content_types=["text"])
# def text_nessage(message):
#     user_id = message.from_user.id
#     bot.send_message(user_id, message.text)


# отправляет текст, который хотим передать
@bot.message_handler(content_types=["text"])
def text_nessage(message):
    user_id = message.from_user.id
    if message.text.lower() == "википедия":
        bot.send_message(user_id, "Введите слово: ", reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, wiki)
    elif message.text.lower() == "переводчик":
        bot.send_message(user_id, "Введите слово для перевода: ", reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, tran)
    else:
        bot.send_message(user_id, "Неизвестная операция")
        bot.register_next_step_handler(message, wiki)


def wiki(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Пройдите на сайт википедии!", reply_markup=ReplyKeyboardRemove())
    bot.send_message(user_id, "Готово, что ещё?", reply_markup=kb)
    bot.register_next_step_handler(message,text_nessage)
def tran(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Пройдите на сайт переводчика!", reply_markup=ReplyKeyboardRemove())
    bot.send_message(user_id, "Готово, что ещё?", reply_markup=kb)
    bot.register_next_step_handler(message, text_nessage)



# Запуск бота
bot.polling(non_stop=True)