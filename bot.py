from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

# ✨ Текст поздравления
def congratulate(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    today = datetime.date.today()

    if today.month == 6 and today.day == 1:
        message = (
            f"Привет, {user.first_name or 'друг'}! 👋\n\n"
            "🎉 С Днём защиты детей!\n"
            "Хоть тебе уже 19, но внутри мы все дети — весёлые, свободные, мечтающие.\n\n"
            "🌟 Желаю тебе светлых мыслей, добрых людей рядом, крепких нервов и удачи во всех делах!\n"
            "💫 Пусть мечты сбываются, а жизнь приносит радость каждый день.\n\n"
            "И помни — ТЫ ОЧЕНЬ КЛАССНЫЙ! 🔥"
        )
    else:
        message = (
            "Сегодня не 1 июня, но всё равно:\n"
            "Ты классный(ая)! 😊 И пусть каждый день будет как праздник!"
        )

    update.message.reply_text(message)

# 🔧 Запуск бота
def main():
    # Замените 'YOUR_TOKEN' на токен вашего бота
    updater = Updater("8087227602:AAGiCg_8QBiYoSuArc5FUj9XTYuDfV8tcIo", use_context=True)
    dp = updater.dispatcher

    # Команда /start
    dp.add_handler(CommandHandler("start", congratulate))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
