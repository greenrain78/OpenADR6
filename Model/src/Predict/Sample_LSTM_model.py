import time

from keras.layers.core import Dense
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from pandas.core.frame import DataFrame
from sklearn import preprocessing

from sklearn.linear_model import LinearRegression
import logging
import pandas as pd

from src.Controller.ANN.ANN_Model import PredictBaseModel

logger = logging.getLogger(__name__)


class LSTMModel(PredictBaseModel):

    def __init__(self):
        self.model = Sequential()

    def train(self, train_X):
        # 훈련
        self.model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
        self.model.add(Dense(1))
        self.model.compile(loss='mae', optimizer='adam')
        logger.debug(self.model.coef_)

    def predict(self, input_data: pd.DataFrame):
        """
        """
        # 예측 수행
        y_predict = self.model.predict(input_data)
        # 데이터 출력
        logger.debug("predict")
        logger.debug(y_predict)
        return y_predict

    def processing_data_one(self, data_df):
        # 데이터 분리
        x_dataset = data_df[['perf_id', 'vol_tage', 'am_pere', 'ar_power', 'rat_power',
                             'pw_factor', 'accrue_power', 'voltager_s', 'voltages_t', 'voltaget_r', 'temperature']]
        values = x_dataset.values
        scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
        scaled = scaler.fit_transform(values)  # 값을 0~1로 떨어뜨린다
        reframed = self.series_to_supervised(scaled, 1, 1)  # t-1시점,t시점 데이터를 한 행으로 둔다

        values = reframed.values
        n_train_hours = 365 * 24  # 1년치 데이터만 가져온다
        train = values[:n_train_hours, :]
        # split into input and outputs
        train_X, train_y = train[:, :-1], train[:, -1]
        # reshape input to be 3D [samples, timesteps, features]
        train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))

        logger.info(f"processing_data_one scaled {type(train_X)} \n"
                    f"{train_X}")
        y_dataset = data_df[['atv_power']]
        # packing
        result = {
            "x_dataset": x_dataset,
            "y_dataset": y_dataset,
        }
        time.sleep(100000)
        return result

    def series_to_supervised(self, data, n_in=1, n_out=1, dropnan=True):
        n_vars = 1 if type(data) is list else data.shape[1]
        df = DataFrame(data)
        cols, names = list(), list()
        # input sequence (t-n, ... t-1)
        for i in range(n_in, 0, -1):
            cols.append(df.shift(i))
            names += [('var%d(t-%d)' % (j + 1, i)) for j in range(n_vars)]
        # forecast sequence (t, t+1, ... t+n)
        for i in range(0, n_out):
            cols.append(df.shift(-i))
            if i == 0:
                names += [('var%d(t)' % (j + 1)) for j in range(n_vars)]
            else:
                names += [('var%d(t+%d)' % (j + 1, i)) for j in range(n_vars)]
        # put it all together
        agg = pd.concat(cols, axis=1)
        agg.columns = names
        # drop rows with NaN values
        if dropnan:
            agg.dropna(inplace=True)
        return agg
