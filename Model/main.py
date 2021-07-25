import json
import logging.config
import os
import unittest

from time import sleep

# 로그 생성
with open('loggers.json') as f:
    config = json.load(f)
    print(config)
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)


def get_env_bool(env_name):
    """
    :arg env_name 환경변수 명
    :return true or false
    :raise bool 이 아닌경우 에러 발생
    """
    # 환경변수명에 따라 해당 값 가져오기
    env = os.environ.get(env_name)
    # str 형태를 bool 로 반환
    if env == "True":
        return True
    elif env == "False":
        return False
    # 예외 발생
    elif env is None:
        raise ValueError(f"env var is null : {env}")
    else:
        raise ValueError(f"env vars is not bool : {env}")


# 메인 프로그램 시작
if __name__ == '__main__':

    # 디버그를 사용
    if get_env_bool('IS_DEBUG'):
        logger.debug('this is a debug')
        print(f"running debug mode")

    # 테스트 코드 실행
    # 에러시 프로그램 종료
    if get_env_bool('IS_RUN_TEST'):
        logger.info('test 실행')
        unittest.main()
    else:
        logger.info('test 미실행')

    # 임시로
    while True:
        logger.debug('running')
        sleep(1)


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
