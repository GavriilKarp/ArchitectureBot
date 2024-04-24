import telebot
from telebot import types

from architecture_utils.architecture_styles import get_styles
from architecture_utils.file_text import get_text
from architecture_utils.path_creater import get_path
from bot_utils.buttons_creater import create_return_button, create_style_button
from bot_utils.architecture_info_sender import send_style_info

bot = telebot.TeleBot("6850613496:AAEO51Wrs1Yo5F9fv7pXaSQKDZMv8LcBHKU")


@bot.message_handler(commands=["start"])
def greet(message) -> None:
    to_styles_button = types.InlineKeyboardMarkup()
    to_styles_button.add(types.InlineKeyboardButton("К стилям",
                         callback_data="to_styles"))
    bot.send_message(message.chat.id, get_text("greeting"),
                     reply_markup=to_styles_button)


@bot.callback_query_handler(func=lambda callback: True)
def go_to_styles(callback) -> None:
    if callback.data == "to_styles":
        styles_menu = types.InlineKeyboardMarkup()
        for i in range(11):
            create_style_button(styles_menu, i)
        bot.send_message(callback.message.chat.id, get_text("styles_list"),
                         reply_markup=styles_menu, parse_mode="html")
    else:
        send_style_info(callback.data, callback, bot)


bot.polling(none_stop=True)
