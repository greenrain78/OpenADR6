import unittest
from logging import getLogger
from time import sleep

from settings import siteId_list
from src.Controller.API.adr_api_client import ADR_API_Client
from src.DB.DB_Adapter import DBAdapter
from src.DB.model.EquipInfo import equipments_info
from src.Engine.DataEngine import DataEngine

logger = getLogger(__name__)


class DataEngineTest(unittest.TestCase):
    api = ADR_API_Client()
    db = DBAdapter(on_test=True)
    data_engine = DataEngine(db)

    def setUp(self):
        self.db.clear_table_all(equipments_info)

    def tearDown(self):
        self.db.clear_table_all(equipments_info)

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
                self.assertEqual(site_id, fetch_data.site_id)
                self.assertEqual(int(data.get("perfId")), fetch_data.perf_id)
                self.assertEqual(data.get("eqpCode"), fetch_data.eqp_code)
                self.assertEqual(data.get("eqpName"), fetch_data.eqp_name)
                self.assertEqual(data.get("eqpType"), fetch_data.eqp_type)

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
        print(fetch_data)
        fetch_data.eqp_code = "test_warning"
        self.db.commit()

        # 업데이트
        self.data_engine.update_eqps()
        print(fetch_data)
