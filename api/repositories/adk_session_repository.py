from abc import ABC, abstractmethod
from typing import List

from api.models.schemas.adk_session import ADKSession

class ADKSessionRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[ADKSession]:
        pass