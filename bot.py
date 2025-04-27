from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os

TOKEN = "8188059521:AAEmmxjGCJEmyomyBhiMMwrCapsEh3sBknE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! This is your Dividend Management Bot.')

async def dividend(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Current estimated dividends are 0 won. (To be updated)')

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('dividend_status', dividend))  # 영어 명령어로 변경

    app.run_polling()

if __name__ == '__main__':
    main()
