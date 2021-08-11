from datetime import datetime
from logging import getLogger

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String, Integer, DateTime

from src.DB.model.model_settings import Base

logger = getLogger(__name__)


class equipments_info(Base):
    __tablename__ = "app_collect_equipments_info"
    id = Column(Integer, primary_key=True)
    site_id = Column(String)
    perf_id = Column(Integer)

    eqp_code = Column(String)
    eqp_name = Column(String)
    eqp_type = Column(String)

    created_at = Column(DateTime)

    def __init__(self, siteID: str, perfId: int,
                 eqpCode: str, eqpName: str, eqpType: str
                 ):
        try:
            self.site_id = siteID
            self.perf_id = int(perfId)

            self.eqp_code = eqpCode
            self.eqp_name = eqpName
            self.eqp_type = eqpType

            self.created_at = datetime.now()
        except ValueError as verr:
            logger.error(f"{verr}: 입력 값이 잘못되었습니다.\n"
                         f"siteID: {siteID}, perfId: {perfId}, eqpCode: {eqpCode}, "
                         f"eqpName: {eqpName}, eqpType: {eqpType}")
            raise ValueError(f"equipments_info init error : {self}")

    def __repr__(self):
        return f"<equipments_info({self.id}, {self.site_id}, {self.perf_id}, " \
               f"{self.eqp_code}, {self.eqp_name}, {self.eqp_type}, " \
               f"{self.created_at})>"

    def __eq__(self, other):
        # 동일 객체인지 확인
        if self.site_id != other.site_id:
            return False
        if self.perf_id != other.perf_id:
            return False
        if self.eqp_code != other.eqp_code:
            return False
        if self.eqp_name != other.eqp_name:
            return False
        if self.eqp_type != other.eqp_type:
            return False
        return True

