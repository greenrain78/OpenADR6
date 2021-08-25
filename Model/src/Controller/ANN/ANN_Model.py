import pickle
import logging
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

from settings import ANN_MODEL_SAVE_PATH


class PredictBaseModel:
    pass


class ANN_Sample_Model(PredictBaseModel):

    def __init__(self):
        self.model = LinearRegression()

    def train(self, x_dataset, y_dataset):
        # 훈련

        self.model.fit(x_dataset, y_dataset)
        logger.debug(self.model.coef_)

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.model}\n" \
               f"{self.model.coef_}"

    def model_score(self, x_dataset, y_dataset):
        # 예측
        # y_predict = model.predict(x_test_dataset)

        logger.info(self.model.coef_)
        logger.info(self.model.score(x_dataset, y_dataset))

    def predict(self, input_data: pd.DataFrame):
        """
        """
        # 예측 수행
        y_predict = self.model.predict(input_data)
        # 데이터 출력
        logger.debug("predict")
        logger.debug(y_predict)
        return y_predict

    def save_model(self, filename="model_save1"):
        # 모델 저장
        # joblib(model, 'model_save1.pkl') # 오류로 해당 모듈을 사용 불가
        with open(f'{ANN_MODEL_SAVE_PATH}/{filename}.pkl', 'wb') as model_file:
            pickle.dump(self.model, model_file)

    def load_model(self, filename="model_save1"):
        # 모델 불러오기
        self.model = joblib.load(f'{ANN_MODEL_SAVE_PATH}/{filename}.pkl')
