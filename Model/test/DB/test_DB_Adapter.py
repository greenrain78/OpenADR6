import unittest

from src.DB.DB_Adapter import DBAdapter
from src.DB.model.EquipInfo import equipments_info


class DBAdapterTest(unittest.TestCase):
    db_adapter = DBAdapter()

    def setUp(self):
        # equipments_info.
        # equipments_info.metadata.clear()
        # print(dir(equipments_info.metadata))
        # print(dir(equipments_info.__table__))

        pass

    def test_insert_eqps(self):
        data_1 = {
            'siteID': "aaaaaaaaaaaaaaaaaaaa",
            'eqpCode': '-1',
            'eqpName': '12',
            'eqpType': '-',
            'perfId': '1234'
        }
        data_obj1 = equipments_info(**data_1)
        print(data_obj1)
        self.db_adapter.insert_object(data_obj1)

    def test_delete_eqps(self):
        self.db_adapter.clear_table_all(equipments_info)
