from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, relationship, mapped_column

from api.models.db_models.contractor_db import ContractorDB

Base = declarative_base()

class AgentDB(Base):
    __tablename__ = "agent"
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime)
    contractor_id : Mapped[int] = mapped_column(ForeignKey("contractor.contractor_id"))

    contractor: Mapped["ContractorDB"] = relationship(back_populates="agent")