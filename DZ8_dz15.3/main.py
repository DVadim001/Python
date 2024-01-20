# ТГ бот регистрации.
import telebot
import database as db
import buttons as bt
from geopy import Nominatim


bot = telebot.TeleBot("6643297345:AAH2Dprar4RgV7PQ4rYd0skrGPdl7cj01m0")
geo = Nominatim(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                           "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

selected_lang = {}
texts = {"welcome_message": {"rus": "Здравствуйте.", "eng": "Welcome."},
         "reg_begin": {"rus": "Начало регистрации. Введите имя.", "eng": "Registration start. Enter your name."},
         "name_res": {"rus":"Имя получено, отправьте номер.", "eng": "Name received, send the number."},
         "loc_res": {"rus":"Номер получен, отправьте локацию.", "eng": "Number received, send the location."},
         "send_but": {"rus":"Отправьте по кнопке.", "eng": "Send using the button."},
         "reg_suc": {"rus":"Регистрация успешна.", "eng": "Registration successful."},
         "lang_choose": {"rus":"Добро пожаловать. Выберите удобный для вас язык", "eng": "Welcome. Choose your preferred language"},
         "set_lang": {"rus":"Установлен язык: Русский.", "eng": "Your language has beet set to: English"},
         # "": {"rus":"", "eng": ""},
         }


def lang_choice(user_id, keyword):
    user_lang = selected_lang.get(user_id, "rus")
    return texts[keyword][user_lang]



@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    check = db.check_in_base(user_id)
    if check:
        bot.send_message(user_id, f"Здравствуйте, '{message.from_user.first_name}', выберите удобный для вас язык.", reply_markup=bt.lang())
    else:
        bot.send_message(user_id,f"Добро пожаловать. Выберите удобный для вас язык",reply_markup=bt.lang())
        bot.send_message(user_id,f"Начало регистрации. Введите имя.")
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


def get_loc(message, name, num):
    user_id = message.from_user.id
    if message.location:
        loc = str(geo.reverse(f"{message.location.latitude},"f"{message.location.longitude}"))
        db.registration(user_id, name, num, loc)
        bot.send_message(user_id,"Регистрация успешна", reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(user_id, "Отправьте по кнопке.", reply_markup=bt.loc_bt())
        bot.register_next_step_handler(message, get_loc, name, num)


@bot.callback_query_handler(lambda call: call.data in ['rus', 'eng'])
def choose_lang(call):
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    selected_lang[user_id] = call.data
    if call.data == "rus":
        bot.send_message(chat_id, "Установлен язык: Русский",reply_markup=telebot.types.ReplyKeyboardRemove())
    elif call.data == "eng":
        bot.send_message(chat_id, "Your language has beet set to: English", reply_markup=telebot.types.ReplyKeyboardRemove())



bot.polling(non_stop=True)
