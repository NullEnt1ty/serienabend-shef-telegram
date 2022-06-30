import logging
import sys

from .config import load_config
from .setup import setup

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

config = load_config()

if config is None:
    logging.info("No config found. Entering setup mode ...")
    setup()
    sys.exit(0)
