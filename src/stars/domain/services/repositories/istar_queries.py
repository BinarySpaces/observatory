from abc import ABC, abstractmethod
from typing import Optional

from src.stars.domain import Star


class IStarQueries(ABC):
    """Interface for read operations on the stars database repository."""

    @abstractmethod
    def get_all(self, offset: int = None, limit: int = None) -> list[Star]:
        """Retrieves a paginated list of stars."""
        pass

    @abstractmethod
    def find(self, source_id: int) -> Optional[Star]:
        """Finds a star by its Gaia source_id."""
        pass
