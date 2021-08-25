import json
import os.path

from model.config import Config

class ConfigLoadError(BaseException):
    def __init__(self, env: str, config_name: str):
        self.env = env
        self.config_name = config_name

    def __str__(self):
        return f"Unable to find config file for {self.config_name} in environment {self.env}"


def load(env: str) -> Config:
    with open(config_file(env, "logging.json")) as logging_config_file:
        return Config(
            environment = env,
            logging = dict(json.load(logging_config_file)),
        )
    pass


def config_file(env: str, name: str) -> str:
    path = os.path.join("{{ cookiecutter.config_dir }}", env, name)
    if not os.path.exists(path):
        raise ConfigLoadError(env, name)
    return path
