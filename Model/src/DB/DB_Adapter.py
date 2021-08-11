"""
DB 와 연결하는 부분
"""
import os
from logging import getLogger

from sqlalchemy.engine.create import create_engine
from sqlalchemy.orm.session import sessionmaker

from settings import IS_SQL_ECHO, DATABASES

log = getLogger(__name__)


def create_db_engine(on_test: bool):
    """
    :param on_test:
    :return: engine
    """
    if on_test:
        # 테스트 실행시 테스트 DB 동작
        db = DATABASES['test']
    else:
        db = DATABASES['default']
    db_link = f'postgresql://{db["user"]}:{db["password"]}' \
              f'@{db["host"]}:{db["port"]}/{db["database"]}'
    engine = create_engine(db_link, echo=IS_SQL_ECHO)
    return engine


class DBAdapter:
    """
    데이터를 사용하는 엔진
    해당 데이터를 다루는 모든 조작을 담당
    """

    def __init__(self, on_test=False):
        self.engine = create_db_engine(on_test=on_test)
        self.session_maker = sessionmaker(bind=self.engine)
        self.session = self.session_maker()

    def insert_object(self, obj):
        """
        받은 오브젝트를 DB에 저장
        :param obj:
        :return:
        """

        self.session.add(obj)
        self.session.commit()

    def insert_list(self, obj_list: list):
        """
        받은 오브젝트 리스트를 모두 DB에 일괄 저장
        :param obj_list:
        :return:
        """

        self.session.add_all(obj_list)
        self.session.commit()

    def select_one(self, model):
        result = self.session.query(model).first()
        return result

    def select_all(self, model):
        result = self.session.query(model).all()
        return result

    def select_query(self, model):
        result = self.session.query(model)
        return result

    def select_filter_one(self, model, **filter_list):
        result = self.session.query(model).filter_by(**filter_list).first()
        return result

    def select_filter_all(self, model, **filter_list):
        result = self.session.query(model).filter_by(**filter_list).all()
        return result

    def delete(self, obj):
        # 리스트인 경우 for문으로 제거
        if type(obj) is list:
            for i in obj:
                self.session.delete(i)
        else:
            self.session.delete(obj)

    def clear_table_all(self, model):
        self.session.query(model).delete()
        self.session.commit()

    def rollback(self):
        # 업데이트 한 객체 모두 롤백
        self.rollback()

    def commit(self):
        # 객체를 업데이트 후 반영
        self.session.commit()
