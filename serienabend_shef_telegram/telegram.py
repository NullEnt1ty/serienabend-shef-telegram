import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    TypeHandler,
    ContextTypes,
    ApplicationHandlerStop,
)

from .serienabend_shef import get_next_chef
from .exceptions import SerienabendShefError

COMMAND_GROUP = 1


async def check_if_chat_is_allowed(
    allowed_chat_id: str, update: Update, context: ContextTypes.DEFAULT_TYPE
):
    if context._chat_id != allowed_chat_id:
        logging.debug(f"Ignoring update from chat ID {context._chat_id}")
        raise ApplicationHandlerStop()


async def command_callback_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")


async def job_callback_announce_next_chef(context: ContextTypes.DEFAULT_TYPE):
    try:
        next_chef = get_next_chef()
        next_chef_name = next_chef["name"]

        await context.bot.send_message(
            context._chat_id, f"{next_chef_name} ist nächste Woche mit Kochen dran."
        )
    except SerienabendShefError as error:
        await context.bot.send_message(
            context._chat_id,
            f"Fehler beim Ermitteln des nächsten Kochs: {error.command_error}",
        )


def start_telegram_bot(config):
    token = config["bot_token"]
    allowed_chat_id = config["chat_id"]

    app = ApplicationBuilder().token(token).build()

    app.add_handler(
        TypeHandler(
            Update, lambda *args: check_if_chat_is_allowed(allowed_chat_id, *args)
        )
    )
    app.add_handler(CommandHandler("hello", command_callback_hello), COMMAND_GROUP)

    # TODO: Set correct date and time
    # app.job_queue.run_custom(
    #     job_callback_announce_next_chef,
    #     {"trigger": "cron", "second": "*/10"},
    #     chat_id=allowed_chat_id,
    # )

    app.run_polling()
