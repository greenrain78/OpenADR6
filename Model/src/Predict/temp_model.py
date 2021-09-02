import logging
from datetime import datetime

import pandas as pd

from src.Controller.ANN.ANN_Model import PredictBaseModel
from src.Controller.Schedule.schedule_manager import add_schedule

logger = logging.getLogger(__name__)


class TempModel(PredictBaseModel):

    def __init__(self):
        self.model = None

    def train(self, x_dataset, y_dataset):
        # 훈련
        pass

    # @add_schedule(second=34)
    def predict(self, input_data: pd.DataFrame):
        """
        """
        # time_start = datetime.
        y_predict = pd.DataFrame()
        # 예측 수행
        select_data = input_data[['site_id', 'perf_id', 'ymdms', 'atv_power']]

        # 모델 이름 추가
        y_predict.insert(3, "model_name", "TempModel")
        y_predict.insert(3, "predict_cycle", "15 minute")
        y_predict.insert(3, "predict_range", "24 hour")
        y_predict.insert(3, "predict_interval", "15 minute")
        # y_predict.loc['2019-06-1':'2020-02-05']

        y_predict.insert(3, "created_at", datetime.now())
        print(y_predict)

        # 데이터 출력
        logger.debug("predict")
        return y_predict

