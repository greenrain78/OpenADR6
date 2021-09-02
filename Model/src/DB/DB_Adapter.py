"""
DB 와 연결하는 부분
"""
from logging import getLogger
import pandas as pd

from sqlalchemy.engine.create import create_engine
from sqlalchemy.orm import session
from sqlalchemy.orm.session import sessionmaker

from settings import IS_SQL_ECHO, DATABASES
from src.Controller.time_record import Record, record_decorator

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


class DBAdapter(object):
    """
    데이터를 사용하는 엔진
    해당 데이터를 다루는 모든 조작을 담당
    """

    def __init__(self, on_test=False):
        self.engine = create_db_engine(on_test=on_test)
        self.session_maker = sessionmaker(bind=self.engine)
        self.session = self.session_maker()
        self.record = Record("DBAdapter")

    def __repr__(self):
        return f"DBAdapter - {self.record}"

    # def _decorator(func):
    #     def func_wrapper(self, *args, **kwargs):
    #         start = time.time()  # 시작 시간 저장
    #         func(self, *args, **kwargs)
    #         print(f" description {start}")
    #
    #     return func_wrapper

    @record_decorator
    def insert_object(self, obj):
        """
        받은 오브젝트를 DB에 저장
        :param obj:
        :return:
        """

        self.session.add(obj)
        self.session.commit()

    @record_decorator
    def insert_list(self, obj_list: list):
        """
        받은 오브젝트 리스트를 모두 DB에 일괄 저장
        :param obj_list:
        :return:
        """

        self.session.add_all(obj_list)
        self.session.commit()

    @record_decorator
    def select_one(self, model):
        result = self.session.query(model).first()
        return result

    @record_decorator
    def select_all(self, model):
        result = self.session.query(model).all()
        return result

    @record_decorator
    def select_query(self, model):
        result = self.session.query(model)
        return result

    @record_decorator
    def select_filter_one(self, model, **filter_list):
        result = self.session.query(model).filter_by(**filter_list).first()
        return result

    @record_decorator
    def select_filter_all(self, model, **filter_list):
        result = self.session.query(model).filter_by(**filter_list).all()
        return result

    @record_decorator
    def get_query(self, model):
        result = self.session.query(model)
        return result

    @record_decorator
    def delete(self, obj):
        # 리스트인 경우 for문으로 제거
        if type(obj) is list:
            for i in obj:
                self.session.delete(i)
        else:
            self.session.delete(obj)

    @record_decorator
    def read_dataframe(self, model, **filter_list):
        data = pd.read_sql(self.session.query(model).filter_by(**filter_list).statement, self.session.bind)
        return data

    def clear_table_all(self, model):
        self.session.query(model).delete()
        self.session.commit()

    def rollback(self):
        # 업데이트 한 객체 모두 롤백
        self.rollback()

    @record_decorator
    def commit(self):
        # 객체를 업데이트 후 반영
        self.session.commit()


class DBAdapterQuery:
    """
    데이터를 사용하는 엔진
    해당 데이터를 다루는 모든 조작을 담당
    """

    def __init__(self, on_test=False):
        self.engine = create_db_engine(on_test=on_test)
        self.session_maker = sessionmaker(bind=self.engine)
        self.session = self.session_maker()
        self.record = Record("DBAdapterQuery")

    def __repr__(self):
        return f"DBAdapter - {self.record}"

    @record_decorator
    def insert_object(self, obj):
        """
        받은 오브젝트를 DB에 저장
        :param obj:
        :return:
        """

        self.session.add(obj)
        self.session.commit()

    @record_decorator
    def insert_list(self, obj_list: list):
        """
        받은 오브젝트 리스트를 모두 DB에 일괄 저장
        :param obj_list:
        :return:
        """
        self.session.add_all(obj_list)
        self.session.commit()

    @record_decorator
    def delete(self, obj):
        # 리스트인 경우 for문으로 제거
        if type(obj) is list:
            for i in obj:
                self.session.delete(i)
        else:
            self.session.delete(obj)

    @record_decorator
    def get_obj_one(self, query: session.query):
        """
        해당 쿼리에서 obj 하나만 가져오기
        """
        result = query.first()
        return result

    @record_decorator
    def get_obj_all(self, query: session.query):
        """
        해당 쿼리에서 obj 모두 가져오기
        """
        result = query.all()
        return result

    def select_query(self, model) -> session.query:
        """
        해당 model에 대한 기본 쿼리 생성
        """
        result = self.session.query(model)
        return result

    def add_filter(self, query: session.query, **filter_list) -> session.query:
        """
        해당 쿼리에 대한 필터 추가
        :param query:
        :param filter_list:
        :return:
        """
        result = query.filter_by(**filter_list)
        return result

    def df_insert(self, df, table_name):
        df.to_sql(name=table_name, con=self.engine,
                  if_exists='append', index=False, index_label='id',)

    def read_dataframe(self, query: session.query):
        """
        주워진 쿼리에 대해 pandas로 변환
        :param query:
        :return:
        """
        data = pd.read_sql(query.statement, self.session.bind)
        return data

    def clear_table_all(self, model):
        """
        해당 테이블에 있는 데이터 모두 제거
        """
        self.session.query(model).delete()
        self.session.commit()

    def rollback(self):
        # 업데이트 한 객체 모두 롤백
        self.rollback()

    @record_decorator
    def commit(self):
        # 객체를 업데이트 후 반영
        self.session.commit()
