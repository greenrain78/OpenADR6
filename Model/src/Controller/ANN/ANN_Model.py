import logging
import pickle
import joblib

from settings import ANN_MODEL_SAVE_PATH

logger = logging.getLogger(__name__)


class PredictBaseModel:
    filename = "undefined_name"
    model = None

    def save_model(self):
        # 모델 저장
        # joblib(model, 'model_save1.pkl') # 오류로 해당 모듈을 사용 불가
        with open(f'{ANN_MODEL_SAVE_PATH}/{self.filename}.pkl', 'wb') as model_file:
            pickle.dump(self.model, model_file)

    def load_model(self, filename="model_save1"):
        # 모델 불러오기
        self.model = joblib.load(f'{ANN_MODEL_SAVE_PATH}/{self.filename}.pkl')

    def model_score(self, x_dataset, y_dataset):
        # 예측
        logger.info(self.model.score(x_dataset, y_dataset))

    def __repr__(self):
        return f"{self.__class__.__name__} - {type(self).__name__}\n" \
               f"기울기: {self.model.coef_}\n" \
               f"파일 이름: {self.filename}\n" \
               f"모델: {self.model}"
