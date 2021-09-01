import os
from datetime import timedelta

from src.Controller.env_import import get_env_bool

IS_DEBUG = get_env_bool('IS_DEBUG')
IS_RUN_TEST = get_env_bool('IS_RUN_TEST')
IS_RUN_SERVER = get_env_bool('IS_RUN_SERVER')

IS_SQL_ECHO = False
IS_MAIN_RUNNING = True

# 테스트 설정
IS_RUN_ALL_TEST = False
TEST_TIME = timedelta(days=365)

# 경로 설정
ANN_MODEL_SAVE_PATH = "file_data/ANN"
CHART_SAVE_PATH = "file_data/Chart"

# 사이트 리스트
siteId_list = ['ace', 'ncg', 'nci', 'ncp']  # 건물 추가시 수정

# 데이터 베이스 설정
DATABASES = {
    'default': {
        "database": os.environ.get('ADR_DB', 'openadr'),
        "user": os.environ.get('ADR_USER', 'user'),
        "password": os.environ.get('ADR_PASSWORD', '1234'),
        "host": os.environ.get('ADR_HOST', 'db'),
        "port": os.environ.get('ADR_PORT', '5432'),
    },
    'test': {
        "database": os.environ.get('ADR_DB', 'openadr'),
        "user": os.environ.get('ADR_USER', 'user'),
        "password": os.environ.get('ADR_PASSWORD', '1234'),
        "host": os.environ.get('TEST_HOST', 'db_test'),
        "port": os.environ.get('TEST_PORT', '5432'),
    }
}