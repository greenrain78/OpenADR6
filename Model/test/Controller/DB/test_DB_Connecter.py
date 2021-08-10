"""
DB에 직접적인 역활을 수행
- 커서를 생성하여 sql문을 실행
"""
import unittest

from src.Controller.DB.DB_Connecter import DB_Connecter


class DB_ConnecterTest(unittest.TestCase):

    def setUp(self):
        self.db_connect = DB_Connecter()


"""
할 테스트가 없네
"""
