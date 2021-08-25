from datetime import datetime

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String, Integer, DateTime

from src.DB.model.model_settings import Base


class power_info(Base):
    __tablename__ = "app_collect_power_info"
    id = Column(Integer, primary_key=True)
    site_id = Column(String)
    perf_id = Column(Integer)

    pn_name = Column(String)
    eqp_name = Column(String)
    ymdms = Column(DateTime)

    vol_tage = Column(String)
    am_pere = Column(String)
    ar_power = Column(String)
    atv_power = Column(String)
    rat_power = Column(String)
    pw_factor = Column(String)
    accrue_power = Column(String)
    voltager_s = Column(String)
    voltages_t = Column(String)
    voltaget_r = Column(String)
    temperature = Column(String)

    created_at = Column(DateTime)

    def __init__(self, siteID: str, perfId: int,
                 pnName: str, eqpName: str, ymdms: str,
                 volTage: str, amPere: str, arPower: str,
                 atvPower: str, ratPower: str, pwFactor: str,
                 accruePower: str, voltagerS: str, voltagesT: str,
                 voltagetR: str, temperature: str
                 ):
        self.site_id = siteID
        self.perf_id = int(perfId)
        self.pn_name = pnName
        self.eqp_name = eqpName
        self.ymdms = datetime.strptime(ymdms, "%Y%m%d%H%M%S")

        self.vol_tage = float(volTage)
        self.am_pere = float(amPere)
        self.ar_power = float(arPower)
        self.atv_power = float(atvPower)
        self.rat_power = float(ratPower)
        self.pw_factor = float(pwFactor)
        self.accrue_power = float(accruePower)
        self.voltager_s = float(voltagerS)
        self.voltages_t = float(voltagesT)
        self.voltaget_r = float(voltagetR)
        self.temperature = float(temperature)

        self.created_at = datetime.now()

    def __repr__(self):
        return f"<power_info({self.id}, {self.site_id}, {self.perf_id}, " \
               f"{self.pn_name}, {self.eqp_name}, {self.ymdms} " \
               f"{self.vol_tage}, {self.am_pere}, {self.ar_power} " \
               f"{self.atv_power}, {self.rat_power}, {self.pw_factor} " \
               f"{self.accrue_power}, {self.voltager_s}, {self.voltages_t} " \
               f"{self.voltaget_r}, {self.temperature}, " \
               f"{self.created_at})>"

    def __eq__(self, other):
        # 동일 객체인지 확인
        # 시간 요소 배제
        return self.site_id == other.site_id \
               and self.perf_id == other.perf_id \
               and self.pn_name == other.pn_name \
               and self.eqp_name == other.eqp_name \
               and self.ymdms == other.ymdms \
               and self.vol_tage == other.vol_tage \
               and self.am_pere == other.am_pere \
               and self.ar_power == other.ar_power \
               and self.atv_power == other.atv_power \
               and self.rat_power == other.rat_power \
               and self.pw_factor == other.pw_factor \
               and self.accrue_power == other.accrue_power \
               and self.voltager_s == other.voltager_s \
               and self.voltages_t == other.voltages_t \
               and self.voltaget_r == other.voltaget_r \
               and self.temperature == other.temperature
