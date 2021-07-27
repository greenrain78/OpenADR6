from logging import getLogger

from settings import db_table_name_elec

log = getLogger(__name__)


class DBAdapterELEC:
    """
    ELEC 데이터를 사용하는 엔진
    해당 데이터를 다루는 모든 조작을 담당
    """

    def __init__(self, db):
        self.db = db
        self.table = db_table_name_elec

    def check_data(self, data: dict) -> bool:
        """
        :param data:
        :return: 데이터가 모두 정상인지 검사
        정상 = true
        비정상 = false
        """
        table_raw_column = self.table['raw_column']

        # 키값이 모두 있는지 검사
        if all(element in data for element in table_raw_column):
            return True
        else:
            log.error(f"입력할 데이터가 잘못되었습니다. {data}")
            return False

    def insert_run(self, site_id, perf_id, eqp_code, eqp_name, eqp_type):
        """
        실제 insert문을 동작시키는 함수
        """
        table_name = self.table['name']
        sql = f"INSERT INTO {table_name} " \
              f"(site_id, perf_id, eqp_code, eqp_name, eqp_type, created_at) " \
              f"VALUES (" \
              f"'{site_id}', '{perf_id}', '{eqp_code}', '{eqp_name}', '{eqp_type}', " \
              f"current_timestamp)"
        self.db.execute(sql)

    def insert(self, data: dict) -> bool:
        """
        데이터 1개 insert
        :param data:
        :return: insert 성공 유무 반환
        """
        # 키값이 모두 있는지 검사
        if self.check_data(data):
            self.insert_run(
                site_id=data['siteID'],
                perf_id=data['perfId'],
                eqp_code=data['eqpCode'],
                eqp_name=data['eqpName'],
                eqp_type=data['eqpType']
            )
            self.db.commit()
            log.debug(f"insert elec : {data}")
            return True
        else:
            log.error(f"입력할 데이터가 잘못되었습니다. {data}")
            return False

    def insert_list(self, data_list, siteID):
        """
        api로 받는 데이터를 DB에 저장
        :param data_list:
        :param siteID:
        :return:
        """
        for data in data_list:
            # siteID 추가
            data['siteID'] = siteID
            if self.check_data(data):
                self.insert_run(
                    site_id=data['siteID'],
                    perf_id=data['perfId'],
                    eqp_code=data['eqpCode'],
                    eqp_name=data['eqpName'],
                    eqp_type=data['eqpType']
                )
            else:
                log.error(f"입력할 데이터가 잘못되었습니다. {data}")
        # db에 반영
        self.db.commit()

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
