from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    TypeHandler,
    ContextTypes,
    ApplicationHandlerStop,
)

COMMAND_GROUP = 1


async def check_if_chat_is_allowed(
    allowed_chat_id: str, update: Update, context: ContextTypes.DEFAULT_TYPE
):
    if context._chat_id != allowed_chat_id:
        raise ApplicationHandlerStop()


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")


def start_telegram_bot(config):
    token = config["bot_token"]
    allowed_chat_id = config["chat_id"]

    app = ApplicationBuilder().token(token).build()

    app.add_handler(
        TypeHandler(
            Update, lambda *args: check_if_chat_is_allowed(allowed_chat_id, *args)
        )
    )
    app.add_handler(CommandHandler("hello", hello), COMMAND_GROUP)

    app.run_polling()
