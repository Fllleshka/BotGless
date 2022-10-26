from telebot import *

from projectfiles.dates import *
from projectfiles.functionsforallusers import *

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
    # Кнопки для администратора
    btn4 = types.KeyboardButton("☎Отредактировать call-центр☎")
    # Общие кнопки
    btn5 = types.KeyboardButton("📲Ссылки с отзывами📲")

    # Определяем тип аккаунта
    id = message.chat.id
    match id:
        # Аккаунта администратора
        case userid.id_6080:
            markup.add(btn1, btn2, btn3, btn4, btn5)
        # Аккаунт клиента
        case _:
            markup.add(btn1, btn2, btn3)

    # От
    textmessage = "Привет, {0.first_name}!\nЯ бот автотехцента ⚙GlessGroup⚙\nЧем я могу вам помочь?"
    bot.send_message(message.chat.id,
                     text = textmessage.format(message.from_user), reply_markup=markup)

# Команды по кнопкам в чате
@bot.message_handler(content_types= ['text'])
def textmessage(message):
    match(message.text):
        case "⏰Режим работы⏰":
            timeworking(message, bot)
        case "🖥Наши социальные сети🖥":
            socialntworks(message, bot)
        case "📝Записаться📝":
            print("Нажали на кнопку: 📝Записаться📝")
        case "☎Отредактировать call-центр☎":
            print("Нажали на кнопку: ☎Отредактировать call-центр☎")
        case "📲Ссылки с отзывами📲":
            print("Нажали на кнопку: 📲Ссылки с отзывами📲")
        case _:
            print(message.text)
            senderrormessage(message.text, bot)

# Запустили постоянный опрос бота Telegram
bot.polling(none_stop=True, interval=0)