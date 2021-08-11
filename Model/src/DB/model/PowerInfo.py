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
    ymdms = Column(String)

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
        self.perf_id = perfId
        self.pn_name = pnName
        self.eqp_name = eqpName
        self.ymdms = ymdms

        self.vol_tage = volTage
        self.am_pere = amPere
        self.ar_power = arPower
        self.atv_power = atvPower
        self.rat_power = ratPower
        self.pw_factor = pwFactor
        self.accrue_power = accruePower
        self.voltager_s = voltagerS
        self.voltages_t = voltagesT
        self.voltaget_r = voltagetR
        self.temperature = temperature

        self.created_at = datetime.now()

    def __repr__(self):
        return f"<equipments_info({self.id}, {self.site_id}, {self.perf_id}, " \
               f"{self.vol_tage}, {self.am_pere}, {self.ar_power} " \
               f"{self.atv_power}, {self.rat_power}, {self.pw_factor} " \
               f"{self.accrue_power}, {self.voltager_s}, {self.voltages_t} " \
               f"{self.voltaget_r}, {self.temperature}, " \
               f"{self.created_at})>"
