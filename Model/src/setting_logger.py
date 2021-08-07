import json
import logging.config
from abc import abstractmethod, ABCMeta, ABC

config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s:%(module)s:%(lineno)s (%(levelname)s) %(message)s",
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
            "level": "ERROR",
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
        "root": {
            "level": "INFO",
            # 발견 못한 로그도 일단은 출력하도록 설정
            "handlers": ["console", ],
        },
        "__main__": {
            "level": "DEBUG",
            "handlers": ["console", "warning_file", "rotation_file", "all_file", ],
            "propagate": False,
        },
        "Controller": {
            "level": "DEBUG",
            "handlers": ["console", "warning_file", "rotation_file", "all_file", ],
            "propagate": False,
        },
        "Engine": {
            "level": "DEBUG",
            "handlers": ["console", "warning_file", "rotation_file", "all_file", ],
            "propagate": False,
        },
        "sqlalchemy": {
            "level": "DEBUG",
            "handlers": ["warning_file", "rotation_file", "all_file", ],
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
        if debug is True:
            cls.change_debug_mode(cls)
        else:
            cls.change_server_mode(cls)
        cls.initialize(cls)

    def change_debug_mode(self):
        """
        디버그 모드시 설정
        """
        print("log debug mode")
        # 기본 콘솔 핸들러가 DEBUG 까지 출력되도록 설정
        handlers = self.log_config.get("handlers")
        console_handler = handlers.get("console")
        console_handler["level"] = "DEBUG"

    def change_server_mode(self):
        """
        서버 모드시 설정
        디폴트 설정이긴 하나 재확인
        """
        print("log server mode")
        # 기본 콘솔 핸들러가 INFO 까지 출력되도록 설정
        handlers = self.log_config.get("handlers")
        console_handler = handlers.get("console")
        console_handler["level"] = "INFO"


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
