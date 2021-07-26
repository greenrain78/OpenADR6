"""
정상 작동하는지 임시로 구현한 테스트 엔진
드라이버
"""
from datetime import datetime

from Controller.DB_Controller import DBAdapter


class TestEngine:
    """
    정상 작동하는지 임시로 구현한 테스트 엔진
    """

    def __init__(self):
        # DB 데이터 입출력
        self.db = DBAdapter()

    def hello(self):
        """
        간단 engine 동작 확인
        """
        print(f"hello {datetime.now()}", flush=True)

    def db_connect(self):
        """
        DB 접근 테스트
        """
        sql = f"SELECT * from auth_permission"
        data = self.db.run_sql(sql)
        print(f"TEST ENGONE: {data}")
