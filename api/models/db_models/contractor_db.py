from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, mapped_column

from api.models.db_models import Base

class ContractorDB(Base):
    __tablename__ = "contractor"
    id = mapped_column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), nullable=True)
    created_at = Column(DateTime)
    email = Column(String(100))
    phone_no = Column(String(15), index=True)

    agent = relationship("AgentDB", back_populates="contractor")
