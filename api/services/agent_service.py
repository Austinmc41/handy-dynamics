from typing import List

from api.models.schemas.agent import Agent
from api.repositories.agent_repository import AgentRepository


class AgentService:
    def __init__(self, repository: AgentRepository):
        self.repository = repository

    def get_agents(self) -> List[Agent]:
        return self.repository.get_all()

    def create_agent(self, created_at, contractor_id) -> Agent:
        agent = Agent(created_at=created_at, contractor_id=contractor_id)
        self.repository.add(agent)
        return agent
