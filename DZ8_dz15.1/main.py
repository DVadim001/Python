# ТГ бот конвертер
import telebot
import buttons as bt

bot = telebot.TeleBot("6801993152:AAFKksnzFYxVMsDZrzCcpEKvgGrOFLq3OQE")

# обработка команды start
@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id,"Здравствуйте.", reply_markup=bt.sum_usd()) #






# @bot.message_handler(content_types=["text"])
# def text_message(message):
#     user_id = message.from_user.id
#
#     bot.send_message(user_id, "test")



bot.polling(non_stop=True)