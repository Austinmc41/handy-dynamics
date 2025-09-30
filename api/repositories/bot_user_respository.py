from abc import ABC, abstractmethod
from typing import List, Optional

from api.models.schemas.bot_user import BotUser


class BotUserRepository(ABC):
    @abstractmethod
    def get_all(self, phone_no: Optional[str] = None, name: Optional[str] = None) -> List[BotUser]:
        pass