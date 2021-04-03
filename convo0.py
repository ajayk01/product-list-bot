#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)



def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    print(update.message.text)
    reply=scrape(update.message.text)
    update.message.reply_text(reply)


def main():
   
    updater = Updater("1361918535:AAGcpr0wUVqQwogVxSEdx8guUV3Mle57dmE", use_context=True)

    
    dp = updater.dispatcher

    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

   
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()