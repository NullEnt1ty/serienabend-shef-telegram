import os
import os.path
import json
from pathlib import Path

data_dir = Path.home() / ".local" / "share" / "serienabend_shef_telegram"
config_file = data_dir / "config.json"


def load_config():
    if not os.path.exists(config_file):
        return None

    if not os.path.isfile(config_file):
        raise Exception(
            f"Path to config exists but does not point to a file: {config_file}"
        )

    try:
        with open(config_file, "r", encoding="utf-8") as file:
            config = json.load(file)
    except:
        raise Exception("Could not read config file")

    ensure_config_is_valid(config)

    return config


def save_config(config):
    ensure_data_dir_exists()

    flags = os.O_CREAT | os.O_WRONLY  # Create file and open in write mode
    mode = 0o600  # Only owner can read and write the file

    try:
        with open(os.open(config_file, flags, mode), "w", encoding="utf-8") as file:
            json.dump(config, file, indent=4)
    except:
        raise Exception("Could not write config file")


def ensure_data_dir_exists():
    if not data_dir.exists():
        data_dir.mkdir(parents=True)


def ensure_config_is_valid(config):
    required_keys = ["bot_token", "chat_id"]

    if config is None:
        raise Exception("Invalid config: Config is None")

    if not isinstance(config, dict):
        raise Exception("Invalid config: Config is not a dictionary")

    for key in required_keys:
        if not key in config.keys():
            raise Exception(f"Invalid config: Missing key '{key}'")
