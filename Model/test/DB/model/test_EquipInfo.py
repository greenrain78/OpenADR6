import unittest
from logging import getLogger
from time import sleep

from src.Controller.API.adr_api_client import ADR_API_Client
from src.DB.DB_Adapter import DBAdapter
from src.DB.model.EquipInfo import equipments_info
from test.utils_test_code import CheckTimeDecorator, check_time_decorator

logger = getLogger(__name__)


class EquipmentsInfoTest(unittest.TestCase):
    db = DBAdapter(on_test=True)
    api = ADR_API_Client()

    def setUp(self):
        self.db.clear_table_all(equipments_info)

    def tearDown(self):
        self.db.clear_table_all(equipments_info)

    @check_time_decorator
    def test_CRUD_one(self):
        logger.info("test_CRUD_one")
        data = {
            'siteID': "teat",
            'eqpCode': '-1',
            'eqpName': '12',
            'eqpType': '-',
            'perfId': '1234'
        }
        obj = equipments_info(**data)
        # DB에 데이터 추가
        self.db.insert_object(obj)

        # DB에 데이터 읽기
        fetch_data = self.db.select_one(equipments_info)
        self.assertIsNotNone(fetch_data)

        # 데이터 비교
        self.assertEqual(obj, fetch_data)

        # 데이터 업데이트
        fetch_data.perf_id = 777
        self.db.commit()

        update_data = self.db.select_one(equipments_info)
        self.assertEqual(update_data.perf_id, 777)

        # 데이터 제거
        self.db.delete(obj)
        delete_data = self.db.select_one(equipments_info)
        self.assertIsNone(delete_data)

    @check_time_decorator
    def test_equal(self):
        logger.info("test_equal")
        data = {
            'siteID': "teat",
            'eqpCode': '-1',
            'eqpName': '12',
            'eqpType': '-',
            'perfId': '1234'
        }
        obj = equipments_info(**data)
        new_obj = equipments_info(**data)

        # DB에 데이터 추가
        self.db.insert_object(obj)
        self.db.insert_object(new_obj)

        # DB에 데이터 읽기
        fetch_data = self.db.select_one(equipments_info)
        self.assertIsNotNone(fetch_data)
        # sleep(100000)
        # 동일 데이터 비교
        self.assertEqual(new_obj, fetch_data)
        self.assertEqual(new_obj, obj)

    @check_time_decorator
    def test_fetch_data(self):
        logger.info("test_fetch_data")

        site_id = 'ace'
        data_list = self.api.fetch_eqps(site_id)
        obj_list = []
        for data in data_list:
            obj = equipments_info(siteID=site_id, **data)
            obj_list.append(obj)
        self.db.insert_list(obj_list)

        # 검증
        for obj in obj_list:
            result = self.db.select_filter_one(equipments_info, perf_id=obj.perf_id)
            self.assertEqual(obj, result)
