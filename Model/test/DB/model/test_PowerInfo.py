import unittest
from logging import getLogger
from time import sleep

from src.DB.DB_Adapter import DBAdapter
from src.DB.model.PowerInfo import power_info

logger = getLogger(__name__)


class PowerInfoTest(unittest.TestCase):
    db = DBAdapter(on_test=True)

    def setUp(self):
        pass

    def tearDown(self):
        self.db.clear_table_all(power_info)

    def test_CRUD_one(self):
        logger.info("test_CRUD_one")
        data = {'siteID': 'test', 'pnName': 'PA-A-30_판넬PC', 'eqpName': '2층203호냉난방기',
                'perfId': '444', 'ymdms': '20200309000010', 'volTage': '228.247',
                'amPere': '0.372', 'arPower': '75030', 'atvPower': '3245',
                'ratPower': '4294890000', 'pwFactor': '10', 'accruePower': '1142780',
                'voltagerS': '395.576', 'voltagesT': '395.335', 'voltagetR': '393.51',
                'temperature': '24.768'
                }
        obj = power_info(**data)

        # DB에 데이터 추가
        self.db.insert_object(obj)

        # DB에 데이터 읽기
        fetch_data = self.db.select_one(power_info)
        self.assertIsNotNone(fetch_data)

        # 데이터 비교
        self.assertEqual(obj, fetch_data)

        # 데이터 업데이트
        fetch_data.perf_id = 777
        self.db.commit()

        update_data = self.db.select_one(power_info)

        self.assertEqual(update_data.perf_id, 777)

        # 데이터 제거
        self.db.delete_obj(obj)
        delete_data = self.db.select_one(power_info)
        self.assertIsNone(delete_data)


