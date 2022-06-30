import logging
from getpass import getpass

from .config import save_config, config_file


def setup():
    bot_token = ""
    chat_id = ""

    while bot_token == "":
        bot_token = getpass("Please enter a token for your Telegram bot: ")

    while chat_id == "":
        chat_id = input(
            "Please enter the ID of the chat which should be allowed to communicate with the bot: "
        )

    config = {
        "bot_token": bot_token,
        "chat_id": int(chat_id),
    }

    save_config(config)
    logging.info(f"Saved config to '{config_file}'")
