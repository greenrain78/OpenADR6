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

        # 데이터 출력
        print("predict")
        print(y_predict)

        # 그래프
        plt.scatter(y_test_dataset, y_predict, alpha=0.4)
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

