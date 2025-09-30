from abc import ABC, abstractmethod
from typing import List

from api.models.schemas.adk_session import ADKSession
from api.models.schemas.bot_user import BotUser

class ADKSessionRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[ADKSession]:
        pass

    @abstractmethod
    def get_session_by_user(self, bot_user: List[BotUser]) -> List[ADKSession]:
       pass

