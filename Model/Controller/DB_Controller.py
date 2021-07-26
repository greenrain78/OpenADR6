"""
DB 와 연결하는 부분
"""
from logging import getLogger

from Controller.DB_Connecter import DB_Connecter
from settings import using_db

log = getLogger(__name__)


class DBAdapter:
    """
    데이터를 사용하는 엔진
    해당 데이터를 다루는 모든 조작을 담당
    """

    def __init__(self):
        self.elec = DBAdapterELEC()
        self.db = DB_Connecter(using_db)

    def run_sql(self, sql):
        """
        직접 sql문을 작성해서 실행
        결과는 보장 못함
        :return:
        """
        log.debug("sql 실행")
        data = self.db.execute(sql)
        return data


class DBAdapterELEC:
    """
    ELEC 데이터를 사용하는 엔진
    해당 데이터를 다루는 모든 조작을 담당
    """

    def __init__(self):
        pass