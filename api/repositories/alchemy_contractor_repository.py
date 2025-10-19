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

    def add(self, contractor: Contractor) -> Contractor:
        contractor_db = ContractorDB(**contractor.dict())
        self.session.add(contractor_db)
        self.session.commit()
        self.session.refresh(contractor_db)
        return Contractor.model_validate(contractor_db, from_attributes=True)

    def get_by_id(self, contractor_id: int) -> Optional[Contractor]:
        contractor_db = self.session.query(ContractorDB).get(contractor_id)
        if contractor_db:
            return Contractor.model_validate(contractor_db, from_attributes=True)
        return None

    def update(self, contractor: Contractor):
        contractor_db = self.session.query(ContractorDB).get(contractor.id)
        if contractor_db:
            contractor_db.name = contractor.name
            contractor_db.created_at = contractor.created_at
            contractor_db.email = contractor.email
            contractor_db.phone_no = contractor.phone_no
            self.session.commit()

