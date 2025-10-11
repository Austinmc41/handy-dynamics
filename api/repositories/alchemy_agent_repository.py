from typing import List, Optional

from api.models.db_models.agent_db import AgentDB
from api.models.schemas.agent import Agent
from api.repositories.agent_repository import AgentRepository
from sqlalchemy.orm import Session


class AlchemyAgentRepository(AgentRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Agent]:
        query_agents = self.session.query(AgentDB)
        return [
            Agent.model_validate(query_agent, from_attributes=True)
            for query_agent in query_agents.all()
        ]

    def add(self, agent):
        agent_db = AgentDB(**agent.dict())
        self.session.add(agent_db)
        self.session.commit()

    def get_by_id(self, agent_id: int) -> Optional[Agent]:
        agent_db = self.session.query(AgentDB).get(agent_id)
        if agent_db:
            return Agent.model_validate(agent_db, from_attributes=True)
        return None

    def update(self, agent: Agent):
        agent_db = self.session.query(AgentDB).get(agent.id)
        if agent_db:
            agent_db.created_at = agent.created_at
            agent_db.contractor_id = agent.contractor_id
            self.session.commit()
