from sklearn.linear_model import LinearRegression
import logging
import pandas as pd

from src.Controller.ANN.ANN_Model import PredictBaseModel
logger = logging.getLogger(__name__)


class LinearRegressionModel(PredictBaseModel):

    def __init__(self):
        self.model = LinearRegression()

    def train(self, x_dataset, y_dataset):
        # 훈련

        self.model.fit(x_dataset, y_dataset)
        logger.debug("model train")
        # logger.debug(self.model.coef_)

    @add_schedule(second=34)
    def predict(self, input_data: pd.DataFrame):
        """
        """
        # 예측 수행
        y_predict = self.model.predict(input_data)
        # 데이터 출력
        logger.debug("predict")
        return y_predict


