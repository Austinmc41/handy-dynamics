from typing import List

from api.models.db_models.bot_user_db import BotUserDB
from api.models.schemas.bot_user import BotUser
from api.repositories.bot_user_respository import BotUserRepository
from sqlalchemy.orm import Session


class AlchemyBotUserRepository(BotUserRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[BotUser]:
        query = self.session.query(BotUserDB)
        bot_user_db = query.all()
        return [BotUser.model_validate(b) for b in bot_user_db]
