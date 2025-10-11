from datetime import datetime

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from api.dependencies.dependencies import get_agent_repository, get_contractor_repository
from api.services.agent_service import AgentService
from api.services.contractor_service import ContractorService

router = APIRouter(
    prefix="/sign-up",
    tags=["sign-up"],
)

@router.post('/')
def sign_up(name: str,
            created_at: datetime,
            email: str,
            phone_no: str,
        contractor_repo =  Depends(get_contractor_repository),
        agent_repo = Depends(get_agent_repository)):

    contractor_service = ContractorService(contractor_repo)
    agent_service = AgentService(agent_repo)

    contractor = contractor_service.create_contractor(name, created_at, email, phone_no)
    agent = agent_service.create_agent(created_at=created_at, contractor_id=contractor.id)

    json_contractor = jsonable_encoder(contractor)
    json_agent = jsonable_encoder(agent)

    return JSONResponse({"contractor": json_contractor, "agent": json_agent})



