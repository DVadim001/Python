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


# # Обработка текстовых сообщений (вывод того же сообщения, который ввёл пользователь)
# @bot.message_handler(content_types=["text"])
# def text_nessage(message):
#     user_id = message.from_user.id
#     bot.send_message(user_id, message.text)


# отправляет текст, который хотим передать
@bot.message_handler(content_types=["text"])
def text_message(message):
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
    bot.send_message(user_id, "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0", reply_markup=ReplyKeyboardRemove())
    bot.send_message(user_id, "Готово, что ещё?", reply_markup=kb)
    bot.register_next_step_handler(message,text_message)
def tran(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Пройдите на сайт переводчика!", reply_markup=ReplyKeyboardRemove())
    bot.send_message(user_id, "Готово, что ещё?", reply_markup=kb)
    bot.register_next_step_handler(message, text_message)



# Запуск бота
bot.polling(non_stop=True)