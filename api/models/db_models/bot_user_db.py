from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BotUserDB(Base):
    __tablename__ = "bot_user"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    phone_no = Column(String(15), index=True)
    last_active = Column(DateTime)
    created_at = Column(DateTime)

