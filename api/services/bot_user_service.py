from typing import List

from api.models.schemas.bot_user import BotUser
from api.repositories.bot_user_respository import BotUserRepository


class BotUserService:
    def __init__(self, repository: BotUserRepository):
        self.repository = repository

    def get_bot_users(self) -> List[BotUser]:
        return self.repository.get_all()
