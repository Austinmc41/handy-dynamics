from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class Contractor(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    created_at: datetime
    email: str
    phone_no: str
