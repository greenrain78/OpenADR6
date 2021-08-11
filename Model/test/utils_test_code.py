import time
from logging import getLogger


def datetime_decorator(func):
    def decorated():
        logger = getLogger(__name__)
        start = time.time()  # 시작 시간 저장

        func()
        logger.info(f"test_update_elec - {time.time() - start}")

    return decorated


class CheckTimeDecorator:

    def __init__(self, f):
        self.func = f

    def __call__(self, *args, **kwargs):
        logger = getLogger(__name__)
        start = time.time()  # 시작 시간 저장

        self.func()
        logger.info(f"{self.func.__name__ } - {time.time() - start}")
