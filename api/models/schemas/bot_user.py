from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class BotUser(BaseModel):
    user_id: int
    name: Optional[str] = None
    phone_no: str
    last_active: datetime
    created_at: datetime

    model_config = ConfigDict(from_attributes=True, extra='ignore')