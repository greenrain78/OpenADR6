from src.Controller.ANN.Chart_Maker import ChartMaker
from src.Controller.API.adr_api_client import ADR_API_Client
from src.DB.DB_Adapter import DBAdapter
from src.Engine.DataEngine import DataEngine

import pandas


class MainEngine:

    def __init__(self, data_engine: DataEngine):
        # DB 데이터 입출력
        self.data_engine = data_engine
        self.chart_maker = ChartMaker()

    def ann_run_test(self):
        # 장비 리스트 갱신
        self.data_engine.update_eqps()
        # 장비 정보 업데이트
        self.data_engine.update_elec_remove_all()

        # 장비 데이터 가져오기
        eqps_list = self.data_engine.get_all_eqps()
        # eqps_obj = eqps_list[0]
        chart_data_list = []
        for eqps_obj in eqps_list:
            print(f"MainEngine: eqps_obj: {eqps_obj}")

            # 데이터 검색
            data = self.data_engine.get_ann_data(eqps_obj)
            print(f"MainEngine: {data}")
            chart_data = data['y_dataset'].astype(float)
            chart_data_list.append(chart_data)
        result_chart_data = pandas.concat(chart_data_list)

        self.chart_maker.df_to_line_chart(result_chart_data, "raw_data_chart1")

            # ann 학습

        # 검증
