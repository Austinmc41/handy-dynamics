from typing import List

import uvicorn
from fastapi import FastAPI
from fastapi.params import Depends
import sys
import os

# print("Current Working Directory:", os.getcwd())
# print("Python Module Search Path (sys.path):")
# for path in sys.path:
#     print(path)
#

from api.dependencies.dependencies import get_sqlalchemy_repository
from api.models.schemas.bot_user import BotUser
from api.services.bot_user_service import BotUserService

app = FastAPI()

@app.get('/bot_users/', response_model=List[BotUser])
def get_bot_users(repo = Depends(get_sqlalchemy_repository)):
    service = BotUserService(repo) # warning here might be something
    return service.get_bot_users()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
