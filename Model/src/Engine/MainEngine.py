from time import sleep

from src.Controller.ANN.Chart_Maker import ChartMaker
from src.Controller.API.adr_api_client import ADR_API_Client
from src.Controller.Schedule.schedule_manager import add_schedule
from src.DB.DB_Adapter import DBAdapter
from src.Engine.DataEngine import DataEngine

import pandas
import logging

from src.Predict.temp_model import TempModel

logger = logging.getLogger(__name__)


class MainEngine:

    def __init__(self, data_engine: DataEngine):
        # DB 데이터 입출력
        self.data_engine = data_engine
        self.chart_maker = ChartMaker()
        self.temp_model = TempModel()

    def test_run(self):
        eqps_list = self.data_engine.get_all_eqps()
        for i, eqps_obj in enumerate(eqps_list):
            print(f"MainEngine: eqps_obj({len(eqps_list) - i}): {eqps_obj}")

            # 데이터 검색 - 7일치
            data = self.data_engine.get_ann_data(eqps_obj)
            result = self.temp_model.predict(data)
            print(result)
            self.data_engine.insert_predict("app_expect_predict_atv_power", result)


    def ann_train_test(self):
        logger.info(f"run ann_train_test")
        eqps_list = self.data_engine.get_all_eqps()[:10]
        for i, eqps_obj in enumerate(eqps_list):
            print(f"MainEngine: eqps_obj({len(eqps_list) - i}): {eqps_obj}")

            # 데이터 검색 - 7일치
            data = self.data_engine.get_ann_data(eqps_obj)
            x_data = data['x_dataset']
            record_data = data['y_dataset']
            # self.ann_model.train(x_data, record_data)

    def api_chart_test(self):
        # 특정 상황에만 활성화
        # 장비 리스트 갱신
        # self.data_engine.update_eqps()
        # # 장비 정보 업데이트
        # self.data_engine.update_elec_remove_all()

        # 장비 데이터 가져오기
        eqps_list = self.data_engine.get_all_eqps()[:10]
        # eqps_obj = eqps_list[0]
        chart_data_list = []
        for i, eqps_obj in enumerate(eqps_list):
            print(f"MainEngine: eqps_obj({len(eqps_list) - i}): {eqps_obj}")

            # 데이터 검색 - 7일치
            data = self.data_engine.get_ann_data(eqps_obj)
            chart_data = data['y_dataset']
            chart_data['ymdms'] = pandas.to_datetime(chart_data['ymdms'], format="%H%M%S").dt.time
            chart_data['atv_power'] = chart_data['atv_power'].astype(float)

            chart_data_list.append(chart_data)

        result_chart_data = pandas.concat(chart_data_list, axis=1)

        print(f"MainEngine: {result_chart_data}")
        self.chart_maker.df_to_scatter_chart(result_chart_data, 'ymdms', 'atv_power',
                                             filename="raw_data_scatter_chart2")

        # line chart
        # chart_line_data = chart_data_list
        # logger.info(f"chart_data({type(chart_line_data)})")
        # for i in chart_line_data:
        #     print(i)
        #     print(i.info())
        # self.chart_maker.multi_line_chart(chart_line_data, filename="raw_data_line_ymd_chart1")
        #
        # # ann 학습

        # 검증
