from abc import ABC, abstractmethod
from typing import List

from api.models.schemas.bot_user import BotUser


class BotUserRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[BotUser]:
        pass