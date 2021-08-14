import pickle

import pandas as pandas
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

from settings import ANN_MODEL_SAVE_PATH


class ANN_Sample_Model:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, x_dataset, y_dataset):
        # 훈련

        self.model.fit(x_dataset, y_dataset)
        print(self.model.coef_)

    def save(self):
        # 모델 저장
        # joblib(model, 'model_save1.pkl') # 오류로 해당 모듈을 사용 불가
        with open(f'{ANN_MODEL_SAVE_PATH}/model_save1.pkl', 'wb') as model_file:
            pickle.dump(self.model, model_file)

    def model_score(self, x_dataset, y_dataset):
        # 예측
        # y_predict = model.predict(x_test_dataset)

        print(self.model.coef_)
        print(self.model.score(x_dataset, y_dataset))

    def predict(self, input_data: pd.DataFrame):
        """:arg
        """
        # 그런데 읽는것은 정상적으로 수행
        model = joblib.load('model_save1.pkl')

        score_dataset = pd.read_csv('ANN/api_sample_data_0308.csv', encoding='utf-8')  # 20210307 데이터
        x_score_dataset = score_dataset[['ymdms', 'volTage', 'amPere', 'arPower', 'ratPower',
                                         'pwFactor', 'accruePower', 'voltagerS', 'voltagesT', 'voltagetR',
                                         'temperature']]
        y_score_dataset = score_dataset[['atvPower']]
        print("predict")
        print(model.coef_)
        print(model.score(x_score_dataset, y_score_dataset))

    def save_model(self, model):
        pass

    def load_model(self, model):
        pass
