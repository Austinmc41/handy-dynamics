from pydantic import BaseModel
from datetime import datetime

class BotUser(BaseModel):
    user_id: int
    name: str
    phone_no: str
    last_active: datetime
    created_at: datetime
