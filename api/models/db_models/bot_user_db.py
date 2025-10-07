from sqlalchemy import Column, Integer, String, Float, DateTime

from api.models.db_models import Base


class BotUserDB(Base):
    __tablename__ = "bot_user"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=True)
    phone_no = Column(String(15), index=True)
    last_active = Column(DateTime)
    created_at = Column(DateTime)