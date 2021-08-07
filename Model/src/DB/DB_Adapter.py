"""
DB 와 연결하는 부분
"""
import os
from logging import getLogger

from sqlalchemy.engine.create import create_engine
from sqlalchemy.orm.session import sessionmaker

log = getLogger(__name__)


def create_db_link(debug):
    """
    :param debug:
    :return: engine
    """
    database = os.environ.get('ADR_DB', 'openadr')
    user = os.environ.get('ADR_USER', 'user')
    password = os.environ.get('ADR_PASSWORD', '1234')

    if not debug:
        host = os.environ.get('ADR_HOST', 'db')
        port = os.environ.get('ADR_PORT', '5432')
    else:
        # 테스트 DB
        host = os.environ.get('TEST_HOST', 'db_test')
        port = os.environ.get('TEST_PORT', '5432')
    db_link = f'postgresql://{user}:{password}@{host}:{port}/{database}'
    return db_link


class DBAdapter:
    """
    데이터를 사용하는 엔진
    해당 데이터를 다루는 모든 조작을 담당
    """

    def __init__(self, debug=True):
        # 임시로 IS_SQL_ECHO 환경변수를 가져와서 엔진 설정
        echo = os.environ.get('IS_SQL_ECHO').lower() in 'true'
        # 엔진 링크 생성
        db_link = create_db_link(debug)
        # 엔진 생성
        self.engine = create_engine(db_link, echo=echo)
        # 세션 생성자 생성
        self.Session = sessionmaker(bind=self.engine)

    def insert_object(self, obj):
        """
        받은 오브젝트를 DB에 저장
        :param obj:
        :return:
        """
        with self.Session() as session:
            session.add(obj)
            session.commit()

    def insert_list(self, obj_list: list):
        """
        받은 오브젝트 리스트를 모두 DB에 일괄 저장
        :param obj_list:
        :return:
        """

        with self.Session() as session:
            session.add_all(obj_list)
            session.commit()

    def clear_table_all(self, model):
        with self.Session() as session:
            session.query(model).delete()
            session.commit()
