from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv

from api.models.db_models.bot_user_db import Base
from api.repositories.alchemy_bot_user_respository import AlchemyBotUserRepository

dotenv_path = Path('api/dependencies/.env')
load_dotenv(dotenv_path)

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_port = os.getenv("DB_PORT")

DATABASE_URL = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

# @todo # get user, password and format engine to proper url
def get_sqlalchemy_repository() -> AlchemyBotUserRepository:
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return AlchemyBotUserRepository(Session())