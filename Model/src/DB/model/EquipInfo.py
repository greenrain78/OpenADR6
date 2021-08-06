from datetime import datetime

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String, Integer, DateTime

from src.DB.model.model_settings import Base


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
        self.site_id = siteID
        self.perf_id = perfId

        self.eqp_code = eqpCode
        self.eqp_name = eqpName
        self.eqp_type = eqpType

        self.created_at = datetime.now()


