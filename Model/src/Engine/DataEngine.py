from logging import getLogger

from settings import siteId_list
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

            for data in data_list:
                # DB에 있는 데이터 조회
                fetch_data = self.db.select_filter_one(equipments_info, site_id=site_id, perf_id=data['perfId'])
                # DB 에 없는 경우 데이터 추가
                if fetch_data is None:
                    obj = equipments_info(siteID=site_id, **data)
                    self.db.insert_object(obj)

                # 데이터가 모두 최신인지 확인
                else:
                    # 이름이 달라서 이것뿐이다.
                    if site_id != fetch_data.site_id:
                        logger.warning(f"eqps changed site_id \n"
                                       f"{fetch_data} -> {data}")
                        fetch_data.site_id = data.get('siteID')
                        self.db.commit()
                    if int(data.get('perfId')) != fetch_data.perf_id:
                        logger.warning(f"eqps changed perfId \n"
                                       f"{fetch_data} -> {data}")
                        fetch_data.perf_id = data.get('perfId')
                        self.db.commit()
                    if data.get('eqpCode') != fetch_data.eqp_code:
                        logger.warning(f"eqps changed eqpCode \n"
                                       f"{fetch_data} -> {data}")
                        fetch_data.eqp_code = data.get('eqpCode')
                        self.db.commit()
                    if data.get('eqpName') != fetch_data.eqp_name:
                        logger.warning(f"eqps changed eqpName \n"
                                       f"{fetch_data} -> {data}")
                        fetch_data.eqp_name = data.get('eqpName')
                        self.db.commit()
                    if data.get('eqpType') != fetch_data.eqp_type:
                        logger.warning(f"eqps changed eqpType \n"
                                       f"{fetch_data} -> {data}")
                        fetch_data.eqp_type = data.get('eqpType')
                        self.db.commit()

    def update_elec(self):
        eqps_list = self.db.select_all(equipments_info)
        for eqps_obj in eqps_list:
            print(eqps_obj)
            data = self.api.fetch_elec(eqps_obj.site_id, eqps_obj.perf_id, 20200309)
            print(data)


def ann_run_test(self):
    pass
