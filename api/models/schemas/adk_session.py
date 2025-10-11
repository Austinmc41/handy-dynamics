from datetime import datetime
from pydantic import BaseModel


class ADKSession(BaseModel):
    session_id: int
    created_at: datetime
    last_active: datetime
