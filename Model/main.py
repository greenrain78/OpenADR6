# -*- encoding: utf-8 -*-
import logging.config
import os
import unittest

from time import sleep

from settings import IS_MAIN_RUNNING
from src.Controller.env_import import get_env_bool
from src.Controller.run_test_code import run_tests
from src.Engine.MainEngine import MainEngine
from src.Engine.Planner import schedule_registration
from src.Controller.Schedule.schedule_manager import MainScheduler
from src.setting_logger import py_log_settings

# 로거 생성
logger = logging.getLogger(__name__)

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
        # 테스트 코드 실행
        run_tests()
    else:
        logger.info('test 코드 미실행')

    # start = time.time()  # 시작 시간 저장

    # 객체 생성
    main_engine = MainEngine()
    # scheduler = MainScheduler()
    #
    # # 일정 등록
    # schedule_registration(scheduler)

    # logger.info(f"임시 데이터 추가")
    # main_engine.ann_run_test()

    # 작업 코드
    main_engine.dev_run()
    # print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
    # 임시로
    while IS_MAIN_RUNNING:
        logger.debug('프로그램 실행중')
        sleep(1)
