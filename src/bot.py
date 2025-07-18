"""

MADE BY Usanin Andrey a.k.a. Aqamaru
         TG: @NightsForever
            VK: @Aqamaru

"""

import keyboards

from telebot import TeleBot
from telebot.types import Message
from text import Text, Buttons
from main import cfg
from database import DB

cfg.read("config.ini")

BOT = TeleBot(cfg.get("settings", "tg_token"))

@BOT.message_handler(commands = ['start'])
def on_start(msg: Message) -> None:
    pass


def start_bot() -> None:
    BOT.enable_save_next_step_handlers(delay = 2)
    BOT.load_next_step_handlers()
    BOT.infinity_polling()
