from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Agent(BaseModel):
    id: Optional[int] = None
    created_at: datetime
    contractor_id: int
