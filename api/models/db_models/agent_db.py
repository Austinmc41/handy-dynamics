from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AgentDB(Base):
    __tablename__ = "agent"
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime)
    contractor_id = Column(Integer)