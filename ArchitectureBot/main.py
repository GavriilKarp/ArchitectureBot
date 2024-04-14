import telebot
from telebot import types

bot = telebot.TeleBot("6850613496:AAEO51Wrs1Yo5F9fv7pXaSQKDZMv8LcBHKU")


def get_styles() -> tuple:
    return (
      "Деревянный Петербург",
      "Петровское барокко",
      "Елизаветинское высокое барокко",
      "Классицизм",
      "Ампир",
      "Эклектика",
      "Модерн",
      "Авангард",
      "Сталинский неоклассицизм",
      "Модернизм",
      "Современная архитектура"
    )


def get_text(line_number: int) -> str:
    with open("text/styles.txt", "r", encoding="utf-8") as file:
        line = file.readlines()[line_number]
        return line


@bot.message_handler(commands=["start"])
def greeting(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("К стилям",
                                          callback_data="to_styles"))
    bot.send_message(message.chat.id, "lorem ipsum", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def go_to_styles(callback):
    if callback.data == "to_styles":
        styles_menu = types.InlineKeyboardMarkup()
        styles_menu.add(types.InlineKeyboardButton(get_styles()[0],
                                                   callback_data="style_1"))
        styles_menu.add(types.InlineKeyboardButton(get_styles()[1],
                                                   callback_data="to_styles"))
        styles_menu.add(types.InlineKeyboardButton(get_styles()[2],
                                                   callback_data="to_styles"))
        styles_menu.add(types.InlineKeyboardButton(get_styles()[3],
                                                   callback_data="to_styles"))
        styles_menu.add(types.InlineKeyboardButton(get_styles()[4],
                                                   callback_data="to_styles"))
        styles_menu.add(types.InlineKeyboardButton(get_styles()[5],
                                                   callback_data="to_styles"))
        styles_menu.add(types.InlineKeyboardButton(get_styles()[6],
                                                   callback_data="to_styles"))
        styles_menu.add(types.InlineKeyboardButton(get_styles()[7],
                                                   callback_data="to_styles"))
        styles_menu.add(types.InlineKeyboardButton(get_styles()[8],
                                                   callback_data="to_styles"))
        styles_menu.add(types.InlineKeyboardButton(get_styles()[9],
                                                   callback_data="to_styles"))
        styles_menu.add(types.InlineKeyboardButton(get_styles()[10],
                                                   callback_data="to_styles"))
        bot.send_message(callback.message.chat.id,
                         "Выбор стилей", reply_markup=styles_menu)
    elif callback.data == "style_1":
        bot.send_message(callback.message.chat.id, get_text(0))


bot.polling(none_stop=True)
