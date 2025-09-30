from typing import List, Annotated, Optional

import uvicorn
from fastapi import FastAPI
from fastapi.params import Depends

from api.dependencies.dependencies import get_sqlalchemy_repository
from api.models.schemas.bot_user import BotUser
from api.services.bot_user_service import BotUserService

app = FastAPI()

@app.get('/bot_users/', response_model=List[BotUser])
def get_bot_users(phone_no: Optional[str] = None, name: Optional[str] = None, repo = Depends(get_sqlalchemy_repository)):
    service = BotUserService(repo)
    return service.get_bot_users(phone_no=phone_no, name=name)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
