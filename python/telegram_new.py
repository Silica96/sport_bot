import telegram
from telegram.ext import Updater
import baseball_score
import asyncio

token ="5952714037:AAG5LOVNAyWpWmKSQtbEiChQan3d5_NaiSE"
bot = telegram.Bot(token)
queue = asyncio.Queue()

updater = Updater(bot=bot, update_queue=queue)


async def handler(update):
    async with updater:
        updater.start_polling()

    _id=update.message.chat.id
    user_text = update.message.text

    if user_text.startswith("/") == False:
        return

    if "야구" in user_text:
        bot.send_message(chat_id=_id, text=baseball_score.get_baseball())

handler(updater)