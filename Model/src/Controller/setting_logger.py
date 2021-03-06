import json
import logging.config
from abc import abstractmethod, ABCMeta, ABC

config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s:%(name)s:%(lineno)s (%(levelname)s) %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
        "complex": {
            "format": "[%(asctime)s] %(levelname)s [%(module)s %(name)s :%(lineno)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": "DEBUG",
            "stream": "ext://sys.stdout",
        },
        "warning_file": {
            "class": "logging.FileHandler",
            "filename": "logs/error.log",
            "formatter": "complex",
            "level": "WARNING",
        },
        "all_file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "DEBUG",
            "formatter": "complex",
            "filename": "logs/rotation/all.log",
            "when": "midnight",
            "backupCount": 30,
            "interval": 1,
            "encoding": "utf-8"
        },
        "rotation_file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "INFO",
            "formatter": "complex",
            "filename": "logs/server_info/info.log",
            "when": "midnight",
            "backupCount": 30,
            "interval": 1,
            "encoding": "utf-8"
        },
    },
    "loggers": {
        "": {
            "level": "INFO",
            "handlers": [],
        },
        "__main__": {
            "level": "DEBUG",
            "handlers": ["console", "warning_file", "rotation_file", "all_file"],
            "propagate": False,
        },
        "src": {
            "level": "DEBUG",
            "handlers": ["console", "warning_file", "rotation_file", "all_file"],
            "propagate": False,
        },
        "test": {
            "level": "DEBUG",
            "handlers": ["console", "warning_file", "rotation_file", "all_file"],
            "propagate": False,
        },
        "apscheduler": {
            "level": "INFO",
            "handlers": ["console", "warning_file", "rotation_file", "all_file"],
            "propagate": False,
        },

    },
}


class log_settings:
    log_config = None

    def initialize(self):
        logging.config.dictConfig(self.log_config)


class py_log_settings(log_settings):
    log_config = config

    @classmethod
    def init(cls, debug: bool):

        # 디버그 모드시 로거 변경
        # Todo dict를 복사하기 때문에 변경이 안됨 수정 필수
        if debug is True:
            handlers = cls.log_config.get("handlers")
            console_handler = handlers.get("console")
            console_handler["level"] = "DEBUG"

            loggers = cls.log_config.get("loggers")
            root_loggers = loggers.get("")
            root_loggers["level"] = "DEBUG"
            root_loggers["handlers"] = ["console"]
        # else:
        #     handlers = cls.log_config.get("handlers")
        #     console_handler = handlers.get("console")
        #     console_handler["handlers"] = "INFO"

        cls.initialize(cls)

    def change_config(self, key, *args):
        select = self.log_config
        for arg in args:
            select = select.get(arg)

        pass


def open_log_setting_json():
    """
    json 파일 형식으로 된 logger 설정파일을 읽어와 로거를 설정한다.
    :return:
    """
    with open('loggers.json') as f:
        config_json = json.load(f)
        print("로그 설정")
        print(config)
        logging.config.dictConfig(config_json)
