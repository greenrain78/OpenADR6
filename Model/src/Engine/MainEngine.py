from src.Controller.API.adr_api_client import ADR_API_Client
from src.DB.DB_Adapter import DBAdapter


class MainEngine:

    def __init__(self):
        # DB 데이터 입출력
        self.api = ADR_API_Client()
        self.db = DBAdapter()

    def get_recent_date(self):
        # 장비 데이터 업데이트 확인
        pass

    def ann_run_test(self):
        pass







