from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends

from api.dependencies.dependencies import get_agent_repository
from api.models.schemas.agent import Agent
from api.services.agent_service import AgentService

router = APIRouter(
    prefix="/agents",
    tags=["agents"],
)

@router.get('/', response_model=List[Agent])
def get_agents(repo = Depends(get_agent_repository)):
    service = AgentService(repo)
    return service.get_agents()

@router.post('/')
def create_agent(created_at: datetime,
                 contractor_id: int,
                 repo = Depends(get_agent_repository)):
    service = AgentService(repo)
    agent = service.create_agent(created_at, contractor_id)
    return agent.model_dump()
