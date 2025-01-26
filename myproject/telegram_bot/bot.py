from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

# Ваш токен Telegram бота
TOKEN = '7606751888:AAFx0UURURBd6u87yoS8tqLWjsTxGFk1xZ0'  # Замените на ваш токен

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Обрабатывает команду /start."""
#     await update.message.reply_text("Сәлем, бұл Нұргүлдің күйеуі Асқар.")

# def main():
#     """Запускает бота."""
#     # Создаем приложение Telegram бота
#     application = Application.builder().token(TOKEN).build()

    # Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Обрабатывает команду /start."""
        await update.message.reply_text(
            "Сәлем, бұл Нұргүлдің күйеуі Асқар. Мына қараш не істей аламын:\n"
            "/help - Список команд\n"
            "/about - Мен туралы"
        )

    # Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Обрабатывает команду /help."""
        await update.message.reply_text(
            "Вот список доступных команд:\n"
            "/start - Сөйлесейікші\n"
            "/help - Коммандалар тізімі\n"
            "/about - Узнать о боте"
        )

    # Команда /about
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Обрабатывает команду /about."""
        await update.message.reply_text("Мен Азамат пен Жібектің папасымын. Чем могу помочь?")

    # Ответ на текстовые сообщения
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Обрабатывает текстовые сообщения."""
        user_message = update.message.text.lower()

        # Простейшая логика вопросов-ответов
        if "привет" in user_message:
            await update.message.reply_text("Привет! Как ваши дела?")
        elif "как тебя зовут" in user_message:
            await update.message.reply_text("Асқар! 🚀")
        elif "атың кім" in user_message:
            await update.message.reply_text("Я ваш чат-бот! 🚀")
        elif "атын ким" in user_message:
            await update.message.reply_text("Асқар дедім ғо! 🚀")
        elif "погода" in user_message:
            await update.message.reply_text("Погода морозит, лучше дома оставайся")
        elif "нешедесин" in user_message:
            await update.message.reply_text("Шүкір, ересекпін")
        elif "сколько тебе лет" in user_message:
            await update.message.reply_text("Достаточно")
        elif "как дела" in user_message:
            await update.message.reply_text("У меня всё отлично, спасибо! А у вас?")
        elif "как зовут жену" or "айелиннин аты ким" in user_message:
            await update.message.reply_text("Нағашыбайқызы Нургуль")
        else:
            await update.message.reply_text("Бұл сұрақтарға дайын емеспін.")

    # Основная функция запуска бота
def main():
        """Запускает бота."""
        # Создаем приложение Telegram бота
        application = Application.builder().token(TOKEN).build()

        # Добавляем обработчики команд
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("about", about))

        # Обработчик текстовых сообщений
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        # Запускаем бота
        application.run_polling()



