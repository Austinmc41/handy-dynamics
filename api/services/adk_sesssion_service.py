from typing import List

from api.models.schemas.adk_session import ADKSession
from api.repositories.adk_session_repository import ADKSessionRepository

class ADKSessionService:
    def __init__(self, repository: ADKSessionRepository):
        self.repository = repository

    def get_adk_sessions(self) -> List[ADKSession]:
        return self.repository.get_all()
