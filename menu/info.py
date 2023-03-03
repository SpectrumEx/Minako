import telebot
from telebot import types 
import config
import menu.start

bot = telebot.TeleBot(config.token)
main_button = types.InlineKeyboardButton("На главную", callback_data='main')

def inline_news(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(main_button)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id, "Здесь будет информация о новостях", reply_markup=markup)
def inline_about(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(main_button)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id, "Здесь будет информация обо мне", reply_markup=markup)
def inline_support(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(main_button)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id, "Здесь будет информация о том, как поддержать разработчика", reply_markup=markup)