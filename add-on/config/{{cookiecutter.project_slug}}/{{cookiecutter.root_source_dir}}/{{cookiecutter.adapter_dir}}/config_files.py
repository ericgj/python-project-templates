import os.path

from {% if cookiecutter.is_library == 'y' %}..{% endif %}model.config import Config

class ConfigLoadError(BaseException):
    def __init__(self, env: str, config_name: str):
        self.env = env
        self.config_name = config_name

    def __str__(self):
        return f"Unable to find config file for {self.config_name} in environment {self.env}"


def load(env: str) -> Config:
    # TODO: replace with how you load your config from files
    """
    with open(config_file(env, 'some_config_file')) as c:
        return Config(...)
    """
    pass


def config_file(env: str, name: str) -> str:
    path = os.path.join("{{ cookiecutter.config_dir }}", env, name)
    if not os.path.exists(path):
        raise ConfigLoadError(env, name)
    return path
