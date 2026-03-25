import random
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- Настройка логирования ---
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- Функция генерации фразы ---
def generate_phrase() -> str:
    """Генерирует случайный процент и возвращает итоговую фразу."""
    percent = random.randint(0, 100)
    main_text = f"Сегодня Сергей Хохлов толстожопый на {percent}%"

    # Определяем приписку в зависимости от процента
    if percent > 90:
        footer = "Сергей поздравляю, вы официально толстожопый"
    elif percent > 80:
        footer = "толстожоп толстожопыч"
    elif percent > 70:
        footer = "жопа как орех так и просится на грех"
    elif percent > 60:
        footer = "присядь пожалуйста"
    elif percent > 50:
        footer = "ну вы толстожопик:3"
    elif percent > 40:
        footer = "жопа уже пуленепробиваемая"
    elif percent > 30:
        footer = "ну уже ниче жопка такая"
    elif percent > 20:
        footer = "жопа толстеет"
    elif percent > 10:
        footer = "чуть чуть тостожопый"
    else:
        footer = "ну вообще не толстожопый"  # для процентов <= 10 приписки нет

    # Возвращаем полное сообщение
    if footer:
        return f"{main_text}\n\n{footer}"
    else:
        return main_text

# --- Обработчики команд ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Ответ на команду /start."""
    await update.message.reply_text(
        "Привет! Я бот, который оценивает толщину жопы Сергея Хохлова.\n"
        "Используй команду /random, чтобы получить случайный результат."
    )

async def random_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Генерация случайной фразы по команде /random."""
    phrase = generate_phrase()
    await update.message.reply_text(phrase)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработка обычных текстовых сообщений (не команд)."""
    phrase = generate_phrase()
    await update.message.reply_text(phrase)

# --- Точка входа ---
def main() -> None:
    # Замените 'YOUR_TOKEN' на реальный токен вашего бота
    TOKEN = "8699989228:AAH3O66Z-gHwkDjundfppRJ9Qf9Ftl_gWYQ"

    # Создаём приложение
    application = Application.builder().token(TOKEN).build()

    # Регистрируем команды
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("random", random_command))

    # Реагируем на любые текстовые сообщения (кроме команд)
    #application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
