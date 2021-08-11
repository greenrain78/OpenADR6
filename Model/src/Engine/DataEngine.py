import time
from datetime import datetime, timedelta
from logging import getLogger

from settings import siteId_list, TEST_TIME
from src.Controller.API.adr_api_client import ADR_API_Client
from src.DB.DB_Adapter import DBAdapter
from src.DB.model.EquipInfo import equipments_info
from src.DB.model.PowerInfo import power_info

logger = getLogger(__name__)


class DataEngine:

    def __init__(self, db: DBAdapter):
        # DB 데이터 입출력
        self.api = ADR_API_Client()
        self.db = db

    def update_eqps(self):
        # 장비 데이터 업데이트 확인
        # 모든 사이트
        for site_id in siteId_list:
            # 장비 데이터 가져오기
            data_list = self.api.fetch_eqps(site_id)
            remove_list = []

            for data in data_list:
                # DB에 있는 데이터 조회
                fetch_data = self.db.select_filter_one(equipments_info, site_id=site_id, perf_id=data['perfId'])
                obj = equipments_info(siteID=site_id, **data)
                # DB 에 없는 경우 데이터 추가
                if fetch_data is None:
                    self.db.insert_object(obj)
                # 데이터가 모두 최신인지 확인
                elif not obj == fetch_data:
                    remove_list.append(fetch_data)
                    self.db.insert_object(obj)
                # 최신 데이터와 같으면 그대로 보존
                else:
                    pass
            # 제거할 객체가 있는 경우 삭제
            if not remove_list:
                self.db.delete(remove_list)

    def update_elec(self, before_days: int = 7):
        eqps_list = self.db.select_all(equipments_info)
        insert_list = []
        remove_list = []
        for eqps_obj in eqps_list:
            print(f"{eqps_obj} 데이터 조회")
            for day in range(before_days):
                req_time = datetime.now() - timedelta(days=day) - TEST_TIME
                req_time = req_time.strftime("%Y%m%d")  # 오늘 날짜를 api 형식에 맞게 변형
                # api로 데이터 받아오기
                api_data = self.api.fetch_elec(eqps_obj.site_id, eqps_obj.perf_id, req_time)
                # db 데이터 가져오기
                fetch_data = self.db.select_filter_one(power_info, site_id=eqps_obj.site_id,
                                                       perf_id=eqps_obj.perf_id, ymdms=req_time)
                # DB에 데이터가 없는 경우 추가
                if fetch_data is None:
                    insert_list.append(api_data)
                # 데이터가 있는데 최신데이터인 경우
                elif api_data == fetch_data:
                    # 무시
                    pass
                # 이전 데이터를 지우고 최신 데이터를 생성
                else:
                    remove_list.append(fetch_data)
                    insert_list.append(api_data)

                print(len(api_data))
        start = time.time()  # 시작 시간 저장
        if remove_list:
            self.db.delete(remove_list)
        if insert_list:
            self.db.insert_list(insert_list)
        logger.info(f"timer : {time.time() - start}")



def ann_run_test(self):
    pass
