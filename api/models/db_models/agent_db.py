from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from api.models.db_models import Base


class AgentDB(Base):
    __tablename__ = "agent"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    created_at = Column(DateTime)
    contractor_id: Mapped[int] = mapped_column(ForeignKey("contractor.id"))

    contractor = relationship("ContractorDB", back_populates="agent")
