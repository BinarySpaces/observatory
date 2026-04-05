from src.telescopes.domain import ITelescopeAPI


class TelescopeService:
    """
    Service for telescope pointing operations.
    Delegates the actual pointing command to the underlying API implementation.
    """

    def __init__(self, telescope_api: ITelescopeAPI) -> None:
        """Initializes the service with a telescope API client."""
        self.telescope_api = telescope_api

    # def find_best_telescope(self, ra: float, dec: float) -> Optional[Telescope]:
    #     for telescope in self.telescopes:
    #         if telescope.can_see(ra, dec):
    #             return telescope
    #     return None

    # def find_all_telescopes(self, ra: float, dec: float) -> list[Telescope]:
    #     return [
    #         telescope for telescope in self.telescopes
    #         if telescope.can_see(ra, dec)
    #     ]

    def point_to_star(self, ra: float, dec: float) -> bool:
        """Sends a pointing command to the telescope API."""
        return self.telescope_api.point(ra, dec)
