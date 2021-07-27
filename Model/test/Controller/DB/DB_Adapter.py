"""
DB 와 연결하는 부분
"""
from logging import getLogger

from src.Controller.DB.DB_Adapter_ELEC import DBAdapterELEC
from src.Controller.DB.DB_Adapter_EQPS import DBAdapterEQPS
from src.Controller.DB.DB_Connecter import DB_Connecter
from settings import using_db

log = getLogger(__name__)


class DBAdapter:
    """
    데이터를 사용하는 엔진
    해당 데이터를 다루는 모든 조작을 담당
    """

    def __init__(self):
        self.db = DB_Connecter(using_db)
        self.elec = DBAdapterELEC(self.db)
        self.eqps = DBAdapterEQPS(self.db)

    def select_sql(self, sql):
        """
        직접 sql문을 작성해서 실행
        db에 있는 데이터를 가져온다.
        db에 영향 X
        :return: data
        """
        data = self.db.execute_fetch(sql)
        log.debug(f"sql 실행 : {sql} - data: {data}")
        return data

    def run_sql(self, sql):
        """
        직접 sql문을 작성해서 실행
        결과는 보장 못함
        """
        self.db.execute(sql)
        self.db.commit()
        log.debug(f"sql 실행 : {sql}")


