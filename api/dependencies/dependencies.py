from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.models.db_models.bot_user_db import Base
from api.repositories.alchemy_bot_user_respository import AlchemyBotUserRepository


# @todo # get user, password and format engine to proper url
def get_sqlalchemy_repository() -> AlchemyBotUserRepository:
    engine = create_engine("sqlite:///products.db")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return AlchemyBotUserRepository(Session())