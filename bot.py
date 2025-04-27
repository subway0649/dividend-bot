from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = "7584277728:AAHg5Er4cR9AcrlnhbP2yPzZzre4xYfKYz4"  # 네가 사용한 토큰 번호

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('안녕하세요! 김영찬님의 배당 관리 봇입니다.')

async def dividend(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('현재 예상 배당금은 0원입니다. (추후 연결 예정)')

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("dividend", dividend))  # 명령어 영어로 변경

    application.run_polling()

if __name__ == '__main__':
    main()
