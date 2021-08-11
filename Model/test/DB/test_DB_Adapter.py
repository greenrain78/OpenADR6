import unittest
from logging import getLogger

from src.DB.DB_Adapter import DBAdapter
from src.DB.model.EquipInfo import equipments_info
logger = getLogger(__name__)


class DBAdapterTest(unittest.TestCase):
    db = DBAdapter(on_test=True)

    def setUp(self):
        self.db.clear_table_all(equipments_info)

    def tearDown(self):
        self.db.clear_table_all(equipments_info)

    # @check_time_decorator
    # def test_insert_list_None(self):
    #     # 빈데이터인 경우 에러 발생
    #     self.db.insert_list(None)

    # @check_time_decorator
    # def test_insert_eqps(self):
    #     logger.info("test_insert_eqps")
    #     data_1 = {
    #         'siteID': "777",
    #         'eqpCode': '-1',
    #         'eqpName': '12',
    #         'eqpType': '-',
    #         'perfId': '1234'
    #     }
    #     data_obj1 = equipments_info(**data_1)
    #     print(data_obj1)
    #     self.db.insert_object(data_obj1)
    #
    # def test_delete_eqps(self):
    #     self.db.clear_table_all(equipments_info)
