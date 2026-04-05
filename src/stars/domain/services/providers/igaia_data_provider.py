from abc import ABC, abstractmethod

from src.stars.domain import Star


class IGaiaDataProvider(ABC):
    """Interface for fetching star data from the Gaia archive."""

    @abstractmethod
    def get_stars(self, offset: int = 0) -> dict[int, Star]:
        """Retrieves stars from Gaia."""
        pass
