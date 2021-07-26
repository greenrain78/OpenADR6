recent_date_range = 360
is_test_data = False  # api 데이터를 사용하지 않고 csv파일 데이터를 사용
predict_time = {
    "week": 1
}
train_time = {
    "minutes": 15
}
siteId_list = ['ace', 'ncg', 'nci', 'ncp']  # 건물 추가시 수정

using_db = "postgresql"

mariaDB = {
    "IP": "mariaDB",
    "ID": "user",
    "password": "1234",
    "db": "openadr",
    "port": 3306,
}

postgresql = {
    "IP": "db",
    "ID": "phaethon",
    "password": "phaethon",
    "db": "phaethon",
    "port": 5432,
}








