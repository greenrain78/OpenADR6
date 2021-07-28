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
            self.conn = pymysql.connect(
                host=mariaDB['IP'],
                dbname=mariaDB["db"],
                user=mariaDB['ID'],
                password=mariaDB['password'],
                port=mariaDB['port']
            )
        elif db_name == "postgresql":
            # postgres sql 연결
            self.conn = psycopg2.connect(
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
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()
        self.cursor.close()

    def execute(self, query, args={}):
        """
        sql 문을 실행
        insert나 update 같은 sql 문을 사용
        """
        self.cursor.execute(query, args)
        log.debug(query)

    def execute_fetch(self, query, args={}):
        """
        sql 문을 실행
        select 같은 sql문을 사용하여 데이터를 가져온다.
        :return: data
        """
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def execute_fetch_dict(self, query, args={}):
        """
        sql 문을 실행
        select 같은 sql문을 사용하여 데이터를 가져온다.
        사전 형식으로 출력
        :return: data
        """
        self.cursor.execute(query, args)
        columns = list(self.cursor.description)
        result = self.cursor.fetchall()
        results = []
        for row in result:
            row_dict = {}
            for i, col in enumerate(columns):
                row_dict[col.name] = row[i]
            results.append(row_dict)

        return results

    def fetch_all(self):
        """
        execute 를 사용전에 이걸 먼저 사용하면 오류 발생 함
        :return:
        """
        try:
            row = self.cursor.fetchall()
            return row
        except Exception as e:
            log.error(f"sql문 실행중 오류 발생: {e}")

    def commit(self):
        """
        DB에 실제 반영
        """
        self.conn.commit()
