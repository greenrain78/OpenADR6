# -*- encoding: utf-8 -*-
import logging.config
import os
import time
import unittest

from time import sleep

from src.Engine.TestEngine import TestEngine
from src.setting_logger import py_log_settings

# 로거 생성
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
        # 로그 설정
        py_log_settings.init(debug=True)
        logger.info('로그 정상 동작')
        print(f"디버그 true로 실행")
    else:
        py_log_settings.init(debug=False)
        logger.info('로그 정상 동작')
        print(f"디버그 false로 실행")

    # 테스트 코드 실행
    # 에러시 프로그램 종료
    if get_env_bool('IS_RUN_TEST'):
        logger.info('test 코드 실행')
        unittest.main()
    else:
        logger.info('test 코드 미실행')

    start = time.time()  # 시작 시간 저장

    # 객체 생성
    testEngine = TestEngine()
    # testEngine.db_connect()
    # testEngine.api_connect_eqps()
    # testEngine.db_insert()
    # testEngine.db_select()
    # testEngine.db_insert_controller()
    # testEngine.db_fetch_insert()
    # testEngine.api_controller_elec()

    # 작업 코드
    testEngine.db_insert_elec()
    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
    # 임시로
    while True:
        logger.debug('프로그램 실행중')
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
