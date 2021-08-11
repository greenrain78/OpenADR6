from datetime import datetime

from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, DateTime, Boolean
from sqlalchemy.orm import relationship

from src.DB.model.PowerInfo import power_info
from src.DB.model.model_settings import Base


class power_update(Base):
    __tablename__ = "app_collect_power_update"
    id = Column(Integer, primary_key=True)
    site_id = Column(String)

    ymdms = Column(String)
    is_updated = Column(Boolean)

    created_at = Column(DateTime)

    def __init__(self, site_id: str, perf_id: int,
                 ymdms: str, is_updated: bool, elec: power_info
                 ):
        self.site_id = site_id
        self.perf_id = perf_id

        self.ymdms = ymdms
        self.is_updated = is_updated
        self.elec = elec

        self.created_at = datetime.now()

    def __repr__(self):
        return f"<equipments_info({self.id}, {self.site_id}, {self.perf_id}, " \
               f"{self.eqp_code}, {self.eqp_name}, {self.eqp_type} " \
               f"{self.created_at})>"
