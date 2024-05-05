#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""

import logging, os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
import baseball_score
import football_score
import volleyball_score
from kbo_rank import fetch_kbo_team_stats_single_line
from kleague import fetch_kfootball_team_stats

TOKEN = os.environ["TOKEN"]

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def baseball(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = baseball_score.get_baseball()
    await update.message.reply_text(msg)


async def football(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = football_score.get_football()
    await update.message.reply_text(msg)


async def all_score(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = all()
    await update.message.reply_text(msg)


async def volleyball(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = volleyball_score.get_volleyball()
    await update.message.reply_text(msg)


async def kbo_rank(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = fetch_kbo_team_stats_single_line()
    await update.message.reply_text(msg)


async def kleague_rank(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = fetch_kfootball_team_stats()
    await update.message.reply_text(msg)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("/baseball /football /volleyball /kbo /kleague")


def all():
    msg = (
        "야구: \n"
        + baseball_score.get_baseball()
        + "\n\n\n"
        + "축구 \n"
        + football_score.get_football()
        + "\n\n\n"
        + "배구 \n"
        + volleyball_score.get_volleyball()
    )
    return msg


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler(("all"), all_score))
    application.add_handler(CommandHandler("baseball", baseball))
    application.add_handler(CommandHandler("football", football))
    application.add_handler(CommandHandler("volleyball", volleyball))
    application.add_handler(CommandHandler("kbo", kbo_rank))
    application.add_handler(CommandHandler("kleague", kleague_rank))

    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
