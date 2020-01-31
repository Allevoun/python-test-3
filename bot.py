# -*- coding: utf-8 -*-
import config
import telebot
from telebot import apihelper

# apihelper.proxy = {'https': 'socks5h://{confix.PROXY}}'}
apihelper.proxy = {'https': 'https://116.203.230.195:1080'}
bot = telebot.TeleBot(config.token)


# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, 'Hello bro')


# if __name__ == '__main__':
#     bot.infinity_polling()
# так непонятно почему не работает

bot.polling(none_stop=True)  # а вот так работает
