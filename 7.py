import telebot
from telebot import types
# https://t.me/test_for_joparo_bot
token = "5227484175:AAEWGEcfa1q0gMA4HfAEL843Qk7NFdOe1Cw"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информациюо МТУСИ?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею...')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда - https://mtuci.ru/')

bot.polling(none_stop=True)