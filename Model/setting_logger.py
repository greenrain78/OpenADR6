import json
import logging.config

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
            "level": "ERROR",
        },
        "rotation_file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "DEBUG",
            "formatter": "complex",
            "filename":  "logs/rotation.log",
            "when": "midnight",
            "backupCount": 30,
            "interval": 1,
            "encoding": "utf-8"
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "warning_file", "rotation_file"],
    },
}


def init_log_settings(debug: bool = False):
    """
    로그 설정
    """
    # 로그 생성
    open_log_settings_py(debug)


def open_log_settings_py(debug: bool):
    """
    python 에서 로그 설정파일을 조작
    """
    # 디버그 모드시 로거 변경
    if debug is True:
        pass
    else:
        pass

    logging.config.dictConfig(config)


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
