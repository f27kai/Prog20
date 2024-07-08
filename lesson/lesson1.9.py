import telebot
from telebot import types


bot = telebot.TeleBot("7307740028:AAElo6EN6MJ5e8MXFKDM9h_8R7zRD1sW7XM")

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Кунфу панда", url="https://kadikama.com/10273-2024-kung-fu-panda-4.html")
    btn2 = types.InlineKeyboardButton("Золушка", url="https://filmix.biz/films/drama/108016-zolushka_2015.html")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Кош келипсиз", reply_markup=markup)

@bot.message_handler(content_types = ['text'])
def get_info(message):
    if message.text == "Hello":
        bot.send_message(
            message.chat.id,
            "Salam"
        )
    elif message.text == "Привет":
        bot.send_message(message.chat.id, "Пока")
    # else:
    #     bot.send_message(message.chat.id, "Your are beautiful")


@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.send_message(message.chat.id, "Your photo very good")


@bot.message_handler(commands=['help'])
def help_button(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton("Test")
    btn2 = types.KeyboardButton('Car')
    btn3 = types.KeyboardButton('Apple')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Hi", reply_markup=markup)
#
# def on_click(message):
#     if message.text == "Car":
#         bot.send_message(message.chat.id, "UUUUU")



bot.polling(none_stop=True)