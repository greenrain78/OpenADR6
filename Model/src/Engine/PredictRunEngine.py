import time
from datetime import datetime, timedelta
from logging import getLogger

from pandas.core.frame import DataFrame

from src.Controller.ANN.Chart_Maker import ChartMaker
from src.Controller.Schedule.schedule_manager import add_schedule
from src.DB.model.EquipInfo import equipments_info
from src.DB.model.PowerInfo import power_info
from src.Engine.DataEngine import DataEngine
from src.Predict.Sample_LR_model import LinearRegressionModel
from src.Predict.Sample_LSTM_model import LSTMModel

logger = getLogger(__name__)


class PredictControllerEngine:

    def __init__(self):
        logger.info("PredictControllerEngine init")
        # DB 데이터 입출력
        self.data_engine = DataEngine()
        self.chart_maker = ChartMaker()
        self.lstm_model = LSTMModel()
        self.lr_model = LinearRegressionModel()

    def run_LSTM_model(self):
        logger.info(f"run LSTMModel")
        eqps_list = self.data_engine.get_all_eqps()[:10]
        for i, eqps_obj in enumerate(eqps_list):
            print(f"MainEngine: eqps_obj({len(eqps_list) - i}): {eqps_obj}")

            # 데이터 검색 - 7일치
            data = self.processing_data_by_model(eqps_obj)
            x_data = data['x_dataset']
            record_data = data['y_dataset']
            # self.chart_maker.df_to_line_chart()
            if i > 1 and not x_data.empty:
                print(x_data)
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                predict_data = self.lstm_model.predict(x_data)
                logger.info(f"predict_data({type(predict_data)})\n"
                            f"{predict_data}")
            self.lstm_model.train(x_data)

    def processing_data_by_model(self, eqps_obj):
        data_df = self.data_engine.get_ann_data(eqps_obj)
        data = self.lstm_model.processing_data_one(data_df)
        return data

    # # @add_schedule(second=34)
    def run_LR_model(self):
        logger.info(f"run LinearRegressionModel")
        chart_data_list = []
        eqps_list = self.data_engine.get_all_eqps()[:10]
        for i, eqps_obj in enumerate(eqps_list):
            print(f"MainEngine: eqps_obj({len(eqps_list) - i}): {eqps_obj}")

            # 데이터 검색 - 7일치
            data = self.processing_data_one(eqps_obj)
            x_data = data['x_dataset']
            record_data = data['y_dataset']
            # self.chart_maker.df_to_line_chart()
            if not x_data.empty:
                if i > 1:
                    print(f"x_data :{x_data}")
                    predict_data = self.lr_model.predict(x_data)
                    result = x_data
                    result['predict'] = predict_data
                    self.insert_data(result, site_id=eqps_obj.site_id)
                    # logger.info(f"predict_data({type(predict_data)})\n"
                    #             f"{predict_data}")

                self.lr_model.train(x_data, record_data)

    def insert_data(self, data, site_id):
        """
        predict_atv_power
        :param data:
        :return:
        """
        data['site_id'] = site_id

    def processing_data_one(self, eqps_obj):
        data_df = self.data_engine.get_ann_data(eqps_obj)

        # 데이터 분리
        x_dataset = data_df[['perf_id', 'vol_tage', 'am_pere', 'ar_power', 'rat_power',
                             'pw_factor', 'accrue_power', 'voltager_s', 'voltages_t', 'voltaget_r', 'temperature']]

        # # 날짜 정수화
        # ymdms_data = x_dataset['ymdms'].apply(lambda x: time.mktime(x.timetuple()))
        # x_dataset['ymdms'] = ymdms_data
        #
        y_dataset = data_df[['atv_power']]
        # packing
        result = {
            "x_dataset": x_dataset,
            "y_dataset": y_dataset,
        }
        return result
