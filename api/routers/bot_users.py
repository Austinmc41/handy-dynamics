from typing import List, Optional

from fastapi import APIRouter
from fastapi.params import Depends

from api.dependencies.dependencies import get_bot_user_repository
from api.models.schemas.bot_user import BotUser
from api.services.bot_user_service import BotUserService

router = APIRouter(
    prefix="/bot_users",
    tags=["bot_users"],
)


@router.get("/", response_model=List[BotUser])
def get_bot_users(
    phone_no: Optional[str] = None,
    name: Optional[str] = None,
    repo=Depends(get_bot_user_repository),
):
    service = BotUserService(repo)
    return service.get_bot_users(phone_no=phone_no, name=name)
