import pickle

import matplotlib.pyplot as plt

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

from settings import ANN_MODEL_SAVE_PATH


class ANN_Sample_Model:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, x_dataset, y_dataset):
        # 훈련

        self.model.fit(x_dataset, y_dataset)
        print(self.model.coef_)

    def __repr__(self):
        return f"ANN_Sample_Model: {self.model}\n" \
               f"{self.model.coef_}"

    def model_score(self, x_dataset, y_dataset):
        # 예측
        # y_predict = model.predict(x_test_dataset)

        print(self.model.coef_)
        print(self.model.score(x_dataset, y_dataset))

    def predict(self, input_data: pd.DataFrame):
        """
        """
        # 예측 수행
        y_predict = self.model.predict(input_data)
        y_predict = pd.DataFrame(y_predict)
        # 데이터 출력
        print("predict")
        print(y_predict)
        return y_predict

    def save_chart_img(self, y_predict, y_test_dataset):
        print(f"y_predict - {type(y_predict)} - {len(y_predict)}\n {y_predict}")
        print(f"y_test_dataset - {type(y_test_dataset)} - {len(y_test_dataset)}\n {y_test_dataset}")

        # 그래프
        # plt.scatter(y_predict, y_test_dataset, alpha=0.4)
        # 빨간 대쉬, 파란 사각형, 녹색 삼각형
        # plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
        plt.xlabel("Actual")
        plt.ylabel("Predicted")
        plt.title("test code")
        plt.show()
        plt.savefig(f'{ANN_MODEL_SAVE_PATH}/fig1.png', dpi=300)

    def save_model(self, filename="model_save1"):
        # 모델 저장
        # joblib(model, 'model_save1.pkl') # 오류로 해당 모듈을 사용 불가
        with open(f'{ANN_MODEL_SAVE_PATH}/{filename}.pkl', 'wb') as model_file:
            pickle.dump(self.model, model_file)

    def load_model(self, filename="model_save1"):
        # 모델 불러오기
        self.model = joblib.load(f'{ANN_MODEL_SAVE_PATH}/{filename}.pkl')

