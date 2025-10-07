from datetime import datetime
from typing import List
from fastapi import APIRouter
from fastapi.params import Depends

from api.dependencies.dependencies import get_contractor_repository
from api.models.schemas.contractor import Contractor
from api.services.contractor_service import ContractorService

router = APIRouter(
    prefix="/contractors",
    tags=["contractors"],
)

@router.get('/', response_model=List[Contractor])
def get_contractors(repo = Depends(get_contractor_repository)):
    service = ContractorService(repo)
    return service.get_bot_users()

@router.post('/')
def create_contractor(name: str,
                 created_at: datetime,
                 email: str,
                 phone_no: str,
                 repo = Depends(get_contractor_repository)):
    service = ContractorService(repo)
    contractor = service.create_contractor(name, created_at, email, phone_no)
    return contractor.model_dump()

