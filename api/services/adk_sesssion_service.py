from typing import List

from api.models.schemas.adk_session import ADKSession
from api.repositories.adk_session_repository import ADKSessionRepository
from api.repositories.bot_user_respository import BotUserRepository


class ADKSessionService:
    def __init__(self, adk_repository: ADKSessionRepository):
        self.adk_repository = adk_repository

    def get_adk_sessions(self) -> List[ADKSession]:
        return self.adk_repository.get_all()

    def get_adk_session_by_phone(self, phone_no, bot_user_repo: BotUserRepository):
        bot_user = bot_user_repo.get_all(phone_no=phone_no)
        return self.adk_repository.get_session_by_user(bot_user)


