from abc import ABC, abstractmethod
from typing import Optional


class ISimbadDataProvider(ABC):
    """Interface for retrieving astronomical object names from SIMBAD."""

    @abstractmethod
    def get_name_by_coordinates(self, ra: float, dec: float) -> Optional[str]:
        """Fetches the common name of an object using its equatorial coordinates."""
        pass
