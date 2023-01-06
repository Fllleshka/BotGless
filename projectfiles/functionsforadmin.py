from projectfiles.dates import *
from telebot import *
import requests
import datetime

# Функция редактирования call-центра
def changecallcener(message, bot):
    today = datetime.datetime.today()
    todaytime = today.strftime("%H:%M:%S")
    firstname = message.chat.first_name
    lastname = message.chat.last_name
    print(todaytime, "[", firstname, lastname, "] нажал на кнопку [☎Отредактировать call-центр☎]")
    index = 0
    status = []
    markup = telebot.types.InlineKeyboardMarkup()
    for i in namesmanagers:
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
    id_message = bot.send_message(message.chat.id, "Менеджеры онлайн", reply_markup = markup)
    print(status)

    # Фунция отбработки нажания на кнопку
    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        match(call.data):
            case class_namesmanagers.first:
                statusget = str(requests.get(urlapi + numbermanagers[0] + '/agent', headers=headers).text)[1:-1]
                print("Статус менеджера", class_namesmanagers.first, '(', statusget, ") инвертируем")
                test_for_callback = changestatus(statusget, numbermanagers[0])
                bot.answer_callback_query(call.id, test_for_callback)
                statusget = str(requests.get(urlapi + numbermanagers[0] + '/agent', headers=headers).text)[1:-1]
                logger(firstname, lastname, class_namesmanagers.first, statusget)
            case class_namesmanagers.second:
                statusget = str(requests.get(urlapi + numbermanagers[1] + '/agent', headers=headers).text)[1:-1]
                print("Статус менеджера", class_namesmanagers.second, '(', statusget, ") инвертируем")
                test_for_callback = changestatus(statusget, numbermanagers[1])
                bot.answer_callback_query(call.id, test_for_callback)
                statusget = str(requests.get(urlapi + numbermanagers[1] + '/agent', headers=headers).text)[1:-1]
                logger(firstname, lastname, class_namesmanagers.second, statusget)
            case class_namesmanagers.third:
                statusget = str(requests.get(urlapi + numbermanagers[2] + '/agent', headers=headers).text)[1:-1]
                print("Статус менеджера", class_namesmanagers.third, '(', statusget, ") инвертируем")
                test_for_callback = changestatus(statusget, numbermanagers[2])
                bot.answer_callback_query(call.id, test_for_callback)
                statusget = str(requests.get(urlapi + numbermanagers[2] + '/agent', headers=headers).text)[1:-1]
                logger(firstname, lastname, class_namesmanagers.third, statusget)
            case class_namesmanagers.fourth:
                statusget = str(requests.get(urlapi + numbermanagers[3] + '/agent', headers=headers).text)[1:-1]
                print("Статус менеджера", class_namesmanagers.fourth, '(', statusget, ") инвертируем")
                test_for_callback = changestatus(statusget, numbermanagers[3])
                bot.answer_callback_query(call.id, test_for_callback)
                statusget = str(requests.get(urlapi + numbermanagers[3] + '/agent', headers=headers).text)[1:-1]
                logger(firstname, lastname, class_namesmanagers.fourth, statusget)
            case _:
                print("На кнопочку справа!")
                bot.answer_callback_query(call.id, "На кнопочку справа!")

# Функция логгирования действий
def logger(firstname, lastname, name, status):

    print("\tНомер строки: ")
    print("\tВремя действия: ")
    print("\tКто:\t", firstname, lastname)
    print("\tМенеджер:\t", name)
    print("\tСтатус:\t", status)

# Функция инверсии статуса
def changestatus(statusnow, numbermanager):
    if (statusnow == "OFFLINE"):
        text_for_callback = "Статус " + numbermanager + " изменён на ONLINE"
        urlforapi = urlapi + numbermanager + '/agent'
        result = requests.put(urlforapi, params = paramsonline, headers = headers)
    else:
        text_for_callback = "Статус " + numbermanager + " изменён на OFFLINE"
        urlforapi = urlapi + numbermanager + '/agent'
        result = requests.put(urlforapi, params = paramoffline, headers = headers)
    return text_for_callback