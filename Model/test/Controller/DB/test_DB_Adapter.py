import unittest

from src.Controller.DB.DB_Adapter import DBAdapter


class DBAdapterTest(unittest.TestCase):

    def setUp(self):
        self.db_adapter = DBAdapter()

    def test_connection(self):
        """
        DB 접근 테스트
        """
        sql = f"SELECT * from auth_permission"
        data = self.db_adapter.select_sql(sql)
        self.assertIsNotNone(data, "DB 연결이 안됩니다.")

    def test_insert(self):
        """
        api로 받은 데이터를 DB에 삽입
        """
        # 데이터 생성
        sql = f"INSERT INTO app_collect_equipments_info " \
              f"(site_id, perf_id, eqp_code, eqp_name, eqp_type, created_at)" \
              f"VALUES ('test', '777', '-1', '없음', '-', current_timestamp);"
        self.db_adapter.run_sql(sql)

        # 데이터 검색
        sql = f"SELECT * from app_collect_equipments_info " \
              f"WHERE site_id = 'test' AND perf_id = '777'"
        data = self.db_adapter.select_sql(sql)
        self.assertIsNotNone(data)

        # 데이터 제거
        sql = f"delete from app_collect_equipments_info " \
              f"WHERE site_id = 'test' AND perf_id = '777'"
        self.db_adapter.run_sql(sql)

        sql = f"SELECT * from app_collect_equipments_info " \
              f"WHERE site_id = 'test' AND perf_id = '777'"
        data = self.db_adapter.select_sql(sql)
        self.assertEqual(data, [])