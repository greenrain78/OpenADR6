import pickle

import pandas as pandas
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib


def train():
    # load data
    dataset = pd.read_csv('ANN/api_sample_data_0307.csv', encoding='utf-8')  # 20210307 데이터
    test_dataset = pd.read_csv('ANN/api_sample_data_0308.csv', encoding='utf-8')  # 20210307 데이터
    score_dataset = pd.read_csv('ANN/api_sample_data_0308.csv', encoding='utf-8')  # 20210307 데이터

    x_dataset = dataset[['ymdms', 'volTage', 'amPere', 'arPower', 'ratPower',
                         'pwFactor', 'accruePower', 'voltagerS', 'voltagesT', 'voltagetR', 'temperature']]
    y_dataset = dataset[['atvPower']]

    x_test_dataset = test_dataset[['ymdms', 'volTage', 'amPere', 'arPower', 'ratPower',
                                   'pwFactor', 'accruePower', 'voltagerS', 'voltagesT', 'voltagetR', 'temperature']]
    y_test_dataset = test_dataset[['atvPower']]

    x_score_dataset = score_dataset[['ymdms', 'volTage', 'amPere', 'arPower', 'ratPower',
                                     'pwFactor', 'accruePower', 'voltagerS', 'voltagesT', 'voltagetR', 'temperature']]
    y_score_dataset = score_dataset[['atvPower']]

    # 훈련
    model = LinearRegression()
    model.fit(x_dataset, y_dataset)

    # 예측
    y_predict = model.predict(x_test_dataset)

    print("train1")
    print(model.coef_)
    print(model.score(x_score_dataset, y_score_dataset))

    # joblib(model, 'model_save1.pkl') # 오류로 해당 모듈을 사용 불가
    with open('model_save1.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)


def predict(input_data: pd.DataFrame):
    """:arg
    """
    # 그런데 읽는것은 정상적으로 수행
    model = joblib.load('model_save1.pkl')

    score_dataset = pd.read_csv('ANN/api_sample_data_0308.csv', encoding='utf-8')  # 20210307 데이터
    x_score_dataset = score_dataset[['ymdms', 'volTage', 'amPere', 'arPower', 'ratPower',
                                     'pwFactor', 'accruePower', 'voltagerS', 'voltagesT', 'voltagetR', 'temperature']]
    y_score_dataset = score_dataset[['atvPower']]
    print("predict")
    print(model.coef_)
    print(model.score(x_score_dataset, y_score_dataset))


def save_model(model):
    pass


def load_model(model):
    pass