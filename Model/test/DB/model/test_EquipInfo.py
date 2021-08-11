import unittest
from logging import getLogger

from src.Controller.API.adr_api_client import ADR_API_Client
from src.DB.DB_Adapter import DBAdapter
from src.DB.model.EquipInfo import equipments_info

logger = getLogger(__name__)


class EquipmentsInfoTest(unittest.TestCase):
    db = DBAdapter(on_test=True)
    api = ADR_API_Client()

    def setUp(self):
        self.db.clear_table_all(equipments_info)

    def tearDown(self):
        self.db.clear_table_all(equipments_info)

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
        self.db.delete_obj(obj)
        delete_data = self.db.select_one(equipments_info)
        self.assertIsNone(delete_data)

    def test_fetch_data(self):
        site_id = 'ace'
        data_list = self.api.fetch_eqps(site_id)
        obj_list = []
        for data in data_list:
            obj = equipments_info(siteID=site_id, **data)
            self.db.insert_object(obj)
            obj_list.append(obj)

        # 검증
        for obj in obj_list:
            result = self.db.select_filter_one(equipments_info, perf_id=obj.perf_id)
            self.assertEqual(obj, result)


