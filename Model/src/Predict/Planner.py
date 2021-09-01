from typing import List

from settings import IS_DEBUG, IS_RUN_SERVER
from src.Controller.Schedule.schedule_manager import MainScheduler
from src.Engine.DataEngine import DataEngine
from src.Engine.MainEngine import MainEngine
from src.Engine.TestEngine import TestEngine


class PlanerScheduler:

    def __init__(self):
        # 객체 생성
        self.test_engine = TestEngine()
        self.data_engine = DataEngine()
        self.main_engine = MainEngine(self.data_engine)
        self.scheduler = MainScheduler('Main')

    def schedule_registration(self):
        """
        필요한 일정들을 등록
        """
        # 예시) 매 0초에 hello 출력
        self.scheduler.create_job(test_hello, "ex hello", second=0)

        if IS_DEBUG:
            # 테스트를 위한 8초에 hello 출력
            self.scheduler.create_job(self.test_engine.print_hello, "test hello 8", second=8)

        if IS_RUN_SERVER:
            # eqps 업데이트
            self.scheduler.create_job(self.data_engine.update_eqps, minute=0)
            # elec 업데이트
            self.scheduler.create_job(self.data_engine.update_elec, minute=0)
            # 임시 예측 알고리즘

    def run(self):
        self.scheduler.run()


def test_hello():
    # 안녕
    print("hello")

#
# # test_engine = TestEngine()
#
#
# def schedule_registration(scheduler: MainScheduler):
#     """
#     필요한 일정들을 등록
#     :return:
#     """
#     # 필요 객체 생성
#     main_engine = MainEngine()
#
#     # 예시) 매 0초에 hello 출력
#     # scheduler.create_job(test_engine.print_hello, "test hello 8", second=0)
#
#
# # 간단하게 리스트
# def schedule_registration_list() -> List[dict]:
#     return [
#         {
#             'func': test_hello,
#             'id': 'test_hello',
#             'args': {
#                 'second': 0
#             }
#         },
#     ]
#
#
# schedule_list = [
#     {
#         'func': test_hello,
#         'id': 'test_hello',
#         'args': {
#             'second': 0
#         }
#     },
# ]
