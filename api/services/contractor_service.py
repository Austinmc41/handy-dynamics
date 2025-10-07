from typing import List

from api.models.schemas.contractor import Contractor
from api.repositories.contractor_repository import ContractorRepository


class ContractorService:
    def __init__(self, repository: ContractorRepository):
        self.repository = repository

    def get_bot_users(self) -> List[Contractor]:
        return self.repository.get_all()

    def create_contractor(self, name, created_at, email, phone_no) -> Contractor:
        contractor = Contractor(name=name, created_at=created_at, email=email, phone_no=phone_no)
        self.repository.add(contractor)
        return contractor
