import unittest

from settings import using_db
from src.Controller.DB.DB_Adapter_EQPS import DBAdapterEQPS
from src.Controller.DB.DB_Connecter import DB_Connecter


class DBAdapterEQPSTest(unittest.TestCase):

    def setUp(self):
        connect = DB_Connecter(using_db)
        self.db = DBAdapterEQPS(connect)

    def test_insert_read_delete(self):
        """
        api로 받은 데이터를 DB에 삽입
        """
        data_1 = {
            'siteID': "ace",
            'eqpCode': '-1',
            'eqpName': '12',
            'eqpType': '-',
            'perfId': '1234'
        }
        self.db.insert(data_1)
        # data_2 = self.db.read_all()
        # print(data_2)
        # self.assertEqual(data_1['siteID'], data_2['site_id'])
        # self.assertEqual(data_1['perfId'], data_2['perf_id'])
        # self.assertEqual(data_1['eqpCode'], data_2['eqp_code'])
        # self.assertEqual(data_1['eqpName'], data_2['eqp_name'])
        # self.assertEqual(data_1['eqpType'], data_2['eqp_type'])

    def test_read_all(self):
        """
        작동하는지만 테스트
        :return:
        """
        data_1 = {
            'siteID': "ace",
            'eqpCode': '-1',
            'eqpName': '12',
            'eqpType': '-',
            'perfId': '1234'
        }
        # self.db.insert(data_1)
        # data_2 = self.db.read_all()
        # print(f" eqps {data_2}")
        # self.assertIsNotNone(data_2)

    # def test_fetch_insert(self):
    #     api = ADR_API_Client()
    #
    #     raw_data = api.fetch_eqps('ace')
    #     data_list = raw_data.get('eqps')
    #     self.db.insert_list(data_list, 'ace')
