import random

import telebot
from projectfiles.dates import *
import datetime

# Функция отправки нашего расписания работы
def timeworking(message, bot):
    time = ['09:00 - 19:00', '09:00 - 19:00', '09:00 - 16:00', '09:00 - 19:00', '09:00 - 19:00', '10:00 - 17:00',
            '10:00 - 15:00']
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    markup = telebot.types.InlineKeyboardMarkup()
    index = 0
    for i in time:
        btn1 = telebot.types.InlineKeyboardButton(days[index], callback_data = 1)
        btn2 = telebot.types.InlineKeyboardButton(time[index], callback_data = 2)
        index += 1
        markup.row(btn1, btn2)
    bot.send_message(message.chat.id, "Наш режим работы", reply_markup=markup)

# Функция отправки наших социальных сетей
def socialntworks(message, bot):
    namessocialnetworks = ['📸   Instagram   📸',
                           '🎥   YouTube   🎥',
                           '📱   Vkontakte   📱',
                           '📽   RuTube   📽',
                           '📡   WebSite   📡']
    socialnetworks = ['https://www.instagram.com/glessgroup/',
                      'https://www.youtube.com/c/GLeSSGroup',
                      'https://vk.com/gless_group_omsk',
                      'https://rutube.ru/channel/25007187/',
                      'https://gless.group/']
    index = 0
    markup = telebot.types.InlineKeyboardMarkup()
    for i in socialnetworks:
        button = telebot.types.InlineKeyboardButton(namessocialnetworks[index], url=socialnetworks[index])
        markup.add(button)
        index += 1
    bot.send_message(message.chat.id, "Наши социальные сети", reply_markup=markup)

# Функция отправки ошибки ввода сообещния
def senderrormessage(message, bot):
    text = "Я что-то ничего не понимаю( Кликните по кнопке, пожалуйста."
    bot.send_message(message.chat.id, text)

# Функция отправки ссылок на наши отзывы
def reviews(message, bot):
    reviewsnetworks = ['📸   Flump   📸',
                       '📍   2GIS   📍',
                       '📨   YandexMaps   📨',
                       '🌎   GoogleMaps   🌎']
    socialnetworks = ['http://omsk.flamp.ru/firm/gless_avtotekhcentr-282003257988334',
                      'https://go.2gis.com/xotto',
                      'https://yandex.ru/maps/-/CCUZ4Lc8kB',
                      'https://goo.gl/maps/4CGmYUNVMuh8Md7P8']
    index = 0
    markup = telebot.types.InlineKeyboardMarkup()
    for i in socialnetworks:
        button = telebot.types.InlineKeyboardButton(reviewsnetworks[index], url=socialnetworks[index])
        markup.add(button)
        index += 1
    bot.send_message(message.chat.id, "Оставьте о нас мнение!", reply_markup=markup)

# Функция отправки id человека
def youid(message, bot):
    text = "Человек : " + str(message.chat.id) + "\n" + str(message.chat.first_name) + " " + str(
        message.chat.last_name) + "\n" + str(message.chat.username)
    text2 = "Написал следующее: " + message.text
    bot.send_message(userid.id_6080, text)
    bot.send_message(userid.id_6080, text2)
    text3 = "Ваш ID: \n" + str(message.chat.id)
    bot.send_message(message.chat.id, text3)

# Функция записи на обслуживание
def serviserecord(message, bot):
    today = datetime.datetime.today()
    todaytime = today.strftime("%H:%M:%S")
    msg = bot.send_message(message.chat.id, "Выберите тему обращения.")
    listid = [userid.id_beregovoy, userid.id_konovalov, userid.id_zagravskiy]
    listnames = [class_namesmanagers.second, class_namesmanagers.third, class_namesmanagers.first]
    randommanager = random.randint(0, len(listid) - 1)
    textmessage = todaytime + " [" + message.chat.first_name + " " + message.chat.last_name + "] нажал на кнопку [📝Записаться📝]  перевожу заявку на " + listnames[randommanager] + " ( " + str(listid[randommanager]) + " )"
    print(textmessage)
    bot.send_message(userid.id_fleysner, textmessage)
