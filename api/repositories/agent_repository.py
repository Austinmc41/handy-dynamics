from abc import ABC, abstractmethod
from typing import List

from api.models.schemas.agent import Agent


class AgentRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Agent]:
        pass

    @abstractmethod
    def add(self, agent):
        pass

    @abstractmethod
    def get_by_id(self, agent_id):
        pass

    @abstractmethod
    def update(self, updated_agent):
        pass
