import time
import unittest
from logging import getLogger
from time import sleep

from settings import siteId_list
from src.Controller.API.adr_api_client import ADR_API_Client
from src.DB.DB_Adapter import DBAdapter
from src.DB.model.EquipInfo import equipments_info
from src.DB.model.PowerInfo import power_info
from src.Engine.DataEngine import DataEngine
from test.utils_test_code import check_time_decorator

logger = getLogger(__name__)


class DataEngineTest(unittest.TestCase):
    api = ADR_API_Client()
    db = DBAdapter(on_test=True)
    data_engine = DataEngine(db)

    def setUp(self):
        self.db.clear_table_all(equipments_info)
        self.db.clear_table_all(power_info)

    def tearDown(self):
        self.db.clear_table_all(equipments_info)
        self.db.clear_table_all(power_info)

    @check_time_decorator
    def test_recent_date_eqps(self):
        """
        update_eqps
        데이터가 최신 데이터인지 확인
        """
        logger.info("test_recent_date_eqps")
        self.data_engine.update_eqps()

        # 장비 데이터 업데이트 확인
        # 모든 사이트
        for site_id in siteId_list:
            # 장비 데이터 가져오기
            data_list = self.api.fetch_eqps(site_id)
            for data in data_list:
                fetch_data = self.db.select_filter_one(equipments_info, site_id=site_id, perf_id=data['perfId'])
                obj = equipments_info(siteID=site_id, **data)
                self.assertEqual(obj, fetch_data)

    @check_time_decorator
    def test_update_eqps_warnning(self):
        """
        정상적으로 업데이트가 되는 지 확인
        :return:
        """
        logger.info("test_update_eqps_warnning")
        # 데이터 추가
        self.data_engine.update_eqps()
        fetch_data = self.db.select_one(equipments_info)

        # 데이터 변경
        fetch_data.eqp_code = "test_warning"
        self.db.commit()

        # 업데이트
        self.data_engine.update_eqps()

        # 알림
        logger.warning("위 로그는 test_update_eqps_warnning 테스트 로그 입니다.")

    # @check_time_decorator
    # def test_update_elec(self):
    #
    #     # 장비 리스트 갱신
    #     self.data_engine.update_eqps()
    #     # 장비 정보 업데이트
    #     self.data_engine.update_elec()
        # print("----------")
        # sleep(1)
        # self.data_engine.update_elec(1)

        # print("end not")
        # while True:
        #     pass

    @check_time_decorator
    def test_update_elec_remove_all(self):

        # 장비 리스트 갱신
        self.data_engine.update_eqps()
        # 장비 정보 업데이트
        self.data_engine.update_elec_remove_all()
        # print("----------")
        # self.data_engine.update_elec_remove_all(1)

        # print("----------")
        # sleep(1)
        # self.data_engine.update_elec(1)

        # print("end not")
        # while True:
        #     pass
