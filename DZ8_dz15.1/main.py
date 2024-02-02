# ТГ бот конвертер
import telebot
import buttons as bt

bot = telebot.TeleBot("6801993152:AAFKksnzFYxVMsDZrzCcpEKvgGrOFLq3OQE")


# обработка команды start
@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Здравствуйте, выберите вылюту, которую хотите сконвертировать",
                     reply_markup=bt.sum_usd())


@bot.message_handler(content_types=["text"])
def text_message(message):
    user_id = message.from_user.id
    if message.text == "Sum":
        bot.send_message(user_id, "Введите сумму в сумах")
        bot.register_next_step_handler(message, convert_sum_to_usd)
    elif message.text == "USD":
        bot.send_message(user_id, "Введите сумму usd")
        bot.register_next_step_handler(message, convert_usd_to_sum)
    else:
        bot.send_message(user_id, "Нажмите на кнопку для выбора валюты", reply_markup=bt.sum_usd())


def convert_sum_to_usd(message):
    user_id = message.from_user.id
    convert_rate = 12300
    try:
        sum_amount = float(message.text)
        result = sum_amount / convert_rate
        bot.send_message(user_id, f"Ваша сумма в суммах '{message.text}'из составляет '{result}' usd",
                         reply_markup=bt.sum_usd())
    except:
        bot.send_message(user_id, "Введите числовое значение!")


def convert_usd_to_sum(message):
    user_id = message.from_user.id
    convert_rate = 12300
    try:
        sum_amount = float(message.text)
        result = sum_amount * convert_rate
        bot.send_message(user_id, f"Ваша сумма из составляет '{result}' сум", reply_markup=bt.sum_usd())
    except:
        bot.send_message(user_id, "Введите числовое значение!")


bot.polling(non_stop=True)
