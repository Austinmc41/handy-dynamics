from typing import List, Optional

from api.models.db_models.contractor_db import ContractorDB
from api.models.schemas.contractor import Contractor
from sqlalchemy.orm import Session

from api.repositories.contractor_repository import ContractorRepository


class AlchemyContractorRepository(ContractorRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self, phone_no: Optional[str] = None, name: Optional[str] = None) -> List[Contractor]:
        query_contractors = self.session.query(ContractorDB)
        return [Contractor.model_validate(query_contractor, from_attributes=True) for query_contractor in query_contractors.all()]