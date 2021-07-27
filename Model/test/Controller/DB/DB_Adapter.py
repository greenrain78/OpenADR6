import unittest

from src.Controller.DB.DB_Adapter import DBAdapter


class DBAdapterTest(unittest.TestCase):

    def setUp(self):
        self.db_adapter = DBAdapter()

