from typing import List, Optional

from api.models.schemas.bot_user import BotUser
from api.repositories.bot_user_respository import BotUserRepository


class BotUserService:
    def __init__(self, repository: BotUserRepository):
        self.repository = repository

    def get_bot_users(
        self, phone_no: Optional[str] = None, name: Optional[str] = None
    ) -> List[BotUser]:
        return self.repository.get_all(phone_no=phone_no, name=name)
