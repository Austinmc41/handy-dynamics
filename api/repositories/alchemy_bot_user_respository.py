from typing import List, Optional

from sqlalchemy import and_

from api.models.db_models.bot_user_db import BotUserDB
from api.models.schemas.bot_user import BotUser
from api.repositories.bot_user_respository import BotUserRepository
from sqlalchemy.orm import Session


class AlchemyBotUserRepository(BotUserRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self, phone_no: Optional[str] = None, name: Optional[str] = None) -> List[BotUser]:
        query_users = self.session.query(BotUserDB)
        filters = []

        if phone_no:
            filters.append(BotUserDB.phone_no == phone_no)

        if name:
            filters.append(BotUserDB.name.ilike(f"%{name}%"))

        query_users = query_users.filter(and_(*filters))

        return [BotUser.model_validate(query_user, from_attributes=True) for query_user in query_users.all()]