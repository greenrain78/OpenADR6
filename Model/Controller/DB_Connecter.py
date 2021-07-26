"""
DB에 직접적인 역활을 수행
- 커서를 생성하여 sql문을 실행
"""

from logging import getLogger

import psycopg2
import pymysql

from settings import mariaDB, postgresql

log = getLogger(__name__)


class DB_Connecter:
    def __init__(self, db_name: str = "mariaDB"):
        """
        :param db_name:
        DB에 따라 연결 생성
        """
        if db_name == "mariaDB":
            # maria db 연결
            self.db = pymysql.connect(
                host=mariaDB['IP'],
                dbname=mariaDB["db"],
                user=mariaDB['ID'],
                password=mariaDB['password'],
                port=mariaDB['port']
            )
        elif db_name == "postgresql":
            # postgres sql 연결
            self.db = psycopg2.connect(
                host=postgresql['IP'],
                dbname=postgresql["db"],
                user=postgresql['ID'],
                password=postgresql['password'],
                port=postgresql['port']
            )
        else:
            # 예외 발생
            log.error(f"DB가 잘못 입력되었습니다. {db_name}")
            raise ValueError
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.cursor.commit()
