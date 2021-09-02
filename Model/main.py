# -*- encoding: utf-8 -*-
import logging.config
import time
from time import sleep

from settings import IS_MAIN_RUNNING, IS_DEBUG, IS_RUN_TEST
from src.Controller.run_test_code import run_tests
from src.Predict.Planner import PlanerScheduler
from src.Controller.setting_logger import py_log_settings

# 로거 생성
logger = logging.getLogger(__name__)

# 메인 프로그램 시작
if __name__ == '__main__':
    # 환경 변수 가져오기

    # 디버그를 사용
    if IS_DEBUG:
        # 로그 설정
        py_log_settings.init(debug=True)
        logger.info('로그 정상 동작: 디버그 on')
        print(f"디버그 true로 실행")
    else:
        py_log_settings.init(debug=False)
        logger.info('로그 정상 동작: 디버그 off')
        print(f"디버그 false로 실행")

    # 테스트 코드 실행
    # 에러시 프로그램 종료
    if IS_RUN_TEST:
        logger.info('test 코드 실행')
        # 테스트 코드 실행
        run_tests()
    else:
        logger.info('test 코드 미실행')

    ############################################################################################

    start = time.time()  # 시작 시간 저장
    # 스케줄러 생성
    scheduler = PlanerScheduler()
    scheduler.schedule_registration()
    scheduler.run()

    ############################################################################################

    logger.info(f'main 설정 시간 {time.time() - start}')
    # 임시로
    while IS_MAIN_RUNNING:
        # if IS_DEBUG:
        logger.debug('프로그램 실행중')
        sleep(10)
