from src.Controller.API.adr_api_client import ADR_API_Client
from src.DB.DB_Adapter import DBAdapter
from src.Engine.DataEngine import DataEngine


class MainEngine:

    def __init__(self, data_engine: DataEngine):
        # DB 데이터 입출력
        self.data_engine = data_engine

    def ann_run_test(self):
        # 장비 리스트 갱신
        self.data_engine.update_eqps()
        # 장비 정보 업데이트
        self.data_engine.update_elec_remove_all()

        # 장비 데이터 가져오기
        eqps_list = self.data_engine.get_all_eqps()
        eqps_obj = eqps_list[0]
        print(f"MainEngine: eqps_obj: {eqps_obj}")

        # 데이터 검색
        data = self.data_engine.get_ann_data(eqps_obj)
        print(f"MainEngine: {data}")
