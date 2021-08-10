import unittest

from settings import using_db
from src.Controller.API.adr_api_client import ADR_API_Client
from src.Controller.DB.DB_Adapter_ELEC import DBAdapterELEC
from src.Controller.DB.DB_Connecter import DB_Connecter


class DBAdapterELECTest(unittest.TestCase):

    def setUp(self):
        connect = DB_Connecter(using_db)
        self.db = DBAdapterELEC(connect)

    def test_fetch_insert(self):
        api = ADR_API_Client()
        data_list = api.fetch_elec('ace', 300, 20200309)
        self.db.insert_list(data_list, 'ace')
        # print(f"TEST ENGINE db_insert_elec: {data_list}")
