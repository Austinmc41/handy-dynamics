from abc import ABC, abstractmethod
from typing import List, Optional

from api.models.schemas.contractor import Contractor


class ContractorRepository(ABC):
    @abstractmethod
    def get_all(self, phone_no: Optional[str] = None, name: Optional[str] = None) -> List[Contractor]:
        pass