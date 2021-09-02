import time
from datetime import datetime, timedelta
from logging import getLogger

import pandas
from settings import siteId_list, TEST_TIME
from src.Controller.API.adr_api_client import ADR_API_Client
from src.DB.DB_Adapter import DBAdapter, DBAdapterQuery
from src.DB.model.EquipInfo import equipments_info
from src.DB.model.PowerInfo import power_info

logger = getLogger(__name__)


class DataEngine:
    """
    데이터와 관련된 작업을 하는 엔진
    """

    def __init__(self, on_test: bool = False):
        # DB 데이터 입출력
        self.api = ADR_API_Client()
        self.db = DBAdapterQuery(on_test=on_test)
        # self.ann = ANN_Sample_Model()

    def update_eqps(self):
        # 장비 데이터 업데이트 확인
        # 모든 사이트
        for site_id in siteId_list:
            # 장비 데이터 가져오기
            data_list = self.api.fetch_eqps(site_id)
            remove_list = []

            for data in data_list:
                # DB에 있는 데이터 조회
                base_query = self.db.select_query(equipments_info)
                query_add_filter = self.db.add_filter(base_query, site_id=site_id, perf_id=data['perfId'])
                fetch_data = self.db.get_obj_one(query_add_filter)
                obj = equipments_info(siteID=site_id, **data)
                # DB 에 없는 경우 데이터 추가
                if fetch_data is None:
                    self.db.insert_object(obj)
                # 데이터가 모두 최신인지 확인
                elif not obj == fetch_data:
                    remove_list.append(fetch_data)
                    self.db.insert_object(obj)
                # 최신 데이터와 같으면 그대로 보존
                else:
                    pass
            # 제거할 객체가 있는 경우 삭제
            if not remove_list:
                self.db.delete(remove_list)

    def get_all_eqps(self):
        base_query = self.db.select_query(equipments_info)
        # eqps_list = self.db.get_obj_all(base_query)[:10]
        eqps_list = self.db.get_obj_all(base_query)
        return eqps_list

    def update_elec(self, before_days: int = 7):
        """
        해당 부분 DB 알고리즘 개선 요망
        """
        insert_list = []
        remove_list = []

        # DB에서 장비 데이터 가져오기
        eqps_list = self.get_all_eqps()

        # # 장비 하나씩 데이터 조회
        # for eqps_obj in eqps_list:

        # 지정한 날짜 동안에 대한 데이터 조회
        for day in range(before_days):
            req_time = datetime.now() - timedelta(days=day) - TEST_TIME
            req_time = req_time.strftime("%Y%m%d")  # 오늘 날짜를 api 형식에 맞게 변형
            logger.info(f"{req_time}일차 데이터 조회")

            # 장비 하나씩 데이터 조회
            for eqps_obj in eqps_list:
                # api로 데이터 받아오기
                data_list = self.api.fetch_elec(eqps_obj.site_id, eqps_obj.perf_id, req_time)
                start_time = time.time()
                # 받은 데이터를 하나씩 분리하여 저장
                for raw_data in data_list:
                    # 데이터 객체 생성
                    api_data = power_info(siteID=eqps_obj.site_id, **raw_data)
                    # db 데이터 가져오기
                    base_query = self.db.select_query(power_info)
                    query_add_filter = self.db.add_filter(base_query, site_id=eqps_obj.site_id,
                                                          perf_id=eqps_obj.perf_id, ymdms=api_data.ymdms)
                    fetch_data = self.db.get_obj_one(query_add_filter)

                    # DB에 있는 데이터와 api데이터를 비교
                    # DB에 데이터가 없는 경우 추가
                    if fetch_data is None:
                        insert_list.append(api_data)
                    # 데이터가 있는데 최신데이터가 아닌 경우 -> 이전 데이터를 지우고 최신 데이터를 생성
                    elif api_data != fetch_data:
                        remove_list.append(fetch_data)
                        insert_list.append(api_data)
                    # 최신 데이터인 경우 무시
                    else:
                        pass
                print(f"timer {time.time() - start_time}")
                print(f"DB: {self.db}")

                # DB 데이터 추가 및 제거
                if remove_list:
                    self.db.delete(remove_list)
                    remove_list.clear()
                if insert_list:
                    self.db.insert_list(insert_list)
                    insert_list.clear()
        logger.info(f"api 정보 출력{self.api}")
        logger.info(f"elec 데이터 업데이트 - 추가: {len(insert_list)}, 갱신: {len(remove_list) - len(insert_list)}")

    def update_elec_remove_all(self, before_days: int = 7):
        """
        해당 부분 DB 알고리즘 개선 요망
        """
        # DB에서 장비 데이터 가져오기
        eqps_list = self.get_all_eqps()

        # 지정한 날짜 동안에 대한 데이터 조회
        for day in range(before_days):
            insert_list = []
            remove_list = []

            req_datetime = datetime.now() - timedelta(days=day) - TEST_TIME
            req_time = req_datetime.strftime("%Y%m%d")  # 오늘 날짜를 api 형식에 맞게 변형
            logger.info(f"{req_time}일차 데이터 조회")

            # 해당 날짜 Db 데이터 제거
            base_query = self.db.select_query(power_info)
            # query_add_filter = base_query.filter(power_info.ymdms.like(f"{req_time}%"))
            query_add_filter = base_query.filter(
                power_info.ymdms + timedelta(days=1) > req_datetime
            )
            old_data = self.db.get_obj_all(query_add_filter)
            print(f"old data : {len(old_data)}")

            # 장비 하나씩 데이터 조회
            for eqps_obj in eqps_list:
                # api로 데이터 받아오기
                data_list = self.api.fetch_elec(eqps_obj.site_id, eqps_obj.perf_id, req_time)
                # 받은 데이터를 하나씩 분리하여 저장
                for raw_data in data_list:
                    # 데이터 객체 생성
                    data = power_info(siteID=eqps_obj.site_id, **raw_data)
                    # 데이터 추가
                    insert_list.append(data)

                logger.info(f"elec 데이터 업데이트({day}) - 추가: {len(insert_list)}, 제거: {len(remove_list)}")
                # DB 데이터 추가 및 제거
                if remove_list:
                    self.db.delete(remove_list)
                    remove_list.clear()
                if insert_list:
                    self.db.insert_list(insert_list)
                    insert_list.clear()
                logger.info(f"api 정보 출력{self.api}")

    def ann_run_test(self):
        # 날짜 설정
        req_time = datetime.now() - TEST_TIME
        req_time = req_time.strftime("%Y%m%d")  # 오늘 날짜를 api 형식에 맞게 변형
        logger.info(f"{req_time}일차 데이터 조회")

        # 데이터 조회
        base_query = self.db.select_query(power_info)
        query_add_filter = base_query.filter_by(site_id='ace', perf_id=230)
        query_add_filter = query_add_filter.filter(power_info.ymdms.like(f"{req_time}%"))
        # 해당 데이터 모두 가져와서 dataframe으로 변환
        data = self.db.get_obj_all(query_add_filter)
        df = self.db.read_dataframe(query_add_filter)

        # print(f"data : {len(data)}")
        # print(len(data))
        x_dataset = df[['perf_id', 'ymdms', 'vol_tage', 'am_pere', 'ar_power', 'rat_power',
                        'pw_factor', 'accrue_power', 'voltager_s', 'voltages_t', 'voltaget_r', 'temperature']]
        y_dataset = df[['atv_power']]
        # print(f"x_dataset: {x_dataset}")
        # print(f"y_dataset: {y_dataset}")

        # 모델 학습
        self.ann.train(x_dataset, y_dataset)

        # 날짜 설정
        req_time = datetime.now() - TEST_TIME - timedelta(days=1)
        req_time = req_time.strftime("%Y%m%d")  # 오늘 날짜를 api 형식에 맞게 변형
        logger.info(f"{req_time}일차 데이터 조회")
        # 데이터 조회
        base_query = self.db.select_query(power_info)
        query_add_filter = base_query.filter_by(site_id='ace', perf_id=230)
        query_add_filter = query_add_filter.filter(power_info.ymdms.like(f"{req_time}%"))
        # 해당 데이터 모두 가져와서 dataframe으로 변환
        df = self.db.read_dataframe(query_add_filter)

        x_dataset = df[['perf_id', 'ymdms', 'vol_tage', 'am_pere', 'ar_power', 'rat_power',
                        'pw_factor', 'accrue_power', 'voltager_s', 'voltages_t', 'voltaget_r', 'temperature']]

        print("predict ------------------------------")
        y_predict = self.ann.predict(x_dataset)

        # 정수화
        y_dataset = df[['atv_power']]
        y_dataset['record'] = pandas.to_numeric(y_dataset['atv_power'])
        y_dataset['prediction'] = y_predict
        # self.ann.save_chart_img(y_predict=y_predict, y_test_dataset=y_dataset)
        self.ann.save_chart_img_line(y_dataset)

        print("model score ----------------------------------------------------------")
        # 날짜 설정
        req_time = datetime.now() - TEST_TIME - timedelta(days=2)
        req_time = req_time.strftime("%Y%m%d")  # 오늘 날짜를 api 형식에 맞게 변형
        logger.info(f"{req_time}일차 데이터 조회")
        # 데이터 조회
        base_query = self.db.select_query(power_info)
        query_add_filter = base_query.filter_by(site_id='ace', perf_id=230)
        query_add_filter = query_add_filter.filter(power_info.ymdms.like(f"{req_time}%"))
        df = self.db.read_dataframe(query_add_filter)
        x_dataset = df[['perf_id', 'ymdms', 'vol_tage', 'am_pere', 'ar_power', 'rat_power',
                        'pw_factor', 'accrue_power', 'voltager_s', 'voltages_t', 'voltaget_r', 'temperature']]
        y_dataset = df[['atv_power']]

        self.ann.model_score(x_dataset, y_dataset)

        # # 날짜 설정
        # req_time = datetime.now() - TEST_TIME - timedelta(days=1)
        # req_time = req_time.strftime("%Y%m%d")  # 오늘 날짜를 api 형식에 맞게 변형
        # logger.info(f"{req_time}일차 데이터 조회")
        # # 데이터 조회
        # base_query = self.db.select_query(power_info)
        # query_add_filter = base_query.filter_by(site_id='ace', perf_id=230)
        # query_add_filter = query_add_filter.filter(power_info.ymdms.like(f"{req_time}%"))
        # # 해당 데이터 모두 가져와서 dataframe으로 변환
        # df = self.db.read_dataframe(query_add_filter)
        #
        # x_dataset = df[['perf_id', 'ymdms', 'vol_tage', 'am_pere', 'ar_power', 'rat_power',
        #                 'pw_factor', 'accrue_power', 'voltager_s', 'voltages_t', 'voltaget_r', 'temperature']]
        # y_dataset = df[['atv_power']]
        # print(f"x_dataset: {x_dataset}")
        # print(f"y_dataset: {y_dataset}")
        # self.ann.model_score(x_dataset, y_dataset)
        #
        # self.ann.save_model()
        # print(f"first mode: {self.ann}")
        # tmp_ann = ANN_Sample_Model()
        # tmp_ann.load_model()
        # print(f"second model : {tmp_ann}")

    def get_ann_data(self, eqps_info: equipments_info, before_days=7):
        # 데이터 가져오기
        search_time = datetime.now() - timedelta(days=before_days)
        base_query = self.db.select_query(power_info)
        # 해당 장비 데이터만 선별
        base_query = base_query.filter_by(site_id=eqps_info.site_id, perf_id=eqps_info.perf_id)
        #
        base_query = base_query.filter(power_info.ymdms < search_time)
        result = self.db.read_dataframe(base_query)
        return result

    def get_ann_data_old(self, eqps_info: equipments_info, before_days=7):
        df_list = []
        # 데이터 가져오기
        for day in range(before_days):
            req_time = datetime.now() - timedelta(days=day) - TEST_TIME
            req_time = req_time.strftime("%Y%m%d")  # 오늘 날짜를 api 형식에 맞게 변형

            base_query = self.db.select_query(power_info)
            query_add_filter = base_query.filter_by(site_id=eqps_info.site_id, perf_id=eqps_info.perf_id)
            query_add_filter = query_add_filter.filter(power_info.ymdms.like(f"{req_time}%"))
            # 해당 데이터 모두 가져와서 dataframe으로 변환
            df = self.db.read_dataframe(query_add_filter)
            df_list.append(df)
        # 합치기
        main_df = pandas.concat(df_list)

        # logger.debug(f"main_df: {main_df.info()}")
        # 데이터 분리
        x_dataset = main_df[['perf_id', 'ymdms', 'vol_tage', 'am_pere', 'ar_power', 'rat_power',
                             'pw_factor', 'accrue_power', 'voltager_s', 'voltages_t', 'voltaget_r', 'temperature']]
        y_dataset = main_df[['ymdms', 'atv_power']]
        # 20200815000256
        y_dataset['ymdms'] = y_dataset['ymdms'].str[8:]

        result = {
            "x_dataset": x_dataset,
            "y_dataset": y_dataset,
        }
        return result

    def insert_predict(self, table_name, data):
        self.db.df_insert(df=data, table_name=table_name)
