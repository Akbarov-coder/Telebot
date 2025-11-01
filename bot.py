import telebot
from logic import gen_pass

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я твой Telegram бот. Напиши что-нибудь! Чтобы узнать все доступные функции просто напиши Команды ")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "Привет":
        bot.reply_to(message, "Привет! Как дела?")
    elif message.text == "Пока":
        bot.reply_to(message, "Пока! Удачи!")
    elif message.text == "Йоу":
        bot.reply_to(message, "Йоу!")
    elif message.text == "Что ты можешь?":
        bot.reply_to(message, "Пока мало чего( Но в будущем у меня будет БОЛЬШЕ функций!")
    elif message.text == "Команды":
        bot.reply_to(message, "Привет, Пока, Йоу, Что ты можешь?, /password, Ты тупой.")


@bot.message_handler(commands=['password'])
def send_password(message):
    bot.reply_to(message, gen_pass(12))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "Ты тупой":
        bot.send_message(message.chat.id, "Сам тупой")
    else:
        bot.send_message(message.chat.id, "Что хочешь?")

bot.polling()