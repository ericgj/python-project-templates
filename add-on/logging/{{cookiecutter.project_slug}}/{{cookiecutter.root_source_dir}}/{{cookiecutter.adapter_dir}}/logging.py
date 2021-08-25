import logging.config
import logging

from model.config import Config


def init(config: Config) -> logging.Logger:
    logging.config.dictConfig(config.logging)
    return get(config)


def get(config: Config) -> logging.Logger:
    return logging.getLogger(config.environment)

