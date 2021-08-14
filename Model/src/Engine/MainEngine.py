from src.Controller.API.adr_api_client import ADR_API_Client
from src.DB.DB_Adapter import DBAdapter
from src.Engine.DataEngine import DataEngine


class MainEngine:

    def __init__(self):
        # DB 데이터 입출력
        db = DBAdapter()
        self.data_engine = DataEngine(db)
        pass

    def get_recent_date(self):
        # 장비 데이터 업데이트 확인
        pass

    def ann_run_test(self):
        # 장비 리스트 갱신
        self.data_engine.update_eqps()
        # 장비 정보 업데이트
        self.data_engine.update_elec_remove_all()

        self.data_engine.ann_run_test()

        pass







