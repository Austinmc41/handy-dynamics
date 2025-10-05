from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv

from api.models.db_models.bot_user_db import Base
from api.repositories.alchemy_adk_session_repository import AlchemyADKSessionRepository
from api.repositories.alchemy_agent_repository import AlchemyAgentRepository
from api.repositories.alchemy_bot_user_respository import AlchemyBotUserRepository
from api.repositories.alchemy_contractor_repository import AlchemyContractorRepository

dotenv_path = Path('api/dependencies/.env')
load_dotenv(dotenv_path)

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_port = os.getenv("DB_PORT")

DATABASE_URL = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

def get_bot_user_repository() -> AlchemyBotUserRepository:
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return AlchemyBotUserRepository(Session())

def get_contractor_repository() -> AlchemyContractorRepository:
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return AlchemyContractorRepository(Session())

def get_agent_repository() -> AlchemyAgentRepository:
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return AlchemyAgentRepository(Session())


def get_adk_session_repository() -> AlchemyADKSessionRepository:
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return AlchemyADKSessionRepository(Session())
