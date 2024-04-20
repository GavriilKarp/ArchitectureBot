import telebot
from telebot import types

from architecture_utils.architecture_styles import get_styles


def create_style_button(markup, button_number: int) -> None:
    data = "style_" + str(button_number + 1)
    markup.add(types.InlineKeyboardButton(get_styles()[button_number],
               callback_data=data))


def create_return_button():
    return_button = types.InlineKeyboardMarkup()
    return_button.add(types.InlineKeyboardButton("◀️ Назад  ",
                                                 callback_data="to_styles"))
    return return_button
