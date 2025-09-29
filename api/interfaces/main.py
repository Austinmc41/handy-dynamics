from typing import List

from fastapi import FastAPI
from fastapi.params import Depends

from api.dependencies.dependencies import get_sqlalchemy_repository
from api.models.schemas.bot_user import BotUser
from api.services.bot_user_service import BotUserService

app = FastAPI()

@app.get('/bot_users/', response_model=List[BotUser])
def get_bot_users(repo = Depends(get_sqlalchemy_repository)):
    service = BotUserService(repo) # warning here might be something
    return service.get_bot_users()
