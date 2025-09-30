from sqlalchemy import Column, Integer, DateTime
from api.models.db_models.bot_user_db import Base


class BotUserDB(Base):
    __tablename__ = "adk_session"
    session_id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime)
    last_active = Column(DateTime)

