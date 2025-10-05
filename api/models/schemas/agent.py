from datetime import datetime
from pydantic import BaseModel


class Agent(BaseModel):
    id: int
    created_at: datetime
    contractor_id: int