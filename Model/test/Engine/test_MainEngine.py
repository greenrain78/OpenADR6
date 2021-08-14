import unittest
from logging import getLogger

from settings import siteId_list
from src.Controller.API.adr_api_client import ADR_API_Client
from src.DB.DB_Adapter import DBAdapterQuery
from src.DB.model.EquipInfo import equipments_info
from src.DB.model.PowerInfo import power_info
from src.Engine.DataEngine import DataEngine
from src.Engine.MainEngine import MainEngine
from test.utils_test_code import check_time_decorator

logger = getLogger(__name__)


class MainEngineTest(unittest.TestCase):
    api = ADR_API_Client()
    data_engine = DataEngine(on_test=True)
    main_engine = MainEngine(data_engine=data_engine)
    db = DBAdapterQuery(on_test=True)

    def setUp(self):
        self.db.clear_table_all(equipments_info)
        self.db.clear_table_all(power_info)

    def tearDown(self):
        self.db.clear_table_all(equipments_info)
        self.db.clear_table_all(power_info)

    def test_ann_run_test(self):
        logger.info(f"test_ann_run_test")
        self.main_engine.ann_run_test()
