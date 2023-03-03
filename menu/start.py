def inline_main(call):
        markup = types.InlineKeyboardMarkup() ###Создаем inline кнопки:                                                                                             
        news_button = types.InlineKeyboardButton("Что нового?", callback_data='news')                                                 
        about_button = types.InlineKeyboardButton("Обо мне", callback_data='about')
        support_button = types.InlineKeyboardButton("Поддержать разработчика", callback_data='support')
        markup.add(news_button, about_button, support_button) ###Добавляем кнопки
        bot.delete_message(call.message.chat.id, call.message.message_id) ###Удаляем последнее сообщение бота
        bot.send_message(call.message.chat.id, "Вы можете получить любую интересующую вас информацию.\nДля связи с разработчиком напишите на почту koroleevskiy@gmail.com", reply_markup=markup) ###Отправляем текст и кнопки