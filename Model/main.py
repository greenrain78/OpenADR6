# -*- encoding: utf-8 -*-
import logging.config
import os
import unittest

from time import sleep

from src.Engine.Planner import schedule_registration
from src.Controller.Schedule.schedule_manager import MainScheduler
from src.setting_logger import py_log_settings

# 로거 생성
logger = logging.getLogger(__name__)


def get_env_bool(env_name) -> bool:
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

    # # 테스트 코드 실행
    # 에러시 프로그램 종료
    if get_env_bool('IS_RUN_TEST'):
        logger.info('test 코드 실행')
        # 테스트 코드 탐색
        loader = unittest.TestLoader()
        tests = loader.discover('.')
        # 테스트 실행
        testRunner = unittest.runner.TextTestRunner()
        testRunner.run(tests)
    else:
        logger.info('test 코드 미실행')

    # start = time.time()  # 시작 시간 저장

    # 객체 생성
    # testEngine = TestEngine()
    scheduler = MainScheduler()

    # 일정 등록
    schedule_registration(scheduler)


    # 작업 코드
    # print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
    # 임시로
    while True:
        logger.debug('프로그램 실행중')
        sleep(1)
