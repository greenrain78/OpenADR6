from apscheduler.jobstores import sqlalchemy

from src.DB.DB_Adapter import create_db_engine


class orm_converter:
    def __init__(self, on_test=False):
        self.engine = create_db_engine(on_test)

    def df_to_orm(self, df):

        pass
