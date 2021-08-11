import time
from logging import getLogger


class CheckTimeDecorator:

    def __init__(self, f):
        self.func = f

    def __call__(self, *args, **kwargs):
        logger = getLogger(__name__)
        start = time.time()  # 시작 시간 저장

        self.func(self, *args, **kwargs)
        logger.info(f"{self.func.__name__} - {time.time() - start}")


def check_time_decorator(func):
    def func_wrapper(*args, **kwargs):
        logger = getLogger(f"{func.__module__}.timer")
        start = time.time()  # 시작 시간 저장

        func(*args, **kwargs)
        logger.info(f"{func.__name__} - {time.time() - start}")

    return func_wrapper
