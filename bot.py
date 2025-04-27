from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '8188059521:AAEmmxjGCJEmyomyBhiMMwrCapsEh3sBknE'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Welcome to the dividend management bot.')

async def dividend(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Current expected dividend amount is 0 KRW. (to be connected later)')

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("dividend", dividend))

    app.run_polling()

if __name__ == '__main__':
    main()

