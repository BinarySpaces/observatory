from abc import ABC, abstractmethod

from src.stars.domain import Star


class IStarCommands(ABC):
    """Interface for write operations on the stars database repository."""

    @abstractmethod
    def save(self, star: Star) -> None:
        """Saves a single star to the database."""
        pass

    @abstractmethod
    def update(self, star: Star) -> None:
        """Updates an existing star in the database."""
        pass

    @abstractmethod
    def delete(self, star: Star) -> None:
        """Deletes a single star from the database."""
        pass

    @abstractmethod
    def delete_all(self) -> None:
        """Deletes all stars from the database."""
        pass
