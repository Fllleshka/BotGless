from projectfiles.dates import *
from telebot import *
import requests

#Функция редактирования call-центра
def changecallcener(message, bot):
    print(message.chat.first_name, message.chat.last_name, "Нажал на кнопку [☎Отредактировать call-центр☎]")
    index = 0
    status = []
    markup = telebot.types.InlineKeyboardMarkup()
    for i in namesmanagers:
        # Получаем инфорацию о статусе менеджеров call-центра
        print("Проверка статуса: ", namesmanagers[index])
        statusget = requests.get(urlapi + numbermanagers[index] + '/agent', headers=headers)
        # Добавляем статус каждого менеджера в список
        status.append(str(statusget.text)[1:-1])
        # Создаём кнопку имени менеджера
        buttonname = types.InlineKeyboardButton(namesmanagers[index], callback_data = "123")
        # Создаём кнопку статуса менеджера
        buttonstatus = types.InlineKeyboardButton(text = status[index], callback_data = namesmanagers[index])
        # Добавляем кнопки в меню
        markup.add(buttonname, buttonstatus)
        index += 1
    bot.send_message(message.chat.id, "Менеджеры онлайн", reply_markup = markup)
    print(status)

    # Фунция отбработки нажания на кнопку
    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        match(call.data):
            case class_namesmanagers.first:
                statusget = str(requests.get(urlapi + numbermanagers[0] + '/agent', headers=headers).text)[1:-1]
                print("Статус менеджера", class_namesmanagers.first, '(', statusget, ") инвертируем")
                if (statusget == "OFFLINE"):
                    print("Со статуса OFFLINE меняем на ONLINE")
                    test_for_callback = "Статус " + numbermanagers[0] + " изменён на ONLINE"
                    result = requests.get(urlapi + numbermanagers[0] + '/agent', params = paramonline, headers = headers)
                    print("\t\t\t\t", result)
                else:
                    print("Со статуса ONLINE меняем на OFFLINE")
                    test_for_callback = "Статус " + numbermanagers[0] + " изменён на OFFLINE"
                    result = requests.get(urlapi + numbermanagers[0] + '/agent', params = paramoffline, headers = headers)
                    print("\t\t\t\t", result)
                bot.answer_callback_query(call.id, test_for_callback)
            case class_namesmanagers.second:
                print("Менеджер 2")
                bot.answer_callback_query(call.id, "Менеджер 2")
            case class_namesmanagers.third:
                print("Менеджер 3")
                bot.answer_callback_query(call.id, "Менеджер 3")
            case class_namesmanagers.fourth:
                print("Менеджер 4")
                bot.answer_callback_query(call.id, "Менеджер 4")
            case _:
                print("На кнопочку справа!")
                bot.answer_callback_query(call.id, "На кнопочку справа!")