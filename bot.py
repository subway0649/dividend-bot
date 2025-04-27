import telegram
from telegram.ext import Updater, CommandHandler
import os

TOKEN = "7584277728:AAHq5Er4cR9AclrnhbP2yPzZzre4xYfKyz4"

def start(update, context):
    update.message.reply_text('안녕하세요! 김영찬님의 배당 관리 봇입니다.')

def dividend(update, context):
    update.message.reply_text('현재 예상 배당금은 0원입니다. (추후 연결 예정)')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('배당금현황', dividend))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
