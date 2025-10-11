from typing import List

from api.models.db_models.adk_session_db import ADKSessionDB
from api.models.schemas.adk_session import ADKSession
from api.repositories.adk_session_repository import ADKSessionRepository
from sqlalchemy.orm import Session


class AlchemyADKSessionRepository(ADKSessionRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[ADKSession]:
        query_sessions = self.session.query(ADKSessionDB)
        return [
            ADKSession.model_validate(query_session, from_attributes=True)
            for query_session in query_sessions.all()
        ]

    def get_session_by_user(self, bot_user) -> List[ADKSession]:
        query_sessions = self.session.query(ADKSessionDB)
        bot_user_obj = bot_user
        query_sessions = query_sessions.filter(
            ADKSessionDB.session_id == bot_user_obj[0].user_id
        )
        return [
            ADKSession.model_validate(query_session, from_attributes=True)
            for query_session in query_sessions.all()
        ]
