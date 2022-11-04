from telebot import *

from projectfiles.functionsforallusers import *
from projectfiles.functionsforadmin import *
# Токен для связи с ботом
bot = telebot.TeleBot(botkey)

# Командa start
@bot.message_handler(commands = ['start'])
def start(message):
    # Создаём кнопочки и "плитку"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Кнопки для клиентов
    btn1 = types.KeyboardButton("⏰Режим работы⏰")
    btn2 = types.KeyboardButton("🖥Наши социальные сети🖥")
    btn3 = types.KeyboardButton("📝Записаться📝")
    btn5 = types.KeyboardButton("📲Ссылки с отзывами📲")
    # Кнопки для администратора
    btn4 = types.KeyboardButton("☎Отредактировать call-центр☎")
    btn6 = types.KeyboardButton("Выяснить id пользователя")
    # Общие кнопки


    # Определяем тип аккаунта
    id = message.chat.id
    match id:
        # Аккаунта администратора
        case userid.id_6080:
            markup.add(btn1, btn2, btn3, btn4, btn5)
        # Аккаунты работников
        case userid.id_fleysner:
            markup.add(btn5, btn4)
        # Аккаунт клиента
        case _:
            markup.add(btn1, btn2, btn3, btn6)

    # Отравляем первое приветственное сообщение
    textmessage = "Привет, {0.first_name}!\nЯ бот автотехцента ⚙GlessGroup⚙\nЧем я могу вам помочь?"
    bot.send_message(message.chat.id,
                     text = textmessage.format(message.from_user), reply_markup=markup)

# Команды по кнопкам в чате
@bot.message_handler(content_types= ['text'])
def textmessage(message):
    match(message.text):
        # Кнопки для клиентов
        case "⏰Режим работы⏰":
            timeworking(message, bot)
        case "🖥Наши социальные сети🖥":
            socialntworks(message, bot)
        case "📝Записаться📝":
            print("Нажали на кнопку: 📝Записаться📝")
        case "📲Ссылки с отзывами📲":
            print("Нажали на кнопку: 📲Ссылки с отзывами📲")
        case "Выяснить id пользователя":
            youid(message, bot)
        # Кнопки для администратора
        case "☎Отредактировать call-центр☎":
            changecallcener(message, bot)
        case _:
            print(message.text)
            senderrormessage(message, bot)

# Запустили постоянный опрос бота Telegram
bot.polling(none_stop=True, interval=0)