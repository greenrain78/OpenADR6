"""
정상 작동하는지 임시로 구현한 테스트 엔진
드라이버
"""
from datetime import datetime

from src.Controller.API.adr_api_client import ADR_API_Client
from src.Controller.DB.DB_Adapter import DBAdapter


class TestEngine:
    """
    정상 작동하는지 임시로 구현한 테스트 엔진
    맨 위가 최근에 작성한 코드
    """

    def __init__(self):
        # DB 데이터 입출력
        self.adr_api = ADR_API_Client()
        self.db = DBAdapter()

    def db_insert_elec(self):
        data_list = self.adr_api.fetch_elec('ace', 300, 20200309)
        self.db.eqps.insert_list(data_list, 'ace')
        # print(f"TEST ENGINE db_insert_elec: {data_list}")

    def api_controller_elec(self):
        """
          api 연결 테스트
          """
        data_list = self.adr_api.fetch_elec('ace', 300, 20200309)
        print(f"TEST ENGINE db_connect")
        # print(data_list)

        for data in data_list:
            print(data)

    def db_fetch_insert(self):
        """
        :return:
        """
        raw_data = self.adr_api.fetch_eqps('ace')
        data_list = raw_data.get('eqps')
        self.db.elec.insert_list(data_list, 'ace')
        print(f"TEST ENGINE db_fetch_insert: {data_list}")

    def db_insert_controller(self):
        """
        api로 받은 데이터를 DB에 삽입
        """
        data = {
            'siteID': "ace",
            'eqpCode': '-1',
            'eqpName': '12',
            'eqpType': '-',
            'perfId': '1234'
        }
        self.db.elec.insert(data)
        print(f"TEST ENGINE db_insert_controller: {data}")

    def db_select(self):
        sql = f"SELECT * from app_collect_equipments_info"
        data = self.db.select_sql(sql)
        print(f"TEST ENGINE db_select: {data}")

    def db_insert(self):
        """
        api로 받은 데이터를 DB에 삽입
        """
        sql = f"INSERT INTO app_collect_equipments_info " \
              f"(site_id, perf_id, eqp_code, eqp_name, eqp_type, created_at)" \
              f"VALUES ('ace', '777', '-1', '없음', '-', current_timestamp);"
        self.db.run_sql(sql)
        sql = f"SELECT * from app_collect_equipments_info"
        data = self.db.select_sql(sql)
        print(f"TEST ENGINE db_insert: {data}")

    def api_connect_eqps(self):
        """
        api 연결 테스트
        """
        data = self.adr_api.fetch_eqps('ace')
        print(f"TEST ENGINE db_connect: {data}")

    def db_connect(self):
        """
        DB 접근 테스트
        """
        sql = f"SELECT * from auth_permission"
        data = self.db.run_sql(sql)
        print(f"TEST ENGINE db_connect: {data}")

    def hello(self):
        """
        간단 engine 동작 확인
        """
        print(f"hello {datetime.now()}", flush=True)
