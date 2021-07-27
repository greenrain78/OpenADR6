from src.Controller.API.adr_api_client import ADR_API_Client
from src.Controller.DB.DB_Adapter import DBAdapter


class MainEngine:

    def __init__(self):
        # DB 데이터 입출력
        self.adr_api = ADR_API_Client()
        self.db = DBAdapter()


    def get_recent_date(self):
        pass








