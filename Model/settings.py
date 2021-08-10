import os

IS_SQL_ECHO = True
predict_time = {
    "week": 1
}
train_time = {
    "minutes": 15
}
siteId_list = ['ace', 'ncg', 'nci', 'ncp']  # 건물 추가시 수정

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