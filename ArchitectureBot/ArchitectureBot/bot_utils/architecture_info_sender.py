import telebot

from architecture_utils.file_text import get_text
from architecture_utils.path_creater import get_path
from .buttons_creater import create_return_button


def send_style_info(style_name: str, callback, bot) -> None:
    bot.send_photo(callback.message.chat.id, open(get_path(style_name),
                                                  "rb"),
                   caption=get_text(style_name),
                   parse_mode="html",
                   reply_markup=create_return_button())
