"""
정상 작동하는지 임시로 구현한 테스트 엔진
드라이버
"""
from datetime import datetime

from src.Controller.API.adr_api_client import ADR_API_Client
from src.Controller.DB.DB_Adapter import DBAdapter


class TestEngine:
    """
    정상 작동하는지 임시로 구현한 테스트 엔진
    맨 위가 최근에 작성한 코드
    """

    def __init__(self):
        # DB 데이터 입출력
        self.adr_api = ADR_API_Client()
        self.db = DBAdapter()

    def db_insert_elec(self):
        data_list = self.adr_api.fetch_elec('ace', 300, 20200309)
        self.db.eqps.insert_list(data_list, 'ace')
        # print(f"TEST ENGINE db_insert_elec: {data_list}")



    def hello(self):
        """
        간단 engine 동작 확인
        """
        print(f"hello {datetime.now()}", flush=True)
