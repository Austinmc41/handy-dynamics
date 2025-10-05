from sqlalchemy import Column, Integer, String, DateTime

from api.models.db_models.bot_user_db import Base


class ContractorDB(Base):
    __tablename__ = "contractor"
    contractor_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=True)
    created_at = Column(DateTime)
    email = Column(String(100))
    phone_no = Column(String(15), index=True)
