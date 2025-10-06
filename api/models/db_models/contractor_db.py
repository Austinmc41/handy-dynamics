from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column

from api.models.db_models.agent_db import AgentDB
from api.models.db_models.bot_user_db import Base


class ContractorDB(Base):
    __tablename__ = "contractor"
    contractor_id = mapped_column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=True)
    created_at = Column(DateTime)
    email = Column(String(100))
    phone_no = Column(String(15), index=True)

    agent: Mapped["AgentDB"] = relationship(back_populates="contractor")
