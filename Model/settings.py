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
    "ID": "user",
    "password": "1234",
    "db": "openadr",
    "port": 5432,
}

db_table_name_elec = {
    "name": "app_collect_equipments_info",
    "raw_column": ["siteID", 'perfId', 'eqpCode', 'eqpName', 'eqpType'],
    "column": ["site_id", "perf_id", "eqp_code", "eqp_name", "eqp_type", "created_at"]

}
db_table_name_eqps = {
    "name": "app_collect_power_info",
    "raw_column": ['perfId', 'pnName', 'eqpName', 'ymdms', 'volTage', 'amPere', 'arPower', 'atvPower',
                   'ratPower', 'pwFactor', 'accruePower', 'voltagerS', 'voltagesT', 'voltagetR', 'temperature'],
    "column": ["site_id", "perf_id", "pn_name", "eqp_name", "ymdms", "vol_tage", "am_pere", "ar_power", "atv_power",
               "rat_power", "pw_factor", "accrue_power", "voltager_s", "voltages_t", "voltaget_r", "temperature",
               "created_at"]

}

