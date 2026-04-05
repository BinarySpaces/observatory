from abc import ABC, abstractmethod


class ITelescopeAPI(ABC):
    """Interface for telescope API clients."""

    @abstractmethod
    def point(self, telescope_name, ra, dec) -> bool:
        """Sends a pointing command to the telescope."""
        pass
