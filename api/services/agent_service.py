from typing import List

from api.models.schemas.agent import Agent
from api.repositories.agent_repository import AgentRepository


class AgentService:
    def __init__(self, repository: AgentRepository):
        self.repository = repository

    def get_agents(self) -> List[Agent]:
        return self.repository.get_all()
