import telebot
import requests
from telebot import types 
import random

API_TOKEN = '6012099586:AAGZXoBI7uEXFmVUqcYt2OVjnh6PAb9XRvY'

bot = telebot.TeleBot(API_TOKEN)

# Список id пользователей, которым будет доступна кнопка ADM
allowed_users = [712563713]

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем inline клавиатуру с тремя кнопками (или двумя, если пользователь не в списке allowed_users)
    markup = types.InlineKeyboardMarkup()
    info_button = types.InlineKeyboardButton("Информация", callback_data='info')
    entertainment_button = types.InlineKeyboardButton("Развлечения", callback_data='entertainment')
    if message.from_user.id in allowed_users:
        adm_button = types.InlineKeyboardButton("ADM", callback_data='adm')
        markup.add(info_button, entertainment_button, adm_button)
    else:
        markup.add(info_button, entertainment_button)
    bot.send_message(message.chat.id, "Привет! Я бот. Чем я могу помочь?", reply_markup=markup)

def inline_main(call):
        markup = types.InlineKeyboardMarkup() ###Создаем inline кнопки:                                                                                             
        news_button = types.InlineKeyboardButton("Что нового?", callback_data='news')                                                 
        about_button = types.InlineKeyboardButton("Обо мне", callback_data='about')
        support_button = types.InlineKeyboardButton("Поддержать разработчика", callback_data='support')
        markup.add(news_button, about_button, support_button) ###Добавляем кнопки
        bot.delete_message(call.message.chat.id, call.message.message_id) ###Удаляем последнее сообщение бота
        bot.send_message(call.message.chat.id, "Вы можете получить любую интересующую вас информацию.\nДля связи с разработчиком напишите на почту koroleevskiy@gmail.com", reply_markup=markup) ###Отправляем текст и кнопки

# Обработчик inline кнопок в стартовом меню
@bot.callback_query_handler(func=lambda call: True)
def callback_main(call):
    if call.data == 'info': ###Кнопка "Информация"
        inline_main(call)
    elif call.data == 'entertainment':
        markup = types.InlineKeyboardMarkup()
        cat_button = types.InlineKeyboardButton("Котик", callback_data='cat')
        roll_button = types.InlineKeyboardButton("Случайнон число", callback_data='roll')
        compl_button = types.InlineKeyboardButton("Комплимент", callback_data='compl')
        markup.add(cat_button, roll_button, compl_button)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Здесь будут развлечения", reply_markup=markup)
    elif call.data == 'adm' and call.message.chat.id in allowed_users:
        markup = types.InlineKeyboardMarkup()
        stop_button = types.InlineKeyboardButton("Стоп", callback_data='stop')
        restart_button = types.InlineKeyboardButton("Рестарт", callback_data='restart')
        markup.add(stop_button, restart_button)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Ваш админцентр", reply_markup=markup)
### Обработчик inline кнопок в меню информации 
    elif call.data == 'news':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Здесь будет информация о новостях")
    elif call.data == 'about':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Здесь будет информация обо мне")
    elif call.data == 'support':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Здесь будет информация о том, как поддержать разработчика")
### Обработчик inline кнопок в меню развлечений
    elif call.data == 'compl':
        random_message = lambda: random.choice(say)
        say = ['Твои глаза, как два алмаза', 'Вашей маме зять не нужен? Вам опасно ходить без зятя!', 'Как же хочется просто взять и обнять!', 'Обожаю нежно целовать тебя...', 'Котёнок мой, ты лучшее, что случалось со мной, за последнее время.', 'На планете есть семь чудес света, но есть еще одно, самое очаровательное и красивое - это ты!', 'Ты - та, о ком я думаю каждую секунду, минуту, час, сутки!', 'Ты мой ясный лучик, благодаря тебе я ежедневно просыпаюсь с улыбкой, ведь ты первое, о чем я думаю после пробуждения! Весь мир прекрасен, полон ярких красок и света, если ты рядом, мое солнце!', 'Ты изменила мою жизнь и меня самого. Ты наполнила особым, прекрасным смыслом каждое мгновение.', 'А помнишь те прогулки по ночам? Это лучшие прогулки за всю мою жизнь!', 'У меня заканчивается фантазия, но полным полно мыслей о тебе', 'Трусы в сердечко так и не купили, но ты и в обычных меня покоришь.', 'Солнце моё, я твой зайчик', 'Ни для кого подобного не делал. Я рад, что ты стала первой)', 'Меня бы побили за этот кривой код, но даже так, я не перестану думать о тебе', 'Я такю от тебя, как пломбир под июльским солнцем', 'Я не забуду этот понедельник!', 'Лучшее моё знакомство в ДайВинчике!']
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, random_message())
    elif call.data == 'roll':
        markup = types.InlineKeyboardMarkup()
        news_button = types.InlineKeyboardButton("Что нового?", callback_data='news')
        about_button = types.InlineKeyboardButton("Обо мне", callback_data='about')
        support_button = types.InlineKeyboardButton("Поддержать разработчика", callback_data='support')
        markup.add(news_button, about_button, support_button)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "доделать.", reply_markup=markup)
       # chat_id = message.chat.id
        #text = message.text[50:]  # Skip the "/roll" part of the message
       # dice, sides = (1, 50)
       #  if text:
       #   dice, sides = map(int, text.split('d'))
       # result = [random.randint(1, sides) for _ in range(dice)]
    # bot.send_message(chat_id, "Допустим это: " + "  ".join(map(str, result)))
    elif call.data == 'cat':
        cat_photos = requests.get("https://api.thecatapi.com/v1/images/search?limit=10").json()
        cat_photo = random.choice(cat_photos)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id, cat_photo["url"])
### Обработчик inline кнопок в меню администрации
    elif call.data == 'stop':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Остановка...")
        bot.stop_polling()
    elif call.data == 'restart':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Рестарт...")
        bot.stop_polling()
        bot.polling()

#Запускаем бота
bot.polling()