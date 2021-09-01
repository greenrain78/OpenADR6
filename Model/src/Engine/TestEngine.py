"""
정상 작동하는지 임시로 구현한 테스트 엔진
드라이버
"""
from datetime import datetime

from src.Controller.API.adr_api_client import ADR_API_Client
from src.Controller.Schedule.schedule_manager import add_schedule


class TestEngine:
    """
    정상 작동하는지 임시로 구현한 테스트 엔진
    맨 위가 최근에 작성한 코드
    """

    # print("create TestEngine")

    def __init__(self):
        # DB 데이터 입출력
        self.adr_api = ADR_API_Client()
        # self.db = DBAdapter()
        # print("init TestEngine")

    def db_insert_elec(self):
        data_list = self.adr_api.fetch_elec('ace', 300, 20200309)
        self.db.eqps.insert_list(data_list, 'ace')
        # print(f"TEST ENGINE db_insert_elec: {data_list}")

    # @add_schedule(second=34)
    def print_hello(self):
        print(f"hello world,  -  {datetime.today()}")


