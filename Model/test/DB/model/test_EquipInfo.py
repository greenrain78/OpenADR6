import unittest

from src.DB.DB_Adapter import DBAdapter
from src.DB.model.EquipInfo import equipments_info


class EquipInfoTest(unittest.TestCase):
    db_adapter = DBAdapter()

    def setUp(self):
        pass

    def tearDown(self):
        # 테이블의 모든 데이터 제거
        self.db_adapter.clear_table_all(equipments_info)

    def test_insert(self):
        data = {
            'siteID': "test_insert",
            'eqpCode': '-1',
            'eqpName': '12',
            'eqpType': '-',
            'perfId': '1234'
        }
        obj = equipments_info(**data)
        self.db_adapter.insert_object(obj)

    def test_delete(self):
        data = {
            'siteID': "test_delete",
            'eqpCode': '-1',
            'eqpName': '12',
            'eqpType': '-',
            'perfId': '1234'
        }
        obj = equipments_info(**data)
        self.db_adapter.insert_object(obj)
